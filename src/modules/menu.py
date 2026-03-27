"""
Módulo de Interfaz Principal: menu.py

Gestiona la interfaz de consola principal del Temporizador Pomodoro Pro.
Permite iniciar la sesión, configurar los tiempos personalizados y salir de la aplicación.
"""

import time
import sys
from datetime import datetime, timedelta
from .timer import PomodoroTimer
from config import TIMER_CONFIG, configure

# Configuración global de jornada laboral
WORK_SCHEDULE = {
    'hours': 5,
    'start_hour': 9,
    'label': '5 horas (09:00 - 14:00)'
}

def show_schedule(hours: int = 5, start_hour: int = 9):
    """Muestra los horarios de descanso calculados para una jornada laboral.
    
    Args:
        hours (int): Duración de la jornada laboral en horas (3, 5 u 8)
        start_hour (int): Hora de inicio de la jornada (por defecto 9:00 AM)
    """
    print(f"\n--- HORARIOS DE DESCANSO ({start_hour:02d}:00 - {start_hour + hours:02d}:00) ---")
    
    # Horario de inicio
    start_time = datetime.strptime(f"{start_hour:02d}:00", "%H:%M")
    end_time = datetime.strptime(f"{start_hour + hours:02d}:00", "%H:%M")
    
    current_time = start_time
    cycle_count = 1
    
    print(f"⏰ Horario laboral: {start_time.strftime('%H:%M')} - {end_time.strftime('%H:%M')}")
    print(f"⚙️  Configuración: {TIMER_CONFIG['work_time']}min trabajo, {TIMER_CONFIG['break_time']}min descanso corto, {TIMER_CONFIG['long_break_time']}min descanso largo")
    print("\n📅 Calendario de descansos:")
    
    while current_time < end_time:
        # Trabajo
        work_end = current_time + timedelta(minutes=TIMER_CONFIG['work_time'])
        if work_end > end_time:
            work_end = end_time
        
        print(f"\n🍅 Ciclo {cycle_count}:")
        print(f"   🖥️  Trabajo: {current_time.strftime('%H:%M')} - {work_end.strftime('%H:%M')}")
        
        current_time = work_end
        
        # Verificar si hay tiempo para descanso
        if current_time >= end_time:
            break
            
        # Determinar tipo de descanso
        is_long_break = (cycle_count % 4 == 0)
        break_duration = TIMER_CONFIG['long_break_time'] if is_long_break else TIMER_CONFIG['break_time']
        break_type = "LARGO" if is_long_break else "CORTO"
        
        break_end = current_time + timedelta(minutes=break_duration)
        if break_end > end_time:
            break_end = end_time
        
        print(f"   🛋️  Descanso {break_type}: {current_time.strftime('%H:%M')} - {break_end.strftime('%H:%M')}")
        
        current_time = break_end
        cycle_count += 1
        
        # Si el próximo ciclo no cabe, terminar
        if current_time + timedelta(minutes=TIMER_CONFIG['work_time']) > end_time:
            break
    
    # Calcular descanso largo final si quedan ciclos
    remaining_cycles = TIMER_CONFIG['total_cycles'] - (cycle_count - 1)
    if remaining_cycles > 0 and current_time < end_time:
        print(f"\n🏁 Descanso largo final (+{remaining_cycles} ciclos pendientes)")
        final_break_end = min(current_time + timedelta(minutes=TIMER_CONFIG['long_break_time']), end_time)
        print(f"   🎉 Descanso largo: {current_time.strftime('%H:%M')} - {final_break_end.strftime('%H:%M')}")
    
    print(f"\n💡 Total de ciclos posibles en horario laboral: {cycle_count - 1}")
    input("\nPresiona Enter para volver...")

def show_schedule_menu():
    """Menú para configurar y ver la jornada laboral."""
    while True:
        print("\n========================================")
        print("   CONFIGURAR JORNADA LABORAL          ")
        print("========================================")
        print(" 1) 3 horas  (09:00 - 12:00)")
        print(" 2) 5 horas  (09:00 - 14:00) ← Actual")
        print(" 3) 8 horas  (09:00 - 17:00)")
        print(" 4) Ver horarios detallados")
        print(" 5) Volver")
        print("----------------------------------------")
        
        choice = input("Selecciona una opción: ").strip()
        
        if choice == '1':
            WORK_SCHEDULE['hours'] = 3
            WORK_SCHEDULE['start_hour'] = 9
            WORK_SCHEDULE['label'] = '3 horas (09:00 - 12:00)'
            print("\n✅ Jornada laboral configurada: 3 horas (09:00 - 12:00)")
            time.sleep(1)
        elif choice == '2':
            WORK_SCHEDULE['hours'] = 5
            WORK_SCHEDULE['start_hour'] = 9
            WORK_SCHEDULE['label'] = '5 horas (09:00 - 14:00)'
            print("\n✅ Jornada laboral configurada: 5 horas (09:00 - 14:00)")
            time.sleep(1)
        elif choice == '3':
            WORK_SCHEDULE['hours'] = 8
            WORK_SCHEDULE['start_hour'] = 9
            WORK_SCHEDULE['label'] = '8 horas (09:00 - 17:00)'
            print("\n✅ Jornada laboral configurada: 8 horas (09:00 - 17:00)")
            time.sleep(1)
        elif choice == '4':
            print(f"\n📊 Horarios detallados para jornada de {WORK_SCHEDULE['hours']} horas...")
            time.sleep(1)
            show_schedule(hours=WORK_SCHEDULE['hours'], start_hour=WORK_SCHEDULE['start_hour'])
        elif choice == '5':
            break
        else:
            print("Opción no válida.")
            time.sleep(1)

def show_session_config():
    """Muestra un resumen de la configuración antes de iniciar la sesión."""
    print("\n" + "="*60)
    print("📋 RESUMEN DE CONFIGURACIÓN - SESIÓN POMODORO")
    print("="*60)
    print(f"\n⏱️  TIEMPOS CONFIGURADOS:")
    print(f"   🖥️  Tiempo de trabajo: {TIMER_CONFIG['work_time']} minutos")
    print(f"   🛋️  Descanso corto: {TIMER_CONFIG['break_time']} minutos")
    print(f"   🛋️  Descanso largo: {TIMER_CONFIG['long_break_time']} minutos")
    print(f"   🔄 Ciclos a realizar: {TIMER_CONFIG['total_cycles']}")
    
    print(f"\n📅 JORNADA LABORAL CONFIGURADA:")
    print(f"   ⏰ {WORK_SCHEDULE['label']}")
    print(f"   🍅 Ciclos posibles en jornada: {calculate_max_cycles()}")
    
    print("\n" + "="*60)
    print("✅ Presiona Enter para iniciarpara iniciar tu sesión...")
    print("=" * 60 + "\n")
    input()

def calculate_max_cycles():
    """Calcula el máximo de ciclos que caben en la jornada laboral."""
    start_time = datetime.strptime(f"{WORK_SCHEDULE['start_hour']:02d}:00", "%H:%M")
    end_time = datetime.strptime(f"{WORK_SCHEDULE['start_hour'] + WORK_SCHEDULE['hours']:02d}:00", "%H:%M")
    
    current_time = start_time
    cycle_count = 0
    
    while current_time < end_time:
        # Tiempo de trabajo
        work_end = current_time + timedelta(minutes=TIMER_CONFIG['work_time'])
        if work_end > end_time:
            break
        
        cycle_count += 1
        current_time = work_end
        
        # Si hay descanso después
        is_long_break = (cycle_count % 4 == 0)
        break_duration = TIMER_CONFIG['long_break_time'] if is_long_break else TIMER_CONFIG['break_time']
        break_end = current_time + timedelta(minutes=break_duration)
        
        if break_end <= end_time:
            current_time = break_end
    
    return cycle_count

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
        print(" 3) Configurar Jornada Laboral")
        print("    (Actual: " + WORK_SCHEDULE['label'] + ")")
        print(" 4) Salir")
        print("----------------------------------------")
        
        choice = input("Selecciona una opción: ").strip()

        if choice == '1':
            show_session_config()
            timer_app.exit_event.clear()
            timer_app.pause_event.clear()
            timer_app.run_session()
        elif choice == '2':
            configure()
        elif choice == '3':
            show_schedule_menu()
        elif choice == '4':
            print("¡Hasta pronto!")
            sys.exit(0)
        else:
            print("Opción no válida.")
            time.sleep(1)
