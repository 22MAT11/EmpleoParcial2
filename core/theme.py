"""
Theme tokens para el estilo visual claro (Light Mode).
Centraliza todos los colores de UI para mantener consistencia visual.
"""

# Fondos
PAPER_BACKGROUND = "rgba(255,255,255,1)"       # Fondo base blanco para gráficas
PLOT_BACKGROUND = "rgba(255,255,255,1)"  # Blanco para blending
CARD_BACKGROUND = "rgba(255, 255, 255, 0.9)" # Blanco con ligera transparencia
CONTROLS_BACKGROUND = "rgba(248, 250, 252, 0.95)" # Fondo claro para navbar
BORDER_COLOR = "rgba(0, 0, 0, 0.1)" # Borde sutil

# Tipografía
TEXT_COLOR = "#1E293B"             # Texto principal oscuro
TEXT_MUTED = "#64748B"            # Texto secundario
TEXT_DISABLED = "#94A3B8"         # Texto deshabilitado

# Acento principal — Azul
COLOR_PRIMARY = "#2563EB"
COLOR_PRIMARY_HOVER = "#1D4ED8"
COLOR_PRIMARY_LIGHT = "rgba(37, 99, 235, 0.1)"

# Colores semánticos
COLOR_SUCCESS = "#10B981"
COLOR_DANGER = "#EF4444"
COLOR_SUCCESS_BG = "rgba(16, 185, 129, 0.1)"
COLOR_DANGER_BG = "rgba(239, 68, 68, 0.1)"

# Gráficas
GRID_COLOR = "rgba(0, 0, 0, 0.1)"
NATIONAL_FILL = "rgba(234, 88, 12, 0.1)"
NATIONAL_LINE = "#EA580C"

# Destacado (mapa)
HIGHLIGHT_COLOR = "#F59E0B"

# Estilos de mapa (modo claro)
# Usar 'open-street-map' permite renderizar tiles sin token de Mapbox
MAP_STYLE = "open-street-map"
MAP_CENTER_LAT = 4.5709
MAP_CENTER_LON = -74.2973
MAP_ZOOM = 4.5
MAP_CENTER_LAT = 4.5709
MAP_CENTER_LON = -74.2973
MAP_ZOOM = 4.5


def hex_to_rgba(hex_color: str, alpha_hex: int) -> str:
    """Convierte #RRGGBB a rgba() con opacidad hex (0-255).
    Uso: hex_to_rgba("#B81C2E", 0x18) -> "rgba(184,28,46,24)"
    """
    if hex_color.startswith("rgba"):
        return hex_color
    if len(hex_color) == 7 and hex_color.startswith("#"):
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        return f"rgba({r},{g},{b},{alpha_hex/255.0:.2f})"
    return hex_color
