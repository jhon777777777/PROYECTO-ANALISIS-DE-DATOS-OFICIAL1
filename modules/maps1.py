import plotly.express as px
import json

def mapa_pobreza_completo(df):
    # Calcular porcentaje de pobreza por departamento en todo el dataframe (sin filtro)
    df_map = df.groupby('departamento')['pobreza'].apply(
        lambda x: (x != 'No pobre').mean() * 100
    ).reset_index().sort_values(by='pobreza', ascending=False)
    df_map.rename(columns={'pobreza': 'porcentaje_pobreza'}, inplace=True)

    # Cargar GeoJSON
    with open("geo/peru_departamentos.geojson", "r", encoding="utf-8") as f:
        departamentos_geojson = json.load(f)

    fig = px.choropleth(
        df_map,
        geojson=departamentos_geojson,
        locations='departamento',
        featureidkey='properties.NOMBDEP',
        color='porcentaje_pobreza',
        color_continuous_scale='Reds',
        range_color=(0, 100),
        hover_name='departamento',
        hover_data={'porcentaje_pobreza': ':.2f'},
        labels={'porcentaje_pobreza': 'Pobreza (%)'},
        title='Mapa de pobreza (completo)'
    )

    fig.update_geos(fitbounds="locations", visible=False)

    fig.update_layout(
        margin={"r":0,"t":80,"l":0,"b":0},
        coloraxis_colorbar=dict(
            title="Pobreza (%)",
            tickvals=[0, 20, 40, 60, 80, 100],
            ticktext=['0%', '20%', '40%', '60%', '80%', '100%'],
            len=0.85,
            thickness=20,
            x=0.9,
            y=0.5
        ),
        title_x=0.5,
        height=800,
        font=dict(color="black"),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    return fig
