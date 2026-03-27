"""
🧩 Componentes Personalizados (Widgets) para la GUI

Proporciona widgets reutilizables y personalizados para tkinter.
"""

import tkinter as tk
from tkinter import ttk
from styles import COLORS, FONTS, SPACING

class ModernButton(tk.Button):
    """Botón personalizado con estilo moderno."""
    
    def __init__(self, parent, text, bg=None, fg=None, **kwargs):
        bg = bg or COLORS['tomato']
        fg = fg or COLORS['fg_light']
        
        super().__init__(
            parent,
            text=text,
            bg=bg,
            fg=fg,
            font=FONTS['body_medium'],
            padx=SPACING['md'],
            pady=SPACING['sm'],
            relief=tk.FLAT,
            cursor='hand2',
            activebackground=COLORS['tomato_dark'],
            activeforeground=COLORS['fg_light'],
            **kwargs
        )


class BreakButton(tk.Button):
    """Botón para descanso con estilo verde."""
    
    def __init__(self, parent, text, **kwargs):
        super().__init__(
            parent,
            text=text,
            bg=COLORS['break'],
            fg=COLORS['fg_light'],
            font=FONTS['body_medium'],
            padx=SPACING['md'],
            pady=SPACING['sm'],
            relief=tk.FLAT,
            cursor='hand2',
            activebackground=COLORS['break_dark'],
            activeforeground=COLORS['fg_light'],
            **kwargs
        )


class StopButton(tk.Button):
    """Botón para detener con estilo rojo intenso."""
    
    def __init__(self, parent, text, **kwargs):
        super().__init__(
            parent,
            text=text,
            bg=COLORS['error'],
            fg=COLORS['fg_light'],
            font=FONTS['body_medium'],
            padx=SPACING['md'],
            pady=SPACING['sm'],
            relief=tk.FLAT,
            cursor='hand2',
            activebackground='#A93226',
            activeforeground=COLORS['fg_light'],
            **kwargs
        )


class TimerDisplay(tk.Label):
    """Display digital para mostrar tiempo."""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            text='00:00',
            font=FONTS['mono_large'],
            fg=COLORS['tomato'],
            bg=COLORS['bg_dark'],
            **kwargs
        )
    
    def update_time(self, minutes, seconds):
        """Actualiza el tiempo mostrado."""
        self.config(text=f'{minutes:02d}:{seconds:02d}')


class ProgressBar(tk.Canvas):
    """Barra de progreso circular personalizada."""
    
    def __init__(self, parent, radius=100, **kwargs):
        super().__init__(
            parent,
            width=radius*2,
            height=radius*2,
            bg=COLORS['bg_dark'],
            highlightthickness=0,
            **kwargs
        )
        self.radius = radius
        self.progress = 0
    
    def update_progress(self, percentage):
        """Actualiza el progreso (0-100)."""
        self.progress = max(0, min(100, percentage))
        self.redraw()
    
    def redraw(self):
        """Redibuja la barra."""
        self.delete('all')
        r = self.radius
        
        # Círculo de fondo
        self.create_oval(
            10, 10, r*2-10, r*2-10,
            fill=COLORS['gray_dark'],
            outline=COLORS['gray']
        )
        
        # Círculo de progreso (arco)
        angle = (self.progress / 100) * 360
        self.create_arc(
            10, 10, r*2-10, r*2-10,
            start=90,
            extent=-angle,
            fill=COLORS['tomato'],
            outline=COLORS['tomato'],
            width=5
        )
        
        # Texto de porcentaje
        self.create_text(
            r, r,
            text=f'{int(self.progress)}%',
            font=FONTS['title_small'],
            fill=COLORS['fg_light']
        )


class ModernEntry(tk.Entry):
    """Campo de entrada personalizado."""
    
    def __init__(self, parent, **kwargs):
        super().__init__(
            parent,
            font=FONTS['body_medium'],
            bg=COLORS['fg_light'],
            fg=COLORS['fg_dark'],
            relief=tk.FLAT,
            bd=2,
            **kwargs
        )


class ModernFrame(tk.Frame):
    """Frame personalizado con estilo."""
    
    def __init__(self, parent, bg=None, **kwargs):
        bg = bg or COLORS['frame_bg']
        super().__init__(parent, bg=bg, **kwargs)


class StatusLabel(tk.Label):
    """Etiqueta de estado con icon."""
    
    def __init__(self, parent, text='', **kwargs):
        super().__init__(
            parent,
            text=text,
            font=FONTS['body_small'],
            fg=COLORS['gray'],
            bg=COLORS['bg_dark'],
            **kwargs
        )
    
    def set_working(self):
        """Estado: Trabajando."""
        self.config(text='🔴 Trabajando...', fg=COLORS['tomato'])
    
    def set_breaking(self):
        """Estado: Descansando."""
        self.config(text='🟢 Descansando...', fg=COLORS['break'])
    
    def set_paused(self):
        """Estado: Pausado."""
        self.config(text='⏸️ Pausado', fg=COLORS['warning'])
    
    def set_idle(self):
        """Estado: Inactivo."""
        self.config(text='⚪ Listo', fg=COLORS['gray'])
