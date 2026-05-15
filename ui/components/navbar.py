from dash import dcc, html
from data import CIUDADES
from core.constants import AÑOS, COLORES_REGION
from core.theme import COLOR_PRIMARY, TEXT_COLOR, TEXT_MUTED


def create_sidebar() -> html.Div:
    opciones_ciudades = [{"label": c, "value": c} for c in sorted(CIUDADES.keys())]
    opciones_regiones = [{"label": "Todas", "value": "Todas"}] + \
                        [{"label": r, "value": r} for r in COLORES_REGION.keys()]
    opciones_genero = [
        {"label": "Ambos", "value": "Ambos"},
        {"label": "Mujeres", "value": "Mujeres"},
        {"label": "Hombres", "value": "Hombres"},
    ]

    return html.Aside(className="sidebar", children=[

        # ── Brand ─────────────────────────────────────────────
        html.Div(className="sidebar-brand", children=[
            html.Div(className="brand-icon", children="📊"),
            html.Div([
                html.H1("EmpleaData",
                         style={"margin": 0, "fontSize": "18px",
                                "fontWeight": "700", "color": TEXT_COLOR}),
                html.P("Colombia 2021–2026",
                        style={"margin": 0, "fontSize": "10px",
                               "color": TEXT_MUTED, "fontWeight": "300"}),
            ]),
        ]),

        html.Hr(className="sidebar-divider"),

        # ── AÑO ───────────────────────────────────────────────
        html.Div(className="sidebar-section", children=[
            html.Span("AÑO", className="filter-label"),
            dcc.Slider(
                id="slider-año",
                min=2021, max=2026, step=1, value=2026,
                marks={a: {"label": str(a),
                            "style": {"color": TEXT_MUTED, "fontSize": "10px"}}
                       for a in AÑOS},
                vertical=False,
            ),
        ]),

        html.Hr(className="sidebar-divider"),

        # ── CIUDAD ────────────────────────────────────────────
        html.Div(className="sidebar-section", children=[
            html.Span("CIUDAD", className="filter-label"),
            dcc.Dropdown(
                id="dropdown-ciudad",
                options=opciones_ciudades,
                value="Bogotá",
                clearable=False,
                searchable=True,
                className="dark-dropdown",
            ),
        ]),

        # ── REGIÓN ────────────────────────────────────────────
        html.Div(className="sidebar-section", children=[
            html.Span("REGIÓN", className="filter-label"),
            dcc.Dropdown(
                id="dropdown-region",
                options=opciones_regiones,
                value="Todas",
                clearable=False,
                searchable=False,
                className="dark-dropdown",
            ),
        ]),

        # ── GÉNERO ────────────────────────────────────────────
        html.Div(className="sidebar-section", children=[
            html.Span("GÉNERO", className="filter-label"),
            dcc.Dropdown(
                id="dropdown-genero",
                options=opciones_genero,
                value="Ambos",
                clearable=False,
                searchable=False,
                className="dark-dropdown",
            ),
        ]),

        # ── Spacer ────────────────────────────────────────────
        html.Div(style={"flex": "1"}),

        # ── Footer ────────────────────────────────────────────
        html.Div(className="sidebar-footer", children=[
            html.P("Modelado y Simulacion",
                   style={"margin": 0, "fontSize": "9px", "color": TEXT_MUTED}),
            html.P("Docente: Andres Perpinan Reyes",
                   style={"margin": 0, "fontSize": "9px", "color": TEXT_MUTED}),
            html.P("Fuentes: DANE-GEIH",
                   style={"margin": "2px 0 0", "fontSize": "8px",
                          "color": "#475569"}),
        ]),
    ])
