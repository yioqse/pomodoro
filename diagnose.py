#!/usr/bin/env python3
"""
🍅 Diagnóstico del Temporizador Pomodoro
Verifica el estado de la instalación y componentes necesarios
"""

import sys
import os
import platform

def check_python_version():
    """Verifica la versión de Python."""
    version = sys.version_info
    print(f"🐍 Python {version.major}.{version.minor}.{version.micro}")
    if version >= (3, 8):
        print("   ✅ Versión compatible")
        return True
    else:
        print("   ❌ Requiere Python 3.8 o superior")
        return False

def check_tkinter():
    """Verifica si tkinter está disponible y funcional."""
    try:
        import tkinter
        print("📦 Tkinter importado correctamente")

        # Intentar crear una ventana para verificar Tcl/Tk
        try:
            root = tkinter.Tk()
            root.withdraw()
            root.destroy()
            print("   ✅ Tcl/Tk funcional")
            return True
        except Exception as e:
            print(f"   ❌ Tcl/Tk no funciona: {e}")
            return False
    except ImportError:
        print("   ❌ Tkinter no instalado")
        return False

def check_project_files():
    """Verifica que los archivos del proyecto estén presentes."""
    required_files = [
        'main.py',
        'src/pomodoro.py',
        'src/modules/menu.py',
        'GUI/main_gui.py',
        'requirements.txt'
    ]

    missing = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing.append(file_path)

    if missing:
        print("📁 Archivos faltantes:")
        for file in missing:
            print(f"   ❌ {file}")
        return False
    else:
        print("📁 Todos los archivos del proyecto presentes")
        return True

def check_dependencies():
    """Verifica las dependencias del proyecto."""
    try:
        with open('requirements.txt', 'r') as f:
            requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print("⚠️  requirements.txt no encontrado")
        return False

    print("📦 Verificando dependencias...")
    missing_deps = []

    for req in requirements:
        # Extraer nombre del paquete (antes de ==, >=, etc.)
        package_name = req.split()[0].split('==')[0].split('>=')[0].split('>')[0].split('<')[0]

        try:
            __import__(package_name.replace('-', '_'))
            print(f"   ✅ {package_name}")
        except ImportError:
            print(f"   ❌ {package_name}")
            missing_deps.append(package_name)

    return len(missing_deps) == 0

def main():
    """Función principal de diagnóstico."""
    print("🍅 DIAGNÓSTICO - TEMPORIZADOR POMODORO")
    print("=" * 50)
    print()

    system = platform.system()
    print(f"🖥️  Sistema operativo: {system}")
    print()

    checks = []
    checks.append(("Versión de Python", check_python_version()))
    checks.append(("Archivos del proyecto", check_project_files()))
    checks.append(("Tkinter/GUI", check_tkinter()))
    checks.append(("Dependencias", check_dependencies()))

    print()
    print("📊 RESULTADOS:")
    all_passed = True
    for name, passed in checks:
        status = "✅" if passed else "❌"
        print(f"   {status} {name}")
        if not passed:
            all_passed = False

    print()
    if all_passed:
        print("🎉 ¡Todo está listo! Puedes ejecutar:")
        print("   python main.py")
    else:
        print("❌ Hay problemas que necesitan solución:")
        print()
        print("🔧 SOLUCIONES RECOMENDADAS:")
        print()

        if not checks[0][1]:  # Python version
            print("🐍 ACTUALIZAR PYTHON:")
            print("   1. Ve a https://python.org")
            print("   2. Descarga Python 3.8+")
            print("   3. Marca 'Add to PATH' durante instalación")
            print()

        if not checks[2][1]:  # Tkinter
            print("🖼️  REPARAR TKINTER/TCL:")
            if system == "Windows":
                print("   Opción 1 (Recomendada):")
                print("   1. Reinstala Python desde https://python.org")
                print("   2. Asegúrate de marcar 'tcl/tk and IDLE'")
                print("   3. Reinicia la computadora")
                print()
                print("   Opción 2:")
                print("   1. Instala ActiveTcl: https://www.activestate.com/products/tcl/")
                print("   2. Reinicia la computadora")
            else:
                print(f"   Para {system}:")
                if "Ubuntu" in platform.version() or "Debian" in platform.version():
                    print("   sudo apt-get install python3-tk")
                elif "Fedora" in platform.version():
                    print("   sudo dnf install python3-tkinter")
                else:
                    print("   Instala python3-tk para tu distribución")
            print()

        if not checks[1][1]:  # Project files
            print("📁 ARCHIVOS DEL PROYECTO:")
            print("   Asegúrate de que todos los archivos estén en el directorio correcto")
            print()

        if not checks[3][1]:  # Dependencies
            print("📦 DEPENDENCIAS:")
            print("   Instala las dependencias con:")
            print("   pip install -r requirements.txt")
            print()

if __name__ == '__main__':
    main()