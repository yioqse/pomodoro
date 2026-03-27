# Temporizador Pomodoro Interactivo

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-Pytest-blueviolet?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue?style=flat-square)

Este proyecto consiste en desarrollar un temporizador Pomodoro interactivo que permita a los usuarios gestionar su tiempo de trabajo y descanso usando la técnica Pomodoro (25 minutos de trabajo / 5 minutos de descanso). El desarrollo se realizará paso a paso utilizando Git para control de versiones y contando con la asistencia de herramientas de IA para generar código, el cual deberá ser analizado, comprendido y modificado según las necesidades del proyecto.

## Objetivos de Aprendizaje

- Practicar el uso de Git con commits incrementales.
- Aprender a interactuar con IA para generar código.
- Desarrollar habilidades de revisión y modificación de código generado.
- Documentar el proceso de asistencia de IA.
- Comprender la lógica del manejo del tiempo y bucles en Python.
- Implementar notificaciones y sonidos desde terminal.

## Estructura del Proyecto

```
pomodoro-timer/
|
|-- README.md
|-- .gitignore
|-- requirements.txt
|-- src/
|   |-- pomodoro.py
|   |-- config.py
|   |-- notificaciones.py
|-- docs/
|   |-- asistencia_ia.md
|-- tests/
```

## Instalación

1. Clona el repositorio.
2. Instala las dependencias: `pip install -r requirements.txt`
3. Ejecuta el temporizador: `python src/pomodoro.py`

## Uso

Ejecuta el script principal para iniciar el temporizador Pomodoro. Al iniciar, se te pedirá configurar los tiempos de trabajo y descanso (con valores por defecto de 25 minutos de trabajo y 5 minutos de descanso), y el número de ciclos a completar (por defecto 4). Los valores deben ser números positivos.

El temporizador cuenta los ciclos completados y muestra estadísticas al final de cada uno. Cada 4 ciclos, se realiza un descanso largo de 15 minutos en lugar del descanso corto. Al completar todos los ciclos, muestra un resumen final con un beep sonoro.

Además, el temporizador permite pausar/reanudar en cualquier momento con la tecla 'p' y salir con la tecla 'q'. El estado actual (corriendo/pausado) se muestra en pantalla.

Fase 8: Interfaz de terminal
- Al iniciar se muestra un menú interactivo con opciones de configurar sesión, iniciar y salir.
- Se muestra una barra de progreso visual durante cada cuenta regresiva.
- La pantalla se limpia entre menús y para mejorar la visualización.

## Documentación de uso avanzada

Se agregó un documento de referencia en `docs/documentacion_asistencia_ia.md` que incluye ejemplos de uso directo y pasos para ejecutar con configuración rápida.

Las notificaciones incluyen mensajes destacados en color y sonidos beep compatibles con Windows, Linux y macOS.

## Pruebas (Tests)

El proyecto incluye una suite completa de pruebas automatizadas (unitarias y de integración) desarrolladas con `pytest`. 
Para ejecutar todas las pruebas, asegúrate de haber instalado las dependencias (incluido pytest) y ejecuta el siguiente comando en la raíz del proyecto:

```bash
pytest tests/
```
