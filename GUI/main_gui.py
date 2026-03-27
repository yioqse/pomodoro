"""
🍅 GUI Principal - Temporizador Pomodoro con Tkinter

Aplicación gráfica completa del temporizador Pomodoro.
Integra todos los componentes de la interfaz visual.
"""

import tkinter as tk
from tkinter import messagebox
import sys
import os
import time
import threading

# Agregar src al path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from styles import COLORS, FONTS, SPACING
from widgets import (
    ModernButton, BreakButton, StopButton, TimerDisplay,
    ProgressBar, ModernEntry, ModernFrame, StatusLabel
)
from config.manager import DEFAULT_CONFIG, TIMER_CONFIG, configure, get_positive_value
from notificaciones.notifier import (
    notify_work_start, notify_work_end, notify_break_start,
    notify_break_end, play_final_beep
)


class PomodoroGUI:
    """Aplicación principal de GUI para Pomodoro."""
    
    def __init__(self, root):
        """Inicializa la aplicación."""
        self.root = root
        self.root.title('🍅 Temporizador Pomodoro')
        self.root.geometry('500x600')
        self.root.config(bg=COLORS['bg_dark'])
        self.root.resizable(False, False)
        
        # Variables de control
        self.running = False
        self.paused = False
        self.timer_thread = None
        self.elapsed_seconds = 0
        self.total_seconds = 0
        self.current_phase = None  # 'work' o 'break'
        self.cycle_count = 0
        self.completed_pomodoros = 0
        
        # Cargar configuración
        self.config = TIMER_CONFIG.copy()
        
        # Crear interfaz
        self.create_ui()
    
    def create_ui(self):
        """Crea la interfaz principal."""
        # Menú principal
        self.create_menu_frame()
        
        # Frame principal
        self.main_frame = ModernFrame(
            self.root,
            bg=COLORS['bg_dark'],
            padx=SPACING['lg'],
            pady=SPACING['lg']
        )
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Inicialmente mostrar menú
        self.show_menu()
    
    def create_menu_frame(self):
        """Crea el frame del menú principal."""
        # Limpiar frame principal
        for widget in self.main_frame.winfo_children() if hasattr(self, 'main_frame') else []:
            widget.destroy()
    
    def show_menu(self):
        """Muestra el menú principal."""
        self.clear_main_frame()
        
        # Título
        title = tk.Label(
            self.main_frame,
            text='🍅 TEMPORIZADOR POMODORO',
            font=FONTS['title_large'],
            fg=COLORS['tomato'],
            bg=COLORS['bg_dark']
        )
        title.pack(pady=SPACING['xl'])
        
        # Descripción
        desc = tk.Label(
            self.main_frame,
            text='Técnica Pomodoro para optimizar tu productividad',
            font=FONTS['body_small'],
            fg=COLORS['gray'],
            bg=COLORS['bg_dark']
        )
        desc.pack(pady=SPACING['sm'])
        
        # Espaciador
        tk.Label(self.main_frame, bg=COLORS['bg_dark']).pack(pady=SPACING['lg'])
        
        # Botones principales
        btn_start = ModernButton(
            self.main_frame,
            text='▶️ Iniciar Sesión',
            command=self.show_session
        )
        btn_start.pack(fill=tk.X, pady=SPACING['md'])
        
        btn_config = ModernButton(
            self.main_frame,
            text='⚙️ Configuración',
            bg=COLORS['gray_dark'],
            command=self.show_config
        )
        btn_config.pack(fill=tk.X, pady=SPACING['md'])
        
        btn_stats = ModernButton(
            self.main_frame,
            text='📊 Estadísticas',
            bg=COLORS['info'],
            command=self.show_stats
        )
        btn_stats.pack(fill=tk.X, pady=SPACING['md'])
        
        # Espaciador
        tk.Label(self.main_frame, bg=COLORS['bg_dark']).pack(pady=SPACING['xl'])
        
        # Configuración actual
        config_text = f"""
Configuración Actual:
• Trabajo: {self.config['work_time']:.0f} min
• Descanso: {self.config['break_time']:.0f} min
• Descanso Largo: {self.config['long_break_time']:.0f} min
• Ciclos: {self.config['total_cycles']}
        """
        config_label = tk.Label(
            self.main_frame,
            text=config_text.strip(),
            font=FONTS['body_small'],
            fg=COLORS['gray_light'],
            bg=COLORS['bg_dark'],
            justify=tk.LEFT
        )
        config_label.pack(pady=SPACING['lg'])
        
        # Espaciador
        tk.Label(self.main_frame, bg=COLORS['bg_dark']).pack(pady=SPACING['xl'])
        
        # Botón salir
        btn_exit = ModernButton(
            self.main_frame,
            text='❌ Salir',
            bg=COLORS['error'],
            command=self.root.quit
        )
        btn_exit.pack(fill=tk.X, pady=SPACING['md'])
    
    def show_config(self):
        """Muestra pantalla de configuración."""
        self.clear_main_frame()
        
        # Título
        title = tk.Label(
            self.main_frame,
            text='⚙️ CONFIGURACIÓN',
            font=FONTS['title_medium'],
            fg=COLORS['info'],
            bg=COLORS['bg_dark']
        )
        title.pack(pady=SPACING['lg'])
        
        # Formulario
        entries = {}
        fields = [
            ('work_time', 'Tiempo de Trabajo (min):', 25),
            ('break_time', 'Descanso Corto (min):', 5),
            ('long_break_time', 'Descanso Largo (min):', 15),
            ('total_cycles', 'Número de Ciclos:', 4),
        ]
        
        for key, label, default in fields:
            frame = ModernFrame(self.main_frame, bg=COLORS['bg_dark'])
            frame.pack(fill=tk.X, pady=SPACING['md'])
            
            lbl = tk.Label(
                frame,
                text=label,
                font=FONTS['body_small'],
                fg=COLORS['fg_light'],
                bg=COLORS['bg_dark']
            )
            lbl.pack(anchor=tk.W)
            
            entry = ModernEntry(frame, width=20)
            entry.insert(0, str(int(self.config[key])))
            entry.pack(fill=tk.X, pady=SPACING['sm'])
            entries[key] = entry
        
        # Botones
        btn_frame = ModernFrame(self.main_frame, bg=COLORS['bg_dark'])
        btn_frame.pack(fill=tk.X, pady=SPACING['lg'])
        
        def save_config():
            try:
                for key, entry in entries.items():
                    value = float(entry.get())
                    if value <= 0:
                        raise ValueError('Los valores deben ser positivos')
                    self.config[key] = value
                
                # Actualizar configuración global
                import config.manager as cm
                cm.TIMER_CONFIG = self.config.copy()
                
                messagebox.showinfo('Éxito', 'Configuración guardada')
                self.show_menu()
            except Exception as e:
                messagebox.showerror('Error', f'Error: {str(e)}')
        
        btn_save = ModernButton(btn_frame, text='✓ Guardar', command=save_config)
        btn_save.pack(side=tk.LEFT, padx=SPACING['sm'])
        
        btn_cancel = StopButton(btn_frame, text='✕ Cancelar', command=self.show_menu)
        btn_cancel.pack(side=tk.LEFT, padx=SPACING['sm'])
    
    def show_stats(self):
        """Muestra estadísticas."""
        self.clear_main_frame()
        
        # Título
        title = tk.Label(
            self.main_frame,
            text='📊 ESTADÍSTICAS',
            font=FONTS['title_medium'],
            fg=COLORS['info'],
            bg=COLORS['bg_dark']
        )
        title.pack(pady=SPACING['lg'])
        
        stats_text = f"""
Sesión Actual:
━━━━━━━━━━━━━━━━━━━━
• Ciclos Completados: {self.completed_pomodoros}
• Ciclo Actual: {self.cycle_count}/{int(self.config['total_cycles'])}

Configuración:
━━━━━━━━━━━━━━━━━━━━
• Tiempo de Trabajo: {self.config['work_time']:.0f} min
• Descanso Corto: {self.config['break_time']:.0f} min
• Descanso Largo: {self.config['long_break_time']:.0f} min

Tiempo Estimado:
━━━━━━━━━━━━━━━━━━━━
• Total de Sesión: ~{self.calculate_total_time():.0f} min
        """
        
        stats_label = tk.Label(
            self.main_frame,
            text=stats_text.strip(),
            font=FONTS['body_small'],
            fg=COLORS['gray_light'],
            bg=COLORS['bg_dark'],
            justify=tk.LEFT
        )
        stats_label.pack(pady=SPACING['lg'])
        
        # Botón volver
        btn_back = ModernButton(
            self.main_frame,
            text='← Volver',
            bg=COLORS['gray_dark'],
            command=self.show_menu
        )
        btn_back.pack(fill=tk.X, pady=SPACING['lg'])
    
    def calculate_total_time(self):
        """Calcula el tiempo total estimado."""
        work = self.config['work_time'] * self.config['total_cycles']
        breaks = self.config['break_time'] * (self.config['total_cycles'] - 1)
        long_breaks = self.config['long_break_time']  # cada 4 ciclos
        return work + breaks + long_breaks
    
    def show_session(self):
        """Muestra la pantalla de sesión."""
        self.clear_main_frame()
        
        # Información de ciclo
        self.cycle_count = 1
        self.completed_pomodoros = 0
        
        # Título de ciclo
        self.title_label = tk.Label(
            self.main_frame,
            text=f'Ciclo {self.cycle_count}/{int(self.config["total_cycles"])} - TRABAJO',
            font=FONTS['title_medium'],
            fg=COLORS['tomato'],
            bg=COLORS['bg_dark']
        )
        self.title_label.pack(pady=SPACING['lg'])
        
        # Display de tiempo
        self.time_display = TimerDisplay(self.main_frame)
        self.time_display.pack(pady=SPACING['lg'])
        
        # Barra de progreso
        self.progress_bar = ProgressBar(self.main_frame, radius=80)
        self.progress_bar.pack(pady=SPACING['lg'])
        
        # Etiqueta de estado
        self.status_label = StatusLabel(self.main_frame)
        self.status_label.set_idle()
        self.status_label.pack(pady=SPACING['md'])
        
        # Botones de control
        btn_frame = ModernFrame(self.main_frame, bg=COLORS['bg_dark'])
        btn_frame.pack(fill=tk.X, pady=SPACING['lg'])
        
        self.btn_start = ModernButton(
            btn_frame,
            text='▶️ Iniciar',
            command=self.start_session
        )
        self.btn_start.pack(side=tk.LEFT, padx=SPACING['sm'])
        
        self.btn_pause = ModernButton(
            btn_frame,
            text='⏸️ Pausa',
            bg=COLORS['warning'],
            command=self.toggle_pause,
            state=tk.DISABLED
        )
        self.btn_pause.pack(side=tk.LEFT, padx=SPACING['sm'])
        
        self.btn_stop = StopButton(
            btn_frame,
            text='⏹️ Detener',
            command=self.stop_session,
            state=tk.DISABLED
        )
        self.btn_stop.pack(side=tk.LEFT, padx=SPACING['sm'])
        
        # Botón volver
        btn_menu = ModernButton(
            self.main_frame,
            text='← Menú',
            bg=COLORS['gray_dark'],
            command=lambda: self.show_menu() if not self.running else None
        )
        btn_menu.pack(fill=tk.X, pady=SPACING['lg'])
    
    def start_session(self):
        """Inicia la sesión."""
        self.running = True
        self.paused = False
        
        # Actualizar botones
        self.btn_start.config(state=tk.DISABLED)
        self.btn_pause.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.NORMAL)
        
        # Iniciar en thread
        self.timer_thread = threading.Thread(target=self.run_session, daemon=True)
        self.timer_thread.start()
    
    def run_session(self):
        """Ejecuta la sesión (en thread)."""
        try:
            for cycle in range(1, int(self.config['total_cycles']) + 1):
                if not self.running:
                    break
                
                self.cycle_count = cycle
                
                # Trabajo
                self.current_phase = 'work'
                self.root.after(0, self.update_title, f'Ciclo {cycle}/{int(self.config["total_cycles"])} - TRABAJO')
                self.root.after(0, self.status_label.set_working)
                notify_work_start()
                
                if not self.run_countdown(self.config['work_time'] * 60):
                    break
                
                self.completed_pomodoros += 1
                self.root.after(0, self.status_label.set_idle)
                notify_work_end()
                
                if cycle < int(self.config['total_cycles']):
                    # Descanso
                    is_long = cycle % 4 == 0
                    break_time = self.config['long_break_time'] if is_long else self.config['break_time']
                    break_label = 'DESCANSO LARGO' if is_long else 'DESCANSO'
                    
                    self.current_phase = 'break'
                    self.root.after(0, self.update_title, f'Ciclo {cycle}/{int(self.config["total_cycles"])} - {break_label}')
                    self.root.after(0, self.status_label.set_breaking)
                    notify_break_start()
                    
                    if not self.run_countdown(break_time * 60):
                        break
                    
                    self.root.after(0, self.status_label.set_idle)
                    notify_break_end()
            
            # Sesión completada
            if self.running:
                self.root.after(0, self.session_completed)
        
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror('Error', str(e)))
        finally:
            self.running = False
            self.root.after(0, self.reset_buttons)
    
    def run_countdown(self, total_seconds):
        """Ejecuta una cuenta regresiva."""
        self.total_seconds = total_seconds
        self.elapsed_seconds = 0
        
        while self.elapsed_seconds < total_seconds and self.running:
            if not self.paused:
                self.elapsed_seconds += 1
                
                # Actualizar display
                remaining = total_seconds - self.elapsed_seconds
                minutes = remaining // 60
                seconds = remaining % 60
                percentage = (self.elapsed_seconds / total_seconds) * 100
                
                self.root.after(0, self.time_display.update_time, minutes, seconds)
                self.root.after(0, self.progress_bar.update_progress, percentage)
                
                time.sleep(1)
            else:
                time.sleep(0.1)
        
        return self.running
    
    def toggle_pause(self):
        """Pausa/Reanuda la sesión."""
        self.paused = not self.paused
        if self.paused:
            self.status_label.set_paused()
            self.btn_pause.config(text='▶️ Reanudar')
        else:
            if self.current_phase == 'work':
                self.status_label.set_working()
            else:
                self.status_label.set_breaking()
            self.btn_pause.config(text='⏸️ Pausa')
    
    def stop_session(self):
        """Detiene la sesión."""
        self.running = False
        self.paused = False
        self.show_menu()
    
    def session_completed(self):
        """Sesión completada."""
        play_final_beep()
        messagebox.showinfo(
            'Sesión Completada',
            f'¡Sesión finalizada!\n\n'
            f'Ciclos completados: {self.completed_pomodoros}\n'
            f'Tiempo aproximado: {self.calculate_total_time():.0f} minutos'
        )
        self.show_menu()
    
    def reset_buttons(self):
        """Resetea los botones."""
        self.btn_start.config(state=tk.NORMAL)
        self.btn_pause.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.DISABLED)
    
    def update_title(self, text):
        """Actualiza el título del ciclo."""
        self.title_label.config(text=text)
    
    def clear_main_frame(self):
        """Limpia el frame principal."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()


def main():
    """Función principal."""
    root = tk.Tk()
    app = PomodoroGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
