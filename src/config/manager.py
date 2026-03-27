"""
Módulo de Configuración: manager.py

Gestiona los ajustes y parámetros por defecto del temporizador Pomodoro.
Provee funciones interactivas para modificar los tiempos (trabajo, descansos) y 
la cantidad total de ciclos a cumplir por sesión matemática.
"""

DEFAULT_CONFIG = {
    'work_time': 25.0,
    'break_time': 5.0,
    'long_break_time': 15.0,
    'total_cycles': 4
}

TIMER_CONFIG = DEFAULT_CONFIG.copy()

def get_positive_value(prompt, default, is_int=False):
    """
    Solicita un valor numérico positivo interactivo por terminal.

    Args:
        prompt (str): Texto a mostrar solicitando la entrada de datos.
        default (float|int): Valor que se utilizará si el input queda vacío.
        is_int (bool): Fuerza el retorno a tipo entero si es True.

    Returns:
        float o int: El valor ingresado válido mayor a cero.
    """
    while True:
        try:
            user_input = input(f"{prompt} (por defecto {default}): ").strip()
            if not user_input: return default
            value = float(user_input)
            if value <= 0:
                print("Error: El valor debe ser mayor que cero.")
                continue
            return int(value) if is_int else value
        except ValueError:
            print("Error: Por favor, ingresa un número válido.")

def configure():
    """
    Despliega un asistente en terminal para actualizar globalmente `TIMER_CONFIG` 
    pidiendo al usuario introducir nuevos límites de tiempo y la meta de ciclos.
    """
    print("\n--- Configuración Personalizada ---")
    TIMER_CONFIG['work_time'] = get_positive_value("Tiempo de trabajo (minutos)", DEFAULT_CONFIG['work_time'])
    TIMER_CONFIG['break_time'] = get_positive_value("Tiempo de descanso corto (minutos)", DEFAULT_CONFIG['break_time'])
    TIMER_CONFIG['long_break_time'] = get_positive_value("Tiempo de descanso largo (minutos)", DEFAULT_CONFIG['long_break_time'])
    TIMER_CONFIG['total_cycles'] = get_positive_value("Número de ciclos", DEFAULT_CONFIG['total_cycles'], is_int=True)
    print("\n[OK] Configuración guardada correctamente.")
