from dash import html, dcc
from core.theme import (
    TEXT_MUTED, COLOR_PRIMARY,
)
from ui.components.navbar import create_sidebar


def _panel(children, class_extra="", style_extra=None):
    base = {}
    if style_extra:
        base.update(style_extra)
    return html.Div(children=children, className=f"glass-panel {class_extra}", style=base)


def create_layout() -> html.Div:
    return html.Div(className="app-shell", children=[

        # ── SIDEBAR (izquierda) ─────────────────────────────────
        create_sidebar(),

        # ── MAIN CONTENT (derecha) ──────────────────────────────
        html.Main(className="main-content", children=[

            # ── TABS ────────────────────────────────────────────
            dcc.Tabs(
                id="main-tabs",
                value="overview",
                children=[
                    dcc.Tab(label="Overview", value="overview",
                            className="dcc-tab", selected_className="dcc-tab--selected"),
                    dcc.Tab(label="Regional", value="regional",
                            className="dcc-tab", selected_className="dcc-tab--selected"),
                    dcc.Tab(label="Nacional", value="nacional",
                            className="dcc-tab", selected_className="dcc-tab--selected"),
                ],
                className="tabs-bar",
            ),

            # ══════════════════════════════════════════════════════
            # TAB: OVERVIEW — Mapa + KPIs + Ranking
            # ══════════════════════════════════════════════════════
            html.Div(id="tab-overview", children=[

                # Mapa + KPIs (lado a lado)
                html.Div(className="hero-grid", style={"marginTop": "20px"}, children=[
                    _panel(
                        dcc.Graph(id="mapa-colombia",
                                  config={"displayModeBar": False},
                                  style={"height": "440px"}),
                        class_extra="hero-map",
                    ),
                    _panel(
                        html.Div(id="kpi-cards", style={"height": "100%"}),
                        class_extra="hero-kpis",
                    ),
                ]),

                # Ranking + Tendencia
                html.Div(className="grid-2col", style={"marginTop": "16px"}, children=[
                    html.Div([
                        _panel(
                            dcc.Graph(id="grafica-ranking",
                                      config={"displayModeBar": False},
                                      style={"height": "360px"}),
                        ),
                        html.Span("[Top 5]", id="toggle-ranking", n_clicks=0,
                                  className="toggle-link"),
                    ]),
                    _panel(
                        dcc.Graph(id="grafica-tendencia",
                                  config={"displayModeBar": False},
                                  style={"height": "380px"}),
                    ),
                ]),
            ]),

            # ══════════════════════════════════════════════════════
            # TAB: REGIONAL — Gauss + Sectores + Genero
            # ══════════════════════════════════════════════════════
            html.Div(id="tab-regional", style={"display": "none"}, children=[

                # Gauss + Sectores
                html.Div(className="grid-2col", style={"marginTop": "20px"}, children=[
                    _panel(
                        dcc.Graph(id="grafica-gauss",
                                  config={"displayModeBar": False},
                                  style={"height": "380px"}),
                    ),
                    _panel(
                        dcc.Graph(id="grafica-sectores",
                                  config={"displayModeBar": False},
                                  style={"height": "380px"}),
                    ),
                ]),

                # Genero + Heatmap
                html.Div(className="grid-2col", style={"marginTop": "16px"}, children=[
                    _panel(
                        dcc.Graph(id="grafica-genero",
                                  config={"displayModeBar": False},
                                  style={"height": "380px"}),
                    ),
                    _panel(
                        dcc.Graph(id="grafica-heatmap",
                                  config={"displayModeBar": False},
                                  style={"height": "380px"}),
                    ),
                ]),
            ]),

            # ══════════════════════════════════════════════════════
            # TAB: NACIONAL — Correlacion + DANE + Informalidad
            # ══════════════════════════════════════════════════════
            html.Div(id="tab-nacional", style={"display": "none"}, children=[

                # Correlacion (ancho completo)
                html.Div(style={"marginTop": "20px"}, children=[
                    _panel(
                        dcc.Graph(id="grafica-correlacion",
                                  config={"displayModeBar": False},
                                  style={"height": "400px"}),
                    ),
                ]),

                # DANE sectores + Informalidad barras
                html.Div(className="grid-2col", style={"marginTop": "16px"}, children=[
                    _panel(
                        dcc.Graph(id="grafica-dane-sectores",
                                  config={"displayModeBar": False},
                                  style={"height": "380px"}),
                    ),
                    _panel(
                        dcc.Graph(id="grafica-informalidad-barras",
                                  config={"displayModeBar": False},
                                  style={"height": "380px"}),
                    ),
                ]),

                # Informalidad evolucion (ancho completo)
                _panel(
                    dcc.Graph(id="grafica-informalidad-evolucion",
                              config={"displayModeBar": False},
                              style={"height": "380px"}),
                    style_extra={"marginTop": "16px"},
                ),
            ]),

            # ── FOOTER ─────────────────────────────────────────
            html.Div(className="app-footer", children=[
                html.Span(
                    "Modelado y Simulacion | Docente: Andres Perpinan Reyes | "
                    "Fuentes: DANE-GEIH / Datos Abiertos Colombia",
                    style={"color": TEXT_MUTED, "fontSize": "10px"},
                ),
            ]),
        ]),

        # Correlacion toggle (hidden)
        html.Div(id="contenido-correlacion", style={"display": "none"}),
        html.Span(id="toggle-correlacion", style={"display": "none"}),
    ])