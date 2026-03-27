"""
Módulo de Interfaz Principal: menu.py

Gestiona la interfaz de consola principal del Temporizador Pomodoro Pro.
Permite iniciar la sesión, configurar los tiempos personalizados y salir de la aplicación.
"""

import time
import sys
from .timer import PomodoroTimer
from config import TIMER_CONFIG, configure

def main_menu():
    """Muestra el menú principal y gestiona la navegación."""
    timer_app = PomodoroTimer(TIMER_CONFIG)
    
    while True:
        timer_app.clear_screen()
        print("========================================")
        print("     TEMPORIZADOR POMODORO PRO         ")
        print("========================================")
        print(" 1) Iniciar Sesión")
        print(" 2) Configurar Tiempos")
        print(" 3) Salir")
        print("----------------------------------------")
        
        choice = input("Selecciona una opción: ").strip()

        if choice == '1':
            timer_app.exit_event.clear()
            timer_app.pause_event.clear()
            timer_app.run_session()
        elif choice == '2':
            configure()
        elif choice == '3':
            print("¡Hasta pronto!")
            sys.exit(0)
        else:
            print("Opción no válida.")
            time.sleep(1)
