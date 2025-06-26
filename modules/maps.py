import plotly.express as px
import json

def poverty_map(df):
    # Normalizar nombres de departamento en el DataFrame
    df['departamento'] = df['departamento'].str.strip().str.upper()

    # Calcular porcentaje de pobreza por departamento
    df_map = df.groupby('departamento')['pobreza'].apply(
        lambda x: (x != 'No pobre').mean() * 100
    ).reset_index().rename(columns={'pobreza': 'porcentaje_pobreza'})

    # Cargar GeoJSON de departamentos
    with open("geo/peru_departamentos.geojson", "r", encoding="utf-8") as f:
        departamentos_geojson = json.load(f)

    # Opcional: Debug para ver departamentos en GeoJSON
    # geo_departments = [feat['properties']['NOMBDEP'].upper() for feat in departamentos_geojson['features']]
    # print("Departamentos en GeoJSON:", geo_departments)

    # Opcional: Verificar departamentos que no coinciden
    # faltantes = set(df_map['departamento']) - set(geo_departments)
    # if faltantes:
    #     print("Departamentos en DataFrame no en GeoJSON:", faltantes)

    # Crear el mapa coroplético
    fig = px.choropleth(
        df_map,
        geojson=departamentos_geojson,
        locations='departamento',               # columna del DataFrame
        featureidkey='properties.NOMBDEP',      # propiedad del GeoJSON
        color='porcentaje_pobreza',
        color_continuous_scale='Reds',
        range_color=(0, 100),
        hover_name='departamento',
        hover_data={'porcentaje_pobreza': ':.2f'},
        labels={'porcentaje_pobreza': 'Pobreza (%)'},
        title='Mapa de Pobreza por Departamento'
    )

    # Ajustes visuales y quitar ejes
    fig.update_geos(fitbounds="locations", visible=False)

    # Configurar colorbar personalizado y diseño
    fig.update_layout(
        margin={"r":0,"t":60,"l":0,"b":0},
        coloraxis_colorbar=dict(
            title="Pobreza (%)",
            tickvals=[0, 20, 40, 60, 80, 100],
            ticktext=['0%', '20%', '40%', '60%', '80%', '100%'],
            len=0.75,
            thickness=15,
            x=0.9,
            y=0.5
        ),
        title_x=0.5,
        height=600,
        font=dict(color="black"),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    return fig
