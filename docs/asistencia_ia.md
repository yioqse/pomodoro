# Asistencia de IA

Este documento registra el proceso de asistencia de herramientas de IA durante el desarrollo del proyecto Temporizador Pomodoro.

## Sesiones de Asistencia

### Sesión 1: Generación Inicial del Código
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Generación del README.md
  - Configuración de .gitignore
  - Creación de requirements.txt
  - Desarrollo de módulos: config.py, notificaciones.py, pomodoro.py
- Modificaciones realizadas: Agregados comentarios explicativos en el código.

### Sesión 2: Fase 4 - Configuración Personalizable
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Modificación de config.py para incluir configuración interactiva con validación de valores positivos.
  - Actualización de pomodoro.py para llamar a la configuración al inicio.
  - Actualización del README.md y asistencia_ia.md con la nueva fase.
- Preguntas para la IA:
  - "¿Cómo creo un archivo de configuración en Python con variables globales?"
  - "¿Cómo valido que un número sea positivo y mayor que cero?"
- Respuestas de la IA:
  - Para crear un archivo de configuración con variables globales: Define las variables en un módulo separado (como config.py). Usa `global` dentro de funciones si necesitas modificarlas. Importa las variables en otros módulos con `from config import VARIABLE`.
  - Para validar un número positivo y mayor que cero: Usa un bucle `while True` con `try-except` para convertir a `float`. Verifica `if value > 0`, y repite la solicitud si no es válido.
- Modificaciones realizadas: Agregada función configure() con input validado, y llamada en el main.

### Commit: Fix configuration update issue
- Problema identificado: La configuración se actualizaba correctamente en config.py, pero el temporizador seguía usando los valores por defecto (25 min trabajo) porque las variables importadas en pomodoro.py no se actualizaban. Esto ocurre porque los floats son inmutables en Python; al reasignar WORK_TIME = nuevo_valor, se crea un nuevo objeto, pero la referencia importada sigue apuntando al original.
- Solución implementada: Cambié WORK_TIME y BREAK_TIME a listas mutables ([DEFAULT_WORK_TIME], [DEFAULT_BREAK_TIME]) en config.py. En la función configure(), modifico WORK_TIME[0] y BREAK_TIME[0] en lugar de reasignar. En pomodoro.py, uso WORK_TIME[0] y BREAK_TIME[0] para acceder a los valores actualizados.
- Archivos modificados: src/config.py (cambio a listas), src/pomodoro.py (acceso con [0]).
- Resultado: Ahora la configuración personalizada (ej. 2 min trabajo) se refleja correctamente en el countdown del temporizador.

### Sesión 3: Fase 5 - Contador de ciclos
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Modificación de pomodoro.py para contar ciclos y mostrar estadísticas al final de cada uno.
  - Implementación de descanso largo cada 4 ciclos usando LONG_BREAK_TIME.
  - Actualización del README.md con la nueva funcionalidad.
- Preguntas para la IA:
  - "¿Cómo cuento iteraciones en un bucle y ejecuto algo cada N repeticiones?"
  - "¿Cómo muestro un resumen de ciclos completados en Python?"
- Respuestas de la IA:
  - Para contar iteraciones y ejecutar cada N: Usa una variable contador que incrementa en cada iteración. Verifica `if contador % N == 0` para ejecutar la acción especial.
  - Para mostrar un resumen: Imprime mensajes con f-strings, como `print(f"Estadísticas: Pomodoros completados: {contador}")` al final de cada ciclo.
- Modificaciones realizadas: Agregado LONG_BREAK_TIME a imports, lógica condicional para descanso largo, y print de estadísticas en run_pomodoro().

### Commit: Add configurable number of cycles
- Mejora implementada: Agregué configuración para el número total de ciclos a completar, cambiando el bucle infinito a finito. Ahora el usuario puede especificar cuántos pomodoros quiere hacer en una sesión.
- Cambios en config.py: Nueva variable TOTAL_CYCLES como lista mutable, y prompt en configure() para pedir el número de ciclos (por defecto 4).
- Cambios en pomodoro.py: Importar TOTAL_CYCLES, cambiar while True a while cycle <= TOTAL_CYCLES[0], agregar resumen final al terminar, y actualizar el main para no usar try-except.
- Actualización en README.md: Mencionar la configuración de ciclos y el resumen final.
- Resultado: La sesión ahora es finita, con resumen al completar los ciclos configurados.

### Sesión 4: Fase 6 - Notificaciones y sonido
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Modificación de notificaciones.py para soporte cross-platform (Windows/Linux/Mac) usando platform.system().
  - Emisión de beep al terminar la sesión completa.
  - Mensajes visuales destacados con ANSI escape codes para color y negrita.
- Preguntas para la IA:
  - "¿Cómo emito un beep sonoro desde Python en distintos sistemas operativos?"
  - "¿Cómo detecto el sistema operativo con Python para usar comandos distintos?"
- Respuestas de la IA:
  - Para emitir beep: Usa winsound.Beep() en Windows; en Linux/Mac, imprime '\a' (carácter de campana) que funciona en la mayoría de terminales.
  - Para detectar OS: Importa el módulo platform y usa platform.system() que devuelve 'Windows', 'Linux', 'Darwin' (Mac), etc., para condicionar el código.
- Modificaciones realizadas: Actualizado play_sound() con detección de OS, show_notification() con colores ANSI, agregado play_final_beep() y llamado en pomodoro.py.

### Sesión 5: Fase 7 - Pausa y reanudación
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Implementación de pausa/reanudar por tecla en pomodoro.py usando subhilo de teclado (p/q).
  - Modificación de countdown() para respetar estado de pausado y detenerse con q/exit.
  - Mostrar estado actual (corriendo/pausado) en la terminal.
- Preguntas para la IA:
  - "¿Cómo capturo pulsaciones de teclado sin bloquear el hilo principal en Python?"
  - "¿Cómo implemento pausa y reanudación en un bucle de tiempo?"
- Respuestas de la IA:
  - Para capturar pulsaciones sin bloquear: utiliza un hilo separado que lea teclas con msvcrt (Windows) o select/sys.stdin (Linux/Mac) y actualice eventos compartidos.
  - Para pausa y reanudación en bucle: usa un Event (pause_event). En cada iteración del bucle, si está set, mantén el estado de pausa y no decrementes el reloj, y vuelve al modo normal cuando se desactive.
- Modificaciones realizadas: added keyboard_listener(), pause_event/exit_event, pause-state en countdown y control en loop principal.

### Sesión 6: Fase 8 - Interfaz de usuario en terminal
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Implementación de menú interactivo principal en pomodoro.py con opciones configurar/sesión/salir.
  - Implementación de barra de progreso en cada countdown mediante draw_progress_bar.
  - Limpieza de pantalla en cada menú con clear_screen() para mejor experiencia.
- Preguntas para la IA:
  - "¿Cómo creo una barra de progreso en terminal con Python?"
  - "¿Cómo limpio la pantalla en terminal en cada actualización del tiempo?"
- Respuestas de la IA:
  - Para barra de progreso: construir string con bloques llenos (█) y vacíos (-) basado en porcentaje; imprimir en la misma línea con '\r'.
  - Para limpiar pantalla: usar `os.system('cls')` en Windows y `os.system('clear')` en Linux/Mac o abstraer con una función `clear_screen()`.
- Modificaciones realizadas: Agregado clear_screen(), show_menu(), draw_progress_bar(), ajuste de flujo en __main__ para iniciar desde el menú.

### Sesión 7: Fase 9 - Documentación
- Fecha: [Fecha actual]
- IA utilizada: GitHub Copilot / Grok
- Tareas realizadas:
  - Agregado docstrings a todas las funciones principales en src/pomodoro.py, src/config.py y src/notificaciones.py.
  - Creación de nuevo documento de referencia detallada: docs/documentacion_asistencia_ia.md.
  - Documentación de uso con ejemplos de configuración y ejecución.
- Preguntas para la IA:
  - "¿Cómo creo una barra de progreso en terminal con Python?"
  - "¿Cómo limpio la pantalla en terminal en cada actualización del tiempo?"
  - "¿Cómo documento funcionalidad con ejemplos de uso en un README?"
  - "¿Cómo escribo docstrings correctamente en Python?"
  - "¿Qué información debe incluir un buen docstring para una función de tiempo?"
- Respuestas de la IA:
  - Barra de progreso: calcula porcentaje (elapsed/total), dibuja con bloques llenos/vacíos y actualiza con retorno de carro '\r'.
  - Limpiar pantalla: usar `os.system('cls')` para Windows y `os.system('clear')` para Linux/Mac.
  - Documentación: mantén README con descripción general, incluye guía rápida y enlaza a docs adicionales con ejemplos de comando y flujo de uso.
  - Docstrings: escribe la descripción breve de propósito, parámetros (`:param`), retorno (`:return`) y efectos secundarios. Usa estilo PEP 257 y mantén con triple comillas.
  - Funciones de tiempo: incluye qué mide, unidades (segundos/minutos), formato de valor, cómo se pausa/reanuda y qué eventos controla.
- Modificaciones realizadas: docs/asistencia_ia.md actualizada con fase 9, README enlaza documento nuevo, añadido docstrings en todas las funciones.

### Sesión 8: Commit 10 - Versión final y Refactorización OO
- Fecha: [Fecha actual]
- IA utilizada: Antigravity (Google DeepMind)
- Tareas realizadas:
  - Refactorización completa a Programación Orientada a Objetos (POO).
  - Implementación de la clase `PomodoroTimer` para encapsular el estado (eventos, ciclos, OS).
  - Mejora de `config.py`: Eliminación de listas mutables, uso de diccionario `TIMER_CONFIG`.
  - Mejora de `notificaciones.py`: Consolidación de sonidos y estilos de mensaje.
  - Validación de casos edge (ciclos <= 0, tiempos inválidos).
- Preguntas para la IA:
  - "¿Cómo puedo refactorizar mi código de temporizador para hacerlo más modular?"
  - "¿Qué casos edge debería probar en mi Pomodoro Timer?"
- Respuestas de la IA:
  - Modularidad: La mejor forma es usar clases para separar la lógica de negocio (el tiempo) de la interfaz (menús y notificaciones). Esto permite reutilizar la clase `PomodoroTimer` en una futura GUI sin cambiar el código core.
  - Casos edge: Probar valores como 0 ciclos (debe dar error o salir), números negativos (validados en config), y valores extremadamente grandes. También probar la interrupción brusca (Ctrl+C).
- Modificaciones realizadas: Todo el proyecto migrado a estructura de clase. `asistencia_ia.md` actualizado con el cierre del proyecto.
