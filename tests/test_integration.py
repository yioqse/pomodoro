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
