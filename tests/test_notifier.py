from unittest.mock import patch
from notificaciones import notifier

@patch('notificaciones.notifier.playsound', create=True)
def test_notify_work_start(mock_playsound):
    # Simula la llamada y asegura que no lance excepción
    # y además verifica que hace print (que es la Notificación visual)
    with patch('builtins.print') as mock_print:
        notifier.notify_work_start()
        mock_print.assert_called()

@patch('notificaciones.notifier.playsound', create=True)
def test_notify_break_start(mock_playsound):
    with patch('builtins.print') as mock_print:
        notifier.notify_break_start()
        mock_print.assert_called()
