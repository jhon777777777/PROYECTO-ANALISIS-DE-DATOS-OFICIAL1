import streamlit as st
from modules.data_loader import load_data
from modules.filters import aplicar_filtros, mostrar_filtros
from modules.grafico_pobreza_departamentos import mostrar_grafico_pobreza_departamentos
from modules.grafico_ingreso_educacion import mostrar_grafico_ingreso_educacion
from modules.grafico_pie_pobreza import mostrar_grafico_pie
from modules.tabla_datos import mostrar_tabla_datos
from modules.maps import poverty_map  # Mapa con filtro
from modules.maps1 import mapa_pobreza_completo  # Mapa completo

# Configuración general de página
st.set_page_config(page_title="PROYECTO DE ALGORITMOS - Pobreza en el Perú", layout="wide")

# Tema oscuro global
st.markdown("""
    <style>
    .reportview-container {
        background-color: #121212;
        color: white;
    }
    .sidebar .sidebar-content {
        background-color: #1E1E1E;
        color: white;
    }
    .css-1d391kg {
        background-color: #121212;
    }
    </style>
""", unsafe_allow_html=True)

# Carga de datos
df = load_data("data/enaho_2020_2024.csv")

# Verifica que las columnas necesarias existen
expected_columns = ['educ', 'ingreso_pc', 'pobreza', 'departamento', 'edad']
missing_cols = [col for col in expected_columns if col not in df.columns]
if missing_cols:
    st.error(f"Faltan columnas en los datos: {missing_cols}")
else:
    # Mostrar filtros y aplicar
    departamento, categoria_pobreza, edad_range = mostrar_filtros(df)
    filtered_df = aplicar_filtros(df, departamento, categoria_pobreza, edad_range)

    # Título principal y resumen
    st.markdown("### 📊 Análisis de Pobreza en el Perú (ENAHO 2020 - 2024)")
    st.markdown(f"**Registros encontrados:** {len(filtered_df)}")

    # Mostrar gráficos y tabla
    mostrar_grafico_pobreza_departamentos(df)
    mostrar_grafico_ingreso_educacion(filtered_df)
    mostrar_grafico_pie(df, departamento)
    mostrar_tabla_datos(filtered_df)

    # Mostrar mapa de pobreza por departamento (filtrado)
    st.markdown("### 🗺️ Mapa de pobreza por departamento (filtrado)")
    fig_map = poverty_map(filtered_df)
    st.plotly_chart(fig_map, use_container_width=True)

# Mostrar mapa completo al final, usando todo el dataframe sin filtro
st.markdown("## 🗺️ Mapa de pobreza (completo)")
fig_completo = mapa_pobreza_completo(df)
st.plotly_chart(fig_completo, use_container_width=True)
