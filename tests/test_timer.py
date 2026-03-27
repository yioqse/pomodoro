from modules.timer import PomodoroTimer

def test_draw_progress_bar_zero():
    timer = PomodoroTimer({'total_cycles': 1})
    bar = timer.draw_progress_bar(0, 100, width=10)
    assert bar == "[----------]   0%"

def test_draw_progress_bar_half():
    timer = PomodoroTimer({'total_cycles': 1})
    bar = timer.draw_progress_bar(50, 100, width=10)
    assert bar == "[█████-----]  50%"

def test_draw_progress_bar_full():
    timer = PomodoroTimer({'total_cycles': 1})
    bar = timer.draw_progress_bar(100, 100, width=10)
    assert bar == "[██████████] 100%"

def test_draw_progress_bar_invalid():
    timer = PomodoroTimer({'total_cycles': 1})
    bar = timer.draw_progress_bar(50, 0, width=10)
    assert bar == "[ERROR] Tiempo inválido"
