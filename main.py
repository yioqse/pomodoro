#!/usr/bin/env python3
"""
🍅 Temporizador Pomodoro Interactivo
Punto de entrada desde la raíz del proyecto

Uso:
    python main.py
    
Este script sirve como punto de entrada alternativo que permite
ejecutar la aplicación Pomodoro desde la raíz del proyecto.
"""

import sys
import os

# Agregar src al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

try:
    from modules.menu import main_menu
    
    if __name__ == '__main__':
        main_menu()
        
except KeyboardInterrupt:
    print("\n\n¡Hasta luego! 👋")
    sys.exit(0)
except Exception as e:
    print(f"\n❌ Error: {e}")
    sys.exit(1)
