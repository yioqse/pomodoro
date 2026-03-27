# 🍅 GUI - Interfaz Gráfica Pomodoro

## 📖 Descripción

Interfaz gráfica completa para el Temporizador Pomodoro construida con **Tkinter**.

Proporciona una experiencia visual moderna y amigable con:
- 🎨 Tema oscuro profesional
- 🎯 Pantalla principal intuitiva
- ⚙️ Configuración personalizable
- 📊 Estadísticas en tiempo real
- ⏱️ Display digital grande
- 📈 Barra de progreso visual
- 🔔 Integración con notificaciones

## 🚀 Inicio Rápido

### Requisitos
- Python 3.8+
- Tkinter (incluido en la mayoría de instalaciones de Python)

### En Linux (si Tkinter no está instalado)

**Ubuntu/Debian:**
```bash
sudo apt-get install python3-tk
```

**Fedora:**
```bash
sudo dnf install python3-tkinter
```

**Arch Linux:**
```bash
sudo pacman -S tk
```

### Ejecutar la GUI

**Desde la raíz del proyecto:**
```bash
python gui_launcher.py
```

**Desde el directorio GUI:**
```bash
python GUI/main_gui.py
```

## 📁 Estructura

```
GUI/
├── __init__.py              # Módulo de GUI
├── styles.py                # Temas, colores y fuentes
├── widgets.py               # Componentes personalizados
├── main_gui.py              # Aplicación principal
└── requirements_gui.txt     # Dependencias
```

## 🎮 Características

### Pantalla Principal
- Botón para iniciar sesión
- Acceso a configuración
- Visualización de estadísticas
- Información de configuración actual

### Configuración
- Personalizar tiempo de trabajo (default: 25 min)
- Personalizar descanso corto (default: 5 min)
- Personalizar descanso largo (default: 15 min)
- Personalizar número de ciclos (default: 4)

### Sesión Activa
- Display grande con formato MM:SS
- Título dinámico mostrando ciclo y fase
- Barra de progreso circular
- Botones: Iniciar, Pausa/Reanuda, Detener
- Indicador visual de estado (Trabajando/Descansando/Pausado)

### Estadísticas
- Ciclos completados en la sesión
- Ciclo actual
- Configuración activa
- Tiempo total estimado

## 🎨 Diseño Visual

### Paleta de Colores
- **Trabajo:** Rojo Tomato (#E74C3C)
- **Descanso:** Verde (#27AE60)
- **Descanso Largo:** Azul (#3498DB)
- **Fondo:** Gris oscuro (#2C3E50)
- **Botones:** Colores según contexto

### Componentes
- **ModernButton:** Botones estilo plano con hover
- **TimerDisplay:** Display digital monoespacio
- **ProgressBar:** Barra circular con porcentaje
- **StatusLabel:** Etiqueta con iconos de estado
- **ModernEntry:** Campos de entrada personalizados

## ⌨️ Controls

### En la Pantalla Principal
- **Iniciar Sesión:** Abre la pantalla de sesión activa
- **Configuración:** Permite personalizar parámetros
- **Estadísticas:** Muestra resumen de la sesión
- **Salir:** Cierra la aplicación

### Durante la Sesión
- **▶️ Iniciar:** Comienza la sesión
- **⏸️ Pausa:** Pausa/Reanuda (sin descontar tiempo)
- **⏹️ Detener:** Termina la sesión actual
- **← Menú:** Vuelve al menú principal (solo si está detenido)

## 📊 Display de Información

Durante la sesión se muestra:
```
Ciclo 1/4 - TRABAJO
        
    00:24:35
        
    [=████████░░░░░░░░░░░░] 65%
        
    🔴 Trabajando...
```

## 🔔 Notificaciones

La GUI integra las notificaciones del proyecto:
- Sonido al iniciar trabajo
- Sonido al terminar trabajo
- Sonido al iniciar descanso
- Sonido al terminar descanso
- Sonido final al completar sesión

## 🛠️ Personalización

### Modificar Colores
Edita `styles.py`, sección `COLORS`:
```python
# Cambiar color de trabajo
COLORS['tomato'] = '#YOUR_COLOR'
```

### Modificar Fuentes
Edita `styles.py`, sección `FONTS`:
```python
'title_large': ('Arial', 28, 'bold')
```

### Agregar Widgets
1. Define componente en `widgets.py`
2. Úsalo en `main_gui.py`
3. Importa desde `styles.py` para consistencia

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'tkinter'"

**Solución:** Instala tkinter (ver sección Requisitos)

### La ventana se ve pequeña o cortada

**Solución:** La ventana tiene tamaño fijo 500x600 px. Asegúrate de tener suficiente espacio en pantalla.

### Sonidos no funcionan en la GUI

**Solución:** Verifica que el volumen del sistema esté activo. Los sonidos vienen del módulo `notifier.py`.

### La sesión no avanza

**Solución:**
1. Asegúrate de hacer clic en "▶️ Iniciar"
2. Si está en pausa, haz clic en "▶️ Reanudar"
3. Verifica que el tiempo configurado sea mayor que 0

## 📚 Integración con Terminal

La GUI puede usarse paralelamente con la versión de terminal:
- Terminal: `python main.py`
- GUI: `python gui_launcher.py`

Ambas comparten la misma configuración y módulos core del proyecto.

## 🚀 Futuras Mejoras

Potenciales características para agregar:
- [ ] Soporte para temas claro/oscuro (toggle)
- [ ] Historial de sesiones
- [ ] Gráficos de productividad
- [ ] Atajos de teclado personalizables
- [ ] Integración con calendario
- [ ] Exportar estadísticas
- [ ] Modo pomodoro corto (Power Mode)
- [ ] Sonidos personalizables
- [ ] Soporte para idiomas múltiples

## 📄 Licencia

Mismo proyecto: [LICENSE](../LICENSE)

---

**¡Disfruta usando Pomodoro con interfaz gráfica!** 🍅
