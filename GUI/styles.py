"""
🎨 Estilos y Temas para la GUI de Pomodoro

Define colores, fuentes y temas para la interfaz gráfica.
"""

# 🍅 Paleta de Colores Pomodoro
COLORS = {
    # Colores primarios
    'tomato': '#E74C3C',           # Rojo Pomodoro (trabajo)
    'tomato_light': '#EC7063',     # Rojo claro
    'tomato_dark': '#C0392B',      # Rojo oscuro
    
    # Colores secundarios
    'break': '#27AE60',            # Verde (descanso)
    'break_light': '#52BE80',      # Verde claro
    'break_dark': '#1E8449',       # Verde oscuro
    
    'long_break': '#3498DB',       # Azul (descanso largo)
    'long_break_light': '#5DADE2', # Azul claro
    'long_break_dark': '#2874A6',  # Azul oscuro
    
    # Colores neutros
    'bg_dark': '#2C3E50',          # Fondo oscuro
    'bg_light': '#ECF0F1',         # Fondo claro
    'fg_dark': '#1C2833',          # Texto oscuro
    'fg_light': '#FFFFFF',         # Texto claro
    
    # Colores de estado
    'success': '#27AE60',          # Verde éxito
    'warning': '#F39C12',          # Naranja advertencia
    'error': '#E74C3C',            # Rojo error
    'info': '#3498DB',             # Azul información
    
    # Grises
    'gray_light': '#BDC3C7',       # Gris claro
    'gray': '#95A5A6',             # Gris medio
    'gray_dark': '#34495E',        # Gris oscuro
}

# 🔤 Fuentes
FONTS = {
    # Títulos
    'title_large': ('Segoe UI', 28, 'bold'),
    'title_medium': ('Segoe UI', 20, 'bold'),
    'title_small': ('Segoe UI', 14, 'bold'),
    
    # Texto normal
    'body_large': ('Segoe UI', 16),
    'body_medium': ('Segoe UI', 12),
    'body_small': ('Segoe UI', 10),
    
    # Monoespaciada (para números)
    'mono_large': ('Courier New', 48, 'bold'),
    'mono_medium': ('Courier New', 24, 'bold'),
    'mono_small': ('Courier New', 12),
}

# 🎯 Tema Claro
LIGHT_THEME = {
    'bg': COLORS['bg_light'],
    'fg': COLORS['fg_dark'],
    'button_bg': COLORS['tomato'],
    'button_fg': COLORS['fg_light'],
    'frame_bg': COLORS['bg_light'],
    'entry_bg': COLORS['fg_light'],
    'entry_fg': COLORS['fg_dark'],
}

# 🌙 Tema Oscuro
DARK_THEME = {
    'bg': COLORS['bg_dark'],
    'fg': COLORS['fg_light'],
    'button_bg': COLORS['tomato'],
    'button_fg': COLORS['fg_light'],
    'frame_bg': COLORS['gray_dark'],
    'entry_bg': '#34495E',
    'entry_fg': COLORS['fg_light'],
}

# 📏 Espaciados
SPACING = {
    'xs': 4,
    'sm': 8,
    'md': 16,
    'lg': 24,
    'xl': 32,
}

# 🔳 Bordes
BORDER_RADIUS = {
    'sm': 4,
    'md': 8,
    'lg': 12,
}

# ⚡ Animaciones (milisegundos)
ANIMATION_SPEED = {
    'fast': 100,
    'normal': 300,
    'slow': 500,
}
