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
- 🔄 **Descansos Extendidos** - Descanso largo (15 min) cada 4 ciclos
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
├── README.md                              # Este archivo
├── LICENSE                                # Licencia MIT
├── pyrightconfig.json                     # Configuración de Pyright
├── requirements.txt                       # Dependencias del proyecto
├──
├── src/                                   # Código fuente principal
│   ├── pomodoro.py                        # Script principal
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
├── docs/                                  # Documentación
│   ├── asistencia_ia.md                   # Notas sobre asistencia IA
│   └── documentacion_asistencia_ia.md     # Documentación completa
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

### Inicio Rápido

Ejecuta el script principal para iniciar el temporizador:

```bash
python src/pomodoro.py
```

### Menú Interactivo

Al iniciar, se mostrará un menú interactivo con las siguientes opciones:
- **Configurar sesión** - Personaliza tiempos de trabajo, descanso y número de ciclos
- **Iniciar** - Comienza el temporizador con la configuración actual
- **Salir** - Cierra la aplicación

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

### Características por Fase

**Fase 8: Interfaz de Terminal**
- Menú interactivo con opciones de configuración
- Barra de progreso visual durante la sesión
- Visualización clara del estado actual
- Limpieza automática de pantalla entre etapas
- Mensajes destacados en color

### Sistema de Notificaciones

Las notificaciones incluyen:
- 🔔 Mensajes destacados en color
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
