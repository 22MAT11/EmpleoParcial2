# 📊 Analizador Interactivo de Empleabilidad en Colombia (2021-2026)

Alumnos:  
        - Dharla Jose Duran Riobo 
        - Ivan David Guette Serna 
        - Maira Alejandra Torres Oñate

Aplicación web desarrollada en **Python y Dash** para analizar la empleabilidad en Colombia entre los años 2021 y 2026. El proyecto utiliza información del **DANE-GEIH** y permite visualizar datos mediante gráficos interactivos y análisis estadístico.

---

# 🎯 Objetivo

Brindar una herramienta visual e interactiva para estudiar el comportamiento del empleo en distintas regiones del país, identificando tendencias, diferencias regionales, sectores económicos relevantes y variaciones estadísticas.

---

# 🚀 Funcionalidades

## 📱 Módulos principales

### Overview

* Mapa interactivo de Colombia
* KPIs dinámicos
* Ranking de ciudades

### Regional

* Distribución normal
* Tendencias temporales
* Sectores económicos
* Comparación por género

### Nacional

* Correlación fronteriza
* Heatmap temporal
* Sectores económicos DANE

---

# 📈 Visualizaciones Disponibles

| Visualización              | Descripción                       |
| -------------------------- | --------------------------------- |
| 🗺️ Mapa de Colombia        | Tasas de empleabilidad por ciudad |
| 📊 Ranking Nacional        | Comparación entre ciudades        |
| 📉 Evolución Temporal      | Tendencias entre 2021 y 2026      |
| 🔔 Distribución Normal     | Comparación con la media nacional |
| 🥧 Sectores Económicos     | Participación laboral por sector  |
| 👥 Distribución por Género | Participación femenina            |
| 🔗 Correlación Fronteriza  | Migración vs volatilidad laboral  |
| 🌡️ Heatmap                | Correlación temporal por ciudad   |

---

# 🏗️ Arquitectura del Proyecto

El proyecto está dividido en módulos para mantener una estructura organizada y escalable:

```bash
EmpleaData/
├── app.py
├── requirements.txt
├── core/
├── data/
├── services/
├── visualizations/
├── ui/
└── utils/
core/ → Configuración y constantes
data/ → Gestión y carga de datos
services/ → Lógica estadística
visualizations/ → Construcción de gráficos
ui/ → Componentes de interfaz
utils/ → Funciones auxiliares

# 📚 Tecnologías Utilizadas
    Tecnología	Uso
    Python	Lenguaje principal
    Dash	Framework web
    Plotly	Visualizaciones
    Pandas	Manipulación de datos
    NumPy	Cálculos numéricos
    SciPy	Métodos estadísticos

# 📊 Datos Analizados
    * Ciudades estudiadas
    Bogotá
    Medellín
    Cali
    Barranquilla
    Cartagena
    Santa Marta
    Valledupar
    Montería
    Sincelejo
    Riohacha
    Bucaramanga
    Cúcuta
    Quibdó
    Arauca
    Leticia
    Pasto

# Periodo
    2021 - 2026
    Fuente oficial: DANE-GEIH

# 🔬 Metodología
    Extracción de datos del DANE-GEIH.
    Procesamiento de tasas de ocupación.
    Validación estadística.
    Imputación de datos faltantes.
    Simulación mediante distribuciones normales.
    Generación de gráficos interactivos.

# 📈 Resultados Destacados
    Crecimiento nacional aproximado de 5.3 puntos porcentuales.
    Montería presentó la mayor tasa de ocupación.
    Cali registró el mayor crecimiento del periodo.
    Promedio nacional estimado para 2026: 56.3%.
# 📝 Consideraciones
    Se utilizan datos oficiales del DANE cuando están disponibles.
    El sistema incorpora datos sintéticos como respaldo en ausencia de información.
    La simulación es reproducible mediante semillas deterministas.
    La arquitectura sigue principios SOLID y separación por capas.

# 📄 Licencia

    Proyecto académico desarrollado para la Universidad Popular del Cesar (UniCésar).
