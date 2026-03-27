"""
Módulo de Notificaciones: notifier.py

Provee funciones para emitir sonidos del sistema (beeps) y notificaciones
visuales formateadas por consola. Abstrae la dependencia de la arquitectura
subyacente (Windows/Linux/OSX).
"""
import platform
import os

def play_sound(sound_type: str):
    """
    Reproduce un sonido específico dependiendo del sistema operativo.
    En Windows, utiliza `winsound.Beep` con frecuencias y duraciones dedicadas.
    En otros SO, apela al carácter de escape genérico de campana.

    Args:
        sound_type (str): El tipo de sonido lógico ('work_start', 'work_end', etc.).
    """
    system = platform.system()
    if system == 'Windows':
        import winsound
        freq_map = {
            'work_start': (1000, 500), 'work_end': (800, 500),
            'break_start': (600, 500), 'break_end': (1000, 500),
            'final': (1200, 1000)
        }
        freq, dur = freq_map.get(sound_type, (500, 500))
        winsound.Beep(freq, dur)
    else:
        print('\a', end='', flush=True)

def show_notification(message: str, style='info'):
    """
    Muestra un mensaje formateado en la terminal.
    """
    colors = {
        'info': '\033[1;33m',  # Amarillo
        'success': '\033[1;32m', # Verde
        'alert': '\033[1;31m',  # Rojo
        'reset': '\033[0m'
    }
    color = colors.get(style, colors['info'])
    print(f"{color}*** {message.upper()} ***{colors['reset']}")

def notify_work_start():
    """
    Dispara la notificación visual y el sonido de inicio de un bloque de trabajo.
    """
    show_notification("¡A trabajar! Concentración total.", 'info')
    play_sound('work_start')

def notify_work_end():
    """
    Dispara la notificación visual y el sonido de fin de un bloque de trabajo.
    """
    show_notification("¡Fin del bloque! Estiras las piernas.", 'success')
    play_sound('work_end')

def notify_break_start():
    """
    Dispara la notificación y el sonido correspondientes al inicio de un descanso.
    """
    show_notification("Inicio del descanso.", 'info')
    play_sound('break_start')

def notify_break_end():
    """
    Alerta al usuario sobre el final del periodo de descanso y el fin del silencio.
    """
    show_notification("El descanso ha terminado.", 'alert')
    play_sound('break_end')

def play_final_beep():
    """
    Dispara la indicación visual y sonora definitiva al finalizar la meta global de ciclos.
    """
    show_notification("¡Sesión finalizada con éxito!", 'success')
    play_sound('final')
