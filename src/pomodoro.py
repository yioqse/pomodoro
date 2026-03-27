"""
Módulo Principal: pomodoro.py

Punto de entrada para el temporizador Pomodoro interactivo.
Configura el entorno de ejecución asegurando la disponibilidad del directorio `src`
dentro del PATH y lanza el menú principal de la aplicación.
"""

import sys
import os

# Asegurar que el directorio src está en el path si se ejecuta desde fuera
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modules.menu import main_menu

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\nPrograma cerrado.")
        sys.exit(0)
