from dash import html
from core.theme import CARD_BACKGROUND, BORDER_COLOR, TEXT_COLOR, TEXT_MUTED


def kpi_card(titulo: str, valor: str, subtexto: str,
             color: str = "#00D0FF") -> html.Div:
    return html.Div(className="kpi-card", style={
        "borderLeft": f"3px solid {color}",
        "padding": "14px 16px",
        "display": "flex",
        "flexDirection": "column",
        "justifyContent": "center",
    }, children=[
        html.Div(titulo, style={"color": "#475569", "fontSize": "9px",
                                "letterSpacing": "1.2px", "marginBottom": "5px",
                                "fontWeight": "600"}),
        html.Div(valor, style={"color": color, "fontSize": "26px",
                               "fontWeight": "700", "lineHeight": "1.1"}),
        html.Div(subtexto, style={"color": "#64748B", "fontSize": "9px",
                                  "marginTop": "4px", "fontWeight": "400"}),
    ])


def create_kpi_cards(ciudad: str, año: int, media: float, mediana: float,
                     std: float, sector: str, mu_nac: float,
                     is_outlier: bool) -> html.Div:
    from core.theme import COLOR_DANGER, COLOR_PRIMARY, COLOR_SUCCESS

    color_outlier = COLOR_DANGER if is_outlier else COLOR_SUCCESS
    outlier_label = "OUTLIER >2s" if is_outlier else "NORMAL"

    cards = [
        kpi_card("TASA EMPLEO", f"{media:.1f}%",
                 f"{ciudad} - {año}", COLOR_PRIMARY),
        kpi_card("MEDIANA",     f"{mediana:.1f}%",
                 "Brecha desigualdad", COLOR_PRIMARY),
        kpi_card("DESV. STD",   f"+-{std:.2f}",
                 "Volatilidad laboral", "#A78BFA"),
        kpi_card("SECTOR",      sector[:14],
                 "Mayor contratacion", COLOR_SUCCESS),
        kpi_card("MED. NAC.",   f"{mu_nac:.1f}%",
                 f"Colombia {año}", "#F59E0B"),
        kpi_card("ESTADO",      outlier_label,
                 f"vs. +-2s nacional", color_outlier),
    ]

    return html.Div(children=cards, style={
        "display": "grid",
        "gridTemplateColumns": "1fr",
        "gridTemplateRows": "auto auto auto",
        "gap": "6px",
        "boxSizing": "border-box",
    })
