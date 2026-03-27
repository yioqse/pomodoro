import sys
import os

# Agrega la carpeta src al PYTHONPATH para que los tests puedan importar los módulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
