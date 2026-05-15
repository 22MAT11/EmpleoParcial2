# Visualización de mapa coroplético de Colombia.

from typing import Optional

import plotly.graph_objects as go

from core.constants import AÑOS, COLORES_REGION
from core.theme import (
    BORDER_COLOR, HIGHLIGHT_COLOR, MAP_CENTER_LAT, MAP_CENTER_LON,
    PAPER_BACKGROUND, TEXT_COLOR,
)
from data import CIUDADES, EMPLEO_BASE, SECTOR_DOMINANTE, SIGMA_BASE
from services.estadisticas_service import calcular_media_nacional, ajustar_tasa_por_genero
from services.outlier_service import es_outlier


# Genera el mapa de Colombia con tasas de empleo por ciudad.
def figura_mapa(año: int, ciudad_sel: Optional[str] = None, region_filtro: Optional[str] = "Todas", genero: str = "Ambos") -> go.Figure:

    idx = AÑOS.index(año)
    mu_nac, _ = calcular_media_nacional(año, genero)

    ciudades_filtradas = {
        c: info for c, info in CIUDADES.items()
        if region_filtro == "Todas" or info["region"] == region_filtro
    }

    lats, lons, nombres, tasas, regiones, textos = [], [], [], [], [], []
    for ciudad, info in ciudades_filtradas.items():
        tasa = EMPLEO_BASE[ciudad][idx]
        tasa = ajustar_tasa_por_genero(tasa, ciudad, genero)
        if tasa is None:
            continue
        sigma = SIGMA_BASE[ciudad]
        outlier = es_outlier(ciudad, año)
        lats.append(info["lat"])
        lons.append(info["lon"])
        nombres.append(ciudad)
        tasas.append(tasa)
        regiones.append(info["region"])
        textos.append(
            f"<b>{ciudad}</b><br>"
            f"Región: {info['region']}<br>"
            f"Tasa Empleo: {tasa:.1f}%<br>"
            f"σ = {sigma}<br>"
            f"Sector: {SECTOR_DOMINANTE[ciudad]}<br>"
            f"{'⚠️ OUTLIER (>2σ)' if outlier else '✓ Dentro rango normal'}"
        )

    fig = go.Figure()
    for region, color in COLORES_REGION.items():
        mask = [r == region for r in regiones]
        fig.add_trace(
            go.Scattergeo(
                lat=[lats[i] for i in range(len(lats)) if mask[i]],
                lon=[lons[i] for i in range(len(lons)) if mask[i]],
                mode="markers+text",
                marker=dict(
                    size=[max(8, tasas[i] / 4.5) for i in range(len(tasas)) if mask[i]],
                    color=color,
                    opacity=0.8,
                    line=dict(color="white", width=1.5),
                ),
                text=[nombres[i] for i in range(len(nombres)) if mask[i]],
                textposition="top center",
                textfont=dict(color=TEXT_COLOR, size=10),
                hovertext=[textos[i] for i in range(len(textos)) if mask[i]],
                hoverinfo="text",
                name=region,
            )
        )

    # Resaltar ciudad seleccionada
    if ciudad_sel and ciudad_sel in CIUDADES:
        info = CIUDADES[ciudad_sel]
        fig.add_trace(
            go.Scattergeo(
                lat=[info["lat"]],
                lon=[info["lon"]],
                mode="markers",
                marker=dict(size=18, color=HIGHLIGHT_COLOR, opacity=1.0, symbol="circle", line=dict(color="white", width=2)),
                hoverinfo="skip",
                name="Seleccionada",
                showlegend=False,
            )
        )

    fig.update_layout(
        geo=dict(
            scope="south america",
            projection=dict(type="mercator"),
            center=dict(lat=MAP_CENTER_LAT, lon=MAP_CENTER_LON),
            showcountries=True,
            showland=True,
            landcolor="rgba(240,240,240,1)",
            bgcolor="rgba(0,0,0,0)",
        ),
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor=PAPER_BACKGROUND,
        plot_bgcolor=PAPER_BACKGROUND,
        legend=dict(
            bgcolor="rgba(255, 255, 255, 0.98)",
            font=dict(color=TEXT_COLOR, size=11),
            bordercolor=BORDER_COLOR,
            borderwidth=1.5,
            x=0.02,
            y=0.98,
            xanchor="left",
            yanchor="top",
        ),
        height=440,
    )
    return fig
