from unittest.mock import patch
from modules.timer import PomodoroTimer

@patch('modules.timer.time.sleep', return_value=None)
@patch('notificaciones.notifier.playsound', create=True)
def test_full_pomodoro_session_cycle(mock_playsound, mock_sleep):
    config = {
        'work_time': 0.01, # tiempo extremadamente corto
        'break_time': 0.01,
        'long_break_time': 0.01,
        'total_cycles': 1
    }
    timer = PomodoroTimer(config)
    # Mockear input y keyboard listener para que no bloquee esperando respuesta en consola
    with patch.object(timer, 'keyboard_listener', return_value=None):
        with patch('builtins.input', return_value=''):
            timer.run_session()
            assert timer.completed_pomodoros == 1

# Tests para main.py
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

def test_main_menu_with_cli_argument():
    """Prueba que main.py procesa correctamente el argumento 'cli'."""
    from main import show_main_menu

    # Simular argumentos
    original_argv = sys.argv
    sys.argv = ['main.py', 'cli']

    try:
        result = show_main_menu()
        assert result == 'cli', f"Esperado 'cli', obtenido '{result}'"
    finally:
        sys.argv = original_argv

def test_main_menu_with_gui_argument():
    """Prueba que main.py procesa correctamente el argumento 'gui'."""
    from main import show_main_menu

    # Simular argumentos
    original_argv = sys.argv
    sys.argv = ['main.py', 'gui']

    try:
        result = show_main_menu()
        assert result == 'gui', f"Esperado 'gui', obtenido '{result}'"
    finally:
        sys.argv = original_argv

def test_main_menu_with_invalid_argument():
    """Prueba que main.py maneja correctamente argumentos inválidos."""
    from main import show_main_menu
    import pytest

    # Simular argumentos inválidos
    original_argv = sys.argv
    sys.argv = ['main.py', 'invalid']

    try:
        with pytest.raises(SystemExit):
            show_main_menu()
    finally:
        sys.argv = original_argv

def test_main_menu_piped_input():
    """Prueba que main.py detecta entrada piped y usa CLI por defecto."""
    from main import show_main_menu
    from unittest.mock import patch

    # Simular entrada no interactiva
    with patch('sys.stdin.isatty', return_value=False):
        result = show_main_menu()
        assert result == 'cli', f"Esperado 'cli' para entrada piped, obtenido '{result}'"
