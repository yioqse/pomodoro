# 🍅 Temporizador Pomodoro Interactivo

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Tests](https://img.shields.io/badge/Tests-Pytest-blueviolet?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue?style=for-the-badge)
![Code Style](https://img.shields.io/badge/Code%20Style-Professional-informational?style=for-the-badge)

**Un temporizador Pomodoro moderno, interactivo y fácil de usar para optimizar tu productividad**

[Demo](#uso) • [Instalación](#instalación) • [Características](#-características) • [Documentación](#documentación)

</div>

---

Este proyecto consiste en desarrollar un temporizador Pomodoro interactivo que permita a los usuarios gestionar su tiempo de trabajo y descanso usando la técnica Pomodoro (25 minutos de trabajo / 5 minutos de descanso). El desarrollo se realizará paso a paso utilizando Git para control de versiones y contando con la asistencia de herramientas de IA para generar código, el cual deberá ser analizado, comprendido y modificado según las necesidades del proyecto.

## 📋 Tabla de Contenidos

- [✨ Características](#-características)
- [🎯 Objetivos de Aprendizaje](#-objetivos-de-aprendizaje)
- [📦 Estructura del Proyecto](#-estructura-del-proyecto)
- [📥 Instalación](#-instalación)
- [🚀 Uso](#-uso)
- [🆕 Nuevas Funcionalidades CLI](#-nuevas-funcionalidades-cli)
- [🔧 Solución de Problemas](#-solución-de-problemas)
- [🧪 Pruebas](#-pruebas)
- [📚 Documentación](#-documentación)
- [🤝 Contribución](#-contribución)
- [📝 Licencia](#-licencia)

## ✨ Características

- ⏱️ **Temporizador Pomodoro Configurables** - Personaliza tiempos de trabajo y descanso
- 🔔 **Notificaciones Inteligentes** - Alertas con sonido y color en terminal
- ⏸️ **Controles Interactivos** - Pausa, reanuda y salta ciclos con facilidad
- 📊 **Estadísticas en Tiempo Real** - Monitorea tu progreso con barra visual
- 🎨 **Interfaz de Terminal Amigable** - Menú interactivo y visualización clara
- 🖼️ **Interfaz Gráfica (GUI)** - Aplicación visual completa con Tkinter
- ⏳ **Descansos Progresivos** - Descanso largo cada 4 ciclos + descanso largo final
- 📈 **Sistema de Logging Completo** - Registra ciclos, pausas y estadísticas en JSON
- 📅 **Planificación de Horarios** - Calcula descansos para horario laboral (9 AM - 2 PM)
- 🛡️ **Totalmente Probado** - Suite completa de tests con pytest
- 🌐 **Multiplataforma** - Compatible con Windows, Linux y macOS

## 🎯 Objetivos de Aprendizaje

- Practicar el uso de Git con commits incrementales.
- Aprender a interactuar con IA para generar código.
- Desarrollar habilidades de revisión y modificación de código generado.
- Documentar el proceso de asistencia de IA.
- Comprender la lógica del manejo del tiempo y bucles en Python.
- Implementar notificaciones y sonidos desde terminal.

## 📦 Estructura del Proyecto

```
pomodoro/
├── main.py                                # ⭐ Punto de entrada (RECOMENDADO)
├── gui_launcher.py                        # 🖼️ Lanzador de GUI
├── README.md                              # Este archivo
├── LICENSE                                # Licencia MIT
├── pyrightconfig.json                     # Configuración de Pyright
├── requirements.txt                       # Dependencias del proyecto
├──
├── src/                                   # Código fuente principal
│   ├── pomodoro.py                        # Script principal de terminal
│   ├── config/                            # Gestión de configuración
│   │   ├── __init__.py
│   │   └── manager.py                     # Gestor de configuración
│   ├── modules/                           # Módulos funcionales
│   │   ├── __init__.py
│   │   ├── menu.py                        # Interfaz de menú
│   │   └── timer.py                       # Lógica del temporizador
│   └── notificaciones/                    # Sistema de notificaciones
│       ├── __init__.py
│       └── notifier.py                    # Gestor de notificaciones
│
├── GUI/                                   # 🖼️ INTERFAZ GRÁFICA (NUEVO)
│   ├── __init__.py
│   ├── styles.py                          # Temas, colores y fuentes
│   ├── widgets.py                         # Componentes personalizados
│   ├── main_gui.py                        # Aplicación GUI principal
│   ├── README.md                          # Documentación de GUI
│   └── requirements_gui.txt               # Dependencias de GUI
│
├── docs/                                  # Documentación
│   ├── asistencia_ia.md                   # Notas sobre asistencia IA
│   ├── documentacion_asistencia_ia.md     # Documentación completa
│   └── doc_proyecto.md                    # Documentación técnica
│
└── tests/                                 # Suite de pruebas
    ├── conftest.py                        # Configuración de pytest
    ├── test_config.py                     # Tests de configuración
    ├── test_timer.py                      # Tests del temporizador
    ├── test_notifier.py                   # Tests de notificaciones
    └── test_integration.py                # Tests de integración
```

## 📥 Instalación

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (para clonar el repositorio)

### Pasos de Instalación

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/yioqse/pomodoro.git
   cd pomodoro
   ```

2. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verifica la instalación**
   ```bash
   # Opción 1: Desde la raíz (RECOMENDADO)
   python main.py
   
   # Opción 2: Desde src
   python src/pomodoro.py
   ```

### Instalación en Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
# En Windows:
venv\Scripts\activate
# En Linux/macOS:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## 🚀 Uso

### Punto de Entrada Unificado (RECOMENDADO)

Ejecuta `main.py` desde la raíz del proyecto para acceder a ambas interfaces:

```bash
# Menú interactivo (elige entre CLI y GUI)
python main.py

# Versión Terminal directamente
python main.py cli
python main.py terminal
python main.py 1

# Versión GUI directamente
python main.py gui
python main.py graphical
python main.py 2
```

### Versiones Específicas

#### Versión Terminal (CLI)

```bash
# Desde el directorio src
python src/pomodoro.py
```

#### Versión GUI (Interfaz Gráfica con Tkinter)

```bash
# Desde el directorio GUI
python GUI/main_gui.py
```

**Nota:** Para la GUI en Linux, puede requerir instalación de tkinter:
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter
```

### 🔧 Solución de Problemas

#### Diagnóstico Automático

Ejecuta el script de diagnóstico para identificar problemas automáticamente:

```bash
python diagnose.py
```

Este script verificará:
- ✅ Versión de Python compatible
- ✅ Archivos del proyecto presentes
- ✅ Tkinter y Tcl/Tk funcionando
- ✅ Dependencias instaladas

#### Error: "Can't find a usable init.tcl" o "Tcl wasn't installed properly"

Este error ocurre cuando Tcl/Tk no está instalado correctamente en Windows. Para solucionarlo:

**Opción 1: Reinstalar Python (Recomendado)**
1. Ve a https://python.org
2. Descarga la versión más reciente de Python
3. **Importante:** Durante la instalación, marca la opción "Add Python to PATH" y "Install launcher for all users"
4. Selecciona "Customize installation" y asegúrate de que "tcl/tk and IDLE" esté marcado
5. Reinicia tu computadora después de la instalación

**Opción 2: Instalar ActiveTcl**
1. Ve a https://www.activestate.com/products/tcl/
2. Descarga e instala ActiveTcl
3. Reinicia tu computadora

Después de cualquiera de estas opciones, ejecuta:
```bash
python main.py gui
```

#### Error: "tkinter no está disponible"

Si tkinter no se puede importar, instala los paquetes necesarios:

**Windows:**
- Viene preinstalado con Python completo
- Si no funciona, reinstala Python

**macOS:**
```bash
brew install python-tk
```

**Linux:**
```bash
# Ubuntu/Debian
sudo apt-get install python3-tk

# Fedora
sudo dnf install python3-tkinter

# Arch Linux
sudo pacman -S tk
```
```

### Terminal - Menú Interactivo

Al iniciar la versión terminal, se mostrará un menú interactivo con las siguientes opciones:
- **Iniciar sesión** - Comienza el temporizador con la configuración actual
- **Configurar tiempos** - Personaliza tiempos de trabajo, descanso y ciclos
- **Ver horarios de jornada laboral** - Calcula y muestra el calendario de descansos (NUEVA OPCIÓN MEJORADA)
- **Salir** - Cierra la aplicación

#### 🆕 Nuevas Funcionalidades CLI

**1. Descanso Largo Final**
- Después de completar todos los ciclos marcados, se ejecuta automáticamente un descanso largo final
- Mensaje de felicitación y motivación

**2. Sistema de Logging Avanzado**
- Registra automáticamente cada sesión en archivos JSON en la carpeta `logs/`
- Información detallada incluye:
  - Ciclos completados y timestamps
  - Número de pausas durante trabajo y descanso
  - Tiempo total pausado en cada fase
  - Duración total de la sesión

**3. Planificación de Horarios Laborales**
- Calcula automáticamente los horarios de descanso para un turno de 9:00 AM a 2:00 PM
- Muestra qué ciclos tienen descanso corto (5 min) y cuáles descanso largo (15 min)
- Ayuda a planificar el día laboral con la técnica Pomodoro

### GUI - Interfaz Gráfica

La versión GUI incluye:
- **Pantalla Principal** - Inicio rápido de sesión, configuración y estadísticas
- **Configuración Visual** - Campos para personalizar tiempos fácilmente
- **Sesión Activa** - Display grande, barra de progreso circular, botones de control
- **Estadísticas** - Resumen de ciclos completados y tiempo estimado
- **Tema Oscuro** - Interfaz moderna y de bajo consumo visual

## 🆕 Nuevas Funcionalidades CLI

### 1. 🏁 Descanso Largo Final
Después de completar todos los ciclos marcados, el temporizador ejecuta automáticamente un **descanso largo final** como recompensa. Este descanso extra motiva la finalización de todos los ciclos planificados.

**Características:**
- Se ejecuta solo al completar 100% de los ciclos
- Duración configurable (por defecto 15 minutos)
- Mensaje de felicitación personalizado

### 2. 📊 Sistema de Logging Avanzado
Cada sesión se registra automáticamente en archivos JSON con información detallada para análisis posterior.

**Información registrada:**
- **Sesión**: Timestamp de inicio/fin, duración total
- **Ciclos**: Detalle de cada ciclo completado con timestamps
- **Pausas**: Número de pausas y tiempo total pausado (trabajo vs descanso)
- **Estadísticas**: Ciclos completados, tipos de descanso utilizados

**Ubicación:** Archivos se guardan en `logs/pomodoro_session_YYYYMMDD_HHMMSS.json`

### 3. 📅 Planificación de Horarios Laborales (MEJORADO)
Función integrada para calcular automáticamente los horarios de descanso con **3 opciones de jornada laboral**.

**Jornadas disponibles:**
- **3 horas**: 09:00 - 12:00 → **5 ciclos** posibles
- **5 horas**: 09:00 - 14:00 → **9 ciclos** posibles  
- **8 horas**: 09:00 - 17:00 → **15 ciclos** posibles

**Cálculos automáticos por jornada:**
- **Descanso corto** (5 min): Después de ciclos 1,2,3,5,6,7,9,10,11,13,14 (no múltiplos de 4)
- **Descanso largo** (15 min): Después de ciclos 4,8,12 (cada 4 ciclos)

**Ejemplos de cálculos:**

*Jornada de 3 horas:*
```
09:00-09:25 🖥️  Trabajo + 09:25-09:30 🛋️  Descanso CORTO
09:30-09:55 🖥️  Trabajo + 09:55-10:00 🛋️  Descanso CORTO  
10:00-10:25 🖥️  Trabajo + 10:25-10:30 🛋️  Descanso CORTO
10:30-10:55 🖥️  Trabajo + 10:55-11:10 🛋️  Descanso LARGO (15min)
11:10-11:35 🖥️  Trabajo + 11:35-11:40 🛋️  Descanso CORTO
Total: 5 ciclos
```

*Jornada de 8 horas:*
```
09:00-09:25 🖥️  Trabajo + 09:25-09:30 🛋️  Descanso CORTO
[...ciclos 2-3...]
10:30-10:55 🖥️  Trabajo + 10:55-11:10 🛋️  Descanso LARGO
[...ciclos 5-7...]
12:40-13:05 🖥️  Trabajo + 13:05-13:20 🛋️  Descanso LARGO
[...ciclos 9-11...]
14:50-15:15 🖥️  Trabajo + 15:15-15:30 🛋️  Descanso LARGO
[...hasta las 17:00]
Total: 15 ciclos
```

### Valores por Defecto

- ⏱️ Trabajo: 25 minutos
- ☕ Descanso corto: 5 minutos  
- 🏖️ Descanso largo: 15 minutos (cada 4 ciclos)
- 🔄 Ciclos: 4

### Controles Durante la Sesión

| Tecla | Acción |
|-------|--------|
| `p`   | Pausa/Reanuda el temporizador |
| `q`   | Salir de la sesión actual |

### Ejemplo de Ejecución

```
┌─────────────────────────────────┐
│   🍅 TEMPORIZADOR POMODORO     │
└─────────────────────────────────┘

Menú Principal:
1. Configurar sesión
2. Iniciar
3. Salir

Selecciona una opción: 2

Iniciando sesión Pomodoro...
Ciclo 1/4 - Tiempo de trabajo

⏱️  00:24:55
████████████████░░░░░░░░░░░░░░░░  49%

Estado: Corriendo | [P]ausa | [Q]uit
```

## 🧪 Pruebas

El proyecto incluye una suite completa de pruebas automatizadas desarrolladas con `pytest`.

### Ejecutar Todas las Pruebas

```bash
pytest tests/
```

### Ejecutar Pruebas Específicas

```bash
# Tests del configurador
pytest tests/test_config.py -v

# Tests del temporizador
pytest tests/test_timer.py -v

# Tests de notificaciones
pytest tests/test_notifier.py -v

# Tests de integración
pytest tests/test_integration.py -v
```

### Ver Cobertura de Código

```bash
pytest tests/ --cov=src --cov-report=html
```

## 📚 Documentación

### Documentos Principales

- **[Asistencia IA](docs/asistencia_ia.md)** - Notas sobre el desarrollo con IA
- **[Documentación Completa](docs/documentacion_asistencia_ia.md)** - Guía de uso avanzada y ejemplos
- **[Documentación Técnica](docs/doc_proyecto.md)** - Análisis exhaustivo de arquitectura
- **[GUI README](GUI/README.md)** - Guía completa de la interfaz gráfica

### Características por Interfaz

**Terminal (Fase 8):**
- Menú interactivo con opciones de configuración
- Barra de progreso visual durante la sesión
- Visualización clara del estado actual
- Limpieza automática de pantalla entre etapas
- Mensajes destacados en color

**GUI Gráfica (NUEVO):**
- 🖼️ Interfaz moderna con tema oscuro
- ⏱️ Display digital grande con formato MM:SS
- 📊 Barra de progreso circular visual
- 🎨 Componentes personalizados (buttons, labels, etc)
- ⚙️ Configuración intuitiva con formulario
- 📈 Estadísticas en tiempo real

### Sistema de Notificaciones

Las notificaciones incluyen:
- 🔔 Mensajes destacados en color (ambas interfaces)
- 🔊 Sonidos beep compatibles con Windows, Linux y macOS
- ⏰ Alertas en momentos clave (inicio/fin de ciclo)

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para contribuir:

1. Fork el repositorio
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

### Estándares de Código

- Sigue PEP 8 para el estilo de código
- Incluye tests para nuevas características
- Actualiza la documentación según sea necesario
- Asegúrate de que todos los tests pasen

## 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

## 👨‍💻 Autor

Proyecto desarrollado como parte de un aprendizaje práctico en Python y Git.

---

<div align="center">

**[⬆ Volver al inicio](#-temporizador-pomodoro-interactivo)**

¡Hecho con ❤️ para mejorar tu productividad!

</div>
