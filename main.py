#!/usr/bin/env python3
"""
🍅 Temporizador Pomodoro Interactivo
Punto de entrada desde la raíz del proyecto

Uso:
    python main.py                    # Menú interactivo
    python main.py cli                # Versión terminal
    python main.py gui                # Versión gráfica
    python main.py terminal           # Alias para cli
    python main.py graphical          # Alias para gui
    python main.py 1                  # Número para cli
    python main.py 2                  # Número para gui
    
Este script sirve como punto de entrada alternativo que permite
ejecutar la aplicación Pomodoro desde la raíz del proyecto.
"""

import sys
import os

# Agregar src al path para importar módulos
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def check_tkinter_available():
    """Verifica si tkinter está disponible y funcional."""
    try:
        import tkinter
        # Intentar crear una ventana mínima para verificar que Tcl/Tk funciona
        root = tkinter.Tk()
        root.withdraw()  # Ocultar la ventana
        root.destroy()   # Destruir inmediatamente
        return True
    except ImportError:
        return False
    except Exception as e:
        # tkinter se importa pero Tcl/Tk no funciona
        return False

def show_main_menu():
    """Muestra el menú principal para elegir entre CLI y GUI."""
    # Verificar si tkinter está disponible
    tkinter_available = check_tkinter_available()
    
    # Verificar si hay argumentos de línea de comandos
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower().strip()
        if arg in ['cli', 'terminal', '1']:
            return 'cli'
        elif arg in ['gui', 'graphical', '2']:
            if not tkinter_available:
                print("❌ Error: Tkinter no está disponible o no funciona correctamente.")
                print("Para usar la GUI, instala o repara Tcl/Tk:")
                print("  - Windows: Reinstala Python desde python.org")
                print("  - O instala ActiveTcl desde https://www.activestate.com/products/tcl/")
                sys.exit(1)
            return 'gui'
        else:
            print(f"❌ Argumento inválido: {arg}")
            print("Uso: python main.py [cli|gui|terminal|graphical|1|2]")
            sys.exit(1)
    
    # Verificar si hay entrada piped (no interactiva)
    if not sys.stdin.isatty():
        print("⚠️  Modo no interactivo detectado. Usando CLI por defecto.")
        return 'cli'
    
    # Modo interactivo
    while True:
        # Limpiar pantalla solo en modo interactivo
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print("🍅 TEMPORIZADOR POMODORO INTERACTIVO")
        print("=" * 50)
        print()
        print("Selecciona la interfaz que deseas usar:")
        print()
        print("1. 🖥️  Terminal (CLI) - Interfaz de texto")
        if tkinter_available:
            print("2. 🖼️  GUI - Interfaz gráfica (Tkinter)")
        else:
            print("2. 🖼️  GUI - Interfaz gráfica (NO DISPONIBLE)")
        print("3. ❌ Salir")
        print()
        
        try:
            choice = input("Elige una opción (1-3): ").strip()
            
            if choice == '1':
                # Lanzar versión CLI
                print("\n🚀 Iniciando versión Terminal...")
                return 'cli'
            elif choice == '2':
                # Verificar si tkinter está disponible
                if not tkinter_available:
                    print("\n❌ Error: Tkinter no está disponible o no funciona correctamente.")
                    print("Para usar la GUI, instala o repara Tcl/Tk:")
                    print("  - Windows: Reinstala Python desde https://python.org")
                    print("  - O instala ActiveTcl desde https://www.activestate.com/products/tcl/")
                    print()
                    input("Presiona Enter para continuar...")
                    continue
                print("\n🚀 Iniciando versión GUI...")
                return 'gui'
            elif choice == '3':
                print("\n👋 ¡Hasta luego!")
                sys.exit(0)
            else:
                print("\n❌ Opción inválida. Elige 1, 2 o 3.")
                input("Presiona Enter para continuar...")
                continue
                
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            sys.exit(0)
        except EOFError:
            # Manejar caso donde no hay input disponible (ej: redirección)
            print("\n❌ No se puede mostrar el menú interactivo.")
            print("Usando versión CLI por defecto...")
            return 'cli'

def launch_cli():
    """Lanza la versión CLI."""
    try:
        from modules.menu import main_menu
        main_menu()
    except Exception as e:
        print(f"\n❌ Error en CLI: {e}")
        sys.exit(1)

def launch_gui():
    """Lanza la versión GUI."""
    try:
        # Verificar tkinter antes de intentar importar
        if not check_tkinter_available():
            print("\n❌ Error: Tkinter no está disponible o Tcl/Tk no funciona correctamente.")
            print("Para solucionar este problema:")
            print("  1. Reinstala Python desde https://python.org (elige la versión completa)")
            print("  2. O instala ActiveTcl desde https://www.activestate.com/products/tcl/")
            print("  3. Reinicia tu computadora después de la instalación")
            print()
            print("Después de instalar, ejecuta: python main.py gui")
            sys.exit(1)
        
        # Agregar GUI al path
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'GUI'))
        
        from GUI.main_gui import main
        
        # Ejecutar GUI
        main()
        
    except ImportError as e:
        print(f"\n❌ Error al importar GUI: {e}")
        print("Asegúrate de que todos los archivos de GUI estén presentes.")
        sys.exit(1)
    except Exception as e:
        error_msg = str(e).lower()
        if 'tcl' in error_msg or 'tk' in error_msg or 'init.tcl' in error_msg:
            print("\n❌ Error de Tcl/Tk: Los componentes gráficos no están instalados correctamente.")
            print("Para solucionar este problema:")
            print("  1. Reinstala Python desde https://python.org (elige la versión completa)")
            print("  2. O instala ActiveTcl desde https://www.activestate.com/products/tcl/")
            print("  3. Reinicia tu computadora después de la instalación")
            print()
            print("Después de instalar, ejecuta: python main.py gui")
        else:
            print(f"\n❌ Error en GUI: {e}")
        sys.exit(1)

def main():
    """Función principal."""
    try:
        # Mostrar menú de selección
        choice = show_main_menu()
        
        # Lanzar la interfaz seleccionada
        if choice == 'cli':
            launch_cli()
        elif choice == 'gui':
            launch_gui()
            
    except KeyboardInterrupt:
        print("\n\n👋 ¡Hasta luego!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error inesperado: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
