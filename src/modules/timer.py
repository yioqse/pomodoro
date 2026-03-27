"""
Módulo del Temporizador: timer.py

Contiene la lógica de ejecución del cuenta atrás, el renderizado de la barra 
de progreso interactiva en terminal y las iteraciones del ciclo Pomodoro.
Permite ejecutar subprocesos para escuchar activamente la interrupción de teclado.
"""
import os
import time
import platform
import sys
import threading
from typing import Dict, Any

# Importaciones desde los nuevos paquetes
from config import TIMER_CONFIG
from notificaciones import (
    notify_work_start, notify_work_end, 
    notify_break_start, notify_break_end, 
    play_final_beep
)

class PomodoroTimer:
    """
    Controlador principal de un temporizador Pomodoro basado en consola.
    Se apoya en la configuración provista y orquesta los tiempos, notificaciones 
    y controles asíncronos de pausa/reanudación.
    """
    def __init__(self, config: Dict[str, Any]):
        """
        Inicializa la instancia del temporizador.

        Args:
            config (Dict[str, Any]): Configuración actual conteniento parámetros
                                     como 'work_time', 'break_time' y 'total_cycles'.
        """
        self.config = config
        self.pause_event = threading.Event()
        self.exit_event = threading.Event()
        self.system = platform.system()
        self.completed_pomodoros = 0

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_progress_bar(self, elapsed: float, total: float, width: int = 20) -> str:
        """
        Genera una representación visual de cadena de una barra de progreso sólida.

        Args:
            elapsed (float): Segundos transcurridos en la actual cuenta regresiva.
            total (float): Segundos totales a contar de la meta actual.
            width (int, opcional): Tamaño visual total de la barra.

        Returns:
            str: Una cadena formateada que representa la barra y porcentaje actual.
        """
        if total <= 0: return "[ERROR] Tiempo inválido"
        progress = min(max(elapsed / total, 0), 1)
        filled = int(progress * width)
        bar = '█' * filled + '-' * (width - filled)
        return f"[{bar}] {int(progress * 100):3d}%"

    def countdown(self, minutes: float, label: str = "Tiempo"):
        """
        Ejecuta un bucle principal de cuenta regresiva que pausa el subproceso actual 
        por ventanas 1 segundo para redibujar la terminal consistentemente en tiempo real.

        Args:
            minutes (float): Los minutos objetivo de esta fase específica.
            label (str): Título conceptual (ej: 'TRABAJO') emitir con la métrica.
        """
        total_seconds = int(minutes * 60)
        elapsed = 0
        while total_seconds > 0 and not self.exit_event.is_set():
            if self.pause_event.is_set():
                sys.stdout.write(f"\r[PAUSADO] {label} - 'p' reanudar")
                sys.stdout.flush()
                time.sleep(0.5)
                continue
                
            mins, secs = divmod(total_seconds, 60)
            timer_str = f"{int(mins):02d}:{int(secs):02d}"
            bar = self.draw_progress_bar(elapsed, minutes * 60, width=20)
            
            # Imprimir siempre cada segundo (ancho reducido para evitar saltos de línea)
            sys.stdout.write(f"\r{label}: {bar} {timer_str}  ")
            sys.stdout.flush()
            
            time.sleep(1)
            total_seconds -= 1
            elapsed += 1
            
        if not self.exit_event.is_set():
            bar = self.draw_progress_bar(1, 1, width=20)
            sys.stdout.write(f"\r{label}: {bar} 00:00 - ¡Completado!  \n")
            sys.stdout.flush()

    def keyboard_listener(self):
        """
        Hilo en segundo plano para manejar interrupciones no bloqueantes dinámicas, 
        interpretando activamente la presión de pausa ('p') y la salida anticipada ('q').
        """
        if self.system != 'Windows': import select
        while not self.exit_event.is_set():
            key = None
            try:
                if self.system == 'Windows':
                    import msvcrt
                    if msvcrt.kbhit(): key = msvcrt.getwch().lower()
                else:
                    import select
                    if select.select([sys.stdin], [], [], 0.1)[0]: key = sys.stdin.read(1).lower()
            except Exception: pass
            if key == 'p':
                if self.pause_event.is_set():
                    self.pause_event.clear()
                    print("\n>>> REANUDADO <<<")
                else:
                    self.pause_event.set()
                    print("\n>>> PAUSADO <<<")
            elif key == 'q':
                self.exit_event.set()
                print("\n>>> SALIENDO... <<<")
                break
            time.sleep(0.1)

    def run_session(self):
        """
        Inicia la coreografía completa de los ciclos de Pomodoro de la sesión.
        Transita intermitentemente entre las fases de trabajo, descansos e hitos, 
        lanzando el control del teclado interactivo durante la duración configurada.
        """
        total_goal = self.config['total_cycles']
        if total_goal <= 0: return
        self.completed_pomodoros = 0
        threading.Thread(target=self.keyboard_listener, daemon=True).start()
        for cycle in range(1, total_goal + 1):
            if self.exit_event.is_set(): break
            print(f"\n--- CICLO {cycle} DE {total_goal} ---")
            notify_work_start()
            self.countdown(self.config['work_time'], "TRABAJO")
            if self.exit_event.is_set(): break
            notify_work_end()
            self.completed_pomodoros += 1
            if cycle < total_goal:
                is_long = (cycle % 4 == 0)
                wait_time = self.config['long_break_time'] if is_long else self.config['break_time']
                notify_break_start()
                self.countdown(wait_time, "DESCANSO")
                if self.exit_event.is_set(): break
                notify_break_end()
        if not self.exit_event.is_set():
            play_final_beep()
            print(f"\n¡SESIÓN TERMINADA! Total: {self.completed_pomodoros}")
            input("\nPresiona Enter para volver...")
