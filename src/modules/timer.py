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
import json
from datetime import datetime
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
        
        # Sistema de logging
        self.session_log = {
            'session_start': None,
            'session_end': None,
            'total_cycles_completed': 0,
            'work_pauses': 0,
            'break_pauses': 0,
            'total_work_pause_time': 0,
            'total_break_pause_time': 0,
            'cycles': []
        }
        self.current_cycle_log = None
        self.pause_start_time = None
        self.current_phase = None  # 'work' o 'break'

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
        self.current_phase = 'work' if 'TRABAJO' in label else 'break'
        total_seconds = int(minutes * 60)
        elapsed = 0
        
        while total_seconds > 0 and not self.exit_event.is_set():
            if self.pause_event.is_set():
                if self.pause_start_time is None:
                    self.pause_start_time = time.time()
                sys.stdout.write(f"\r[PAUSADO] {label} - 'p' reanudar")
                sys.stdout.flush()
                time.sleep(0.5)
                continue
            else:
                # Si acabamos de reanudar, calcular tiempo pausado
                if self.pause_start_time is not None:
                    pause_duration = time.time() - self.pause_start_time
                    if self.current_phase == 'work':
                        self.session_log['work_pauses'] += 1
                        self.session_log['total_work_pause_time'] += pause_duration
                    else:
                        self.session_log['break_pauses'] += 1
                        self.session_log['total_break_pause_time'] += pause_duration
                    self.pause_start_time = None
                
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
        # Inicializar logging de sesión
        self.session_log['session_start'] = datetime.now().isoformat()
        
        total_goal = self.config['total_cycles']
        if total_goal <= 0: return
        self.completed_pomodoros = 0
        threading.Thread(target=self.keyboard_listener, daemon=True).start()
        
        for cycle in range(1, total_goal + 1):
            if self.exit_event.is_set(): break
            
            # Iniciar log del ciclo
            self.current_cycle_log = {
                'cycle_number': cycle,
                'work_start': datetime.now().isoformat(),
                'work_end': None,
                'break_start': None,
                'break_end': None,
                'break_type': None
            }
            
            print(f"\n--- CICLO {cycle} DE {total_goal} ---")
            notify_work_start()
            self.countdown(self.config['work_time'], "TRABAJO")
            if self.exit_event.is_set(): break
            notify_work_end()
            self.completed_pomodoros += 1
            
            # Registrar fin del trabajo
            self.current_cycle_log['work_end'] = datetime.now().isoformat()
            
            if cycle < total_goal:
                is_long = (cycle % 4 == 0)
                wait_time = self.config['long_break_time'] if is_long else self.config['break_time']
                break_type = "LARGO" if is_long else "CORTO"
                
                # Registrar inicio del descanso
                self.current_cycle_log['break_start'] = datetime.now().isoformat()
                self.current_cycle_log['break_type'] = break_type
                
                notify_break_start()
                self.countdown(wait_time, f"DESCANSO {break_type}")
                if self.exit_event.is_set(): break
                notify_break_end()
                
                # Registrar fin del descanso
                self.current_cycle_log['break_end'] = datetime.now().isoformat()
            
            # Agregar ciclo al log de la sesión
            self.session_log['cycles'].append(self.current_cycle_log)
        
        # Agregar descanso largo al FINAL de TODOS los ciclos marcados
        if not self.exit_event.is_set() and self.completed_pomodoros > 0:
            print(f"\n--- DESCANSO LARGO FINAL ---")
            print("¡Felicitaciones! Has completado todos los ciclos marcados.")
            print("Tómate un descanso largo bien merecido.")
            
            # Registrar descanso largo final
            final_break_log = {
                'cycle_number': 'FINAL',
                'work_start': None,
                'work_end': None,
                'break_start': datetime.now().isoformat(),
                'break_end': None,
                'break_type': 'LARGO FINAL'
            }
            
            notify_break_start()
            self.countdown(self.config['long_break_time'], "DESCANSO LARGO FINAL")
            if not self.exit_event.is_set():
                notify_break_end()
                final_break_log['break_end'] = datetime.now().isoformat()
                self.session_log['cycles'].append(final_break_log)
        
        # Finalizar logging de sesión
        self.session_log['session_end'] = datetime.now().isoformat()
        self.session_log['total_cycles_completed'] = self.completed_pomodoros
        
        # Guardar log en archivo JSON
        self.save_session_log()
        
        if not self.exit_event.is_set():
            play_final_beep()
            print(f"\n¡SESIÓN TERMINADA! Total: {self.completed_pomodoros}")
            self.show_session_summary()
            input("\nPresiona Enter para volver...")

    def save_session_log(self):
        """Guarda el log de la sesión en un archivo JSON."""
        try:
            # Crear directorio logs si no existe
            logs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'logs')
            os.makedirs(logs_dir, exist_ok=True)
            
            # Nombre del archivo con timestamp
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"pomodoro_session_{timestamp}.json"
            filepath = os.path.join(logs_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.session_log, f, indent=2, ensure_ascii=False)
            
            print(f"\n📊 Log guardado en: {filepath}")
            
        except Exception as e:
            print(f"\n⚠️  Error al guardar el log: {e}")

    def show_session_summary(self):
        """Muestra un resumen de la sesión completada."""
        print("\n" + "="*50)
        print("📊 RESUMEN DE LA SESIÓN")
        print("="*50)
        
        # Información básica
        start_time = datetime.fromisoformat(self.session_log['session_start'])
        end_time = datetime.fromisoformat(self.session_log['session_end'])
        duration = end_time - start_time
        
        print(f"⏰ Duración total: {duration.seconds // 3600}h {(duration.seconds % 3600) // 60}m")
        print(f"🍅 Ciclos completados: {self.session_log['total_cycles_completed']}")
        
        # Información de pausas
        work_pauses = self.session_log['work_pauses']
        break_pauses = self.session_log['break_pauses']
        total_work_pause = self.session_log['total_work_pause_time']
        total_break_pause = self.session_log['total_break_pause_time']
        
        print(f"\n⏸️  Pausas durante trabajo: {work_pauses} ({int(total_work_pause)}s)")
        print(f"⏸️  Pausas durante descanso: {break_pauses} ({int(total_break_pause)}s)")
        
        # Detalle de ciclos
        print(f"\n📋 Detalle de ciclos:")
        for cycle in self.session_log['cycles']:
            if cycle['cycle_number'] == 'FINAL':
                print(f"   🏁 Descanso largo final: {self.config['long_break_time']} min")
            else:
                break_type = cycle['break_type']
                if break_type:
                    print(f"   🍅 Ciclo {cycle['cycle_number']}: Trabajo + Descanso {break_type}")
        
        print("="*50)
