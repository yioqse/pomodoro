#!/usr/bin/env python3
"""
🍅 Lanzador de GUI - Temporizador Pomodoro

Script para iniciar la interfaz gráfica de Pomodoro desde cualquier ubicación.

Uso:
    python gui_launcher.py
"""

import sys
import os

# Agregar src y GUI al path
project_root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(project_root, 'src'))
sys.path.insert(0, os.path.join(project_root, 'GUI'))

try:
    from GUI.main_gui import main
    
    if __name__ == '__main__':
        print('🍅 Iniciando Temporizador Pomodoro (GUI)...')
        main()

except ImportError as e:
    print(f'❌ Error de importación: {e}')
    print('Asegúrate de tener tkinter instalado: pip install tk')
    sys.exit(1)
except Exception as e:
    print(f'❌ Error: {e}')
    sys.exit(1)
