import streamlit as st

def filter_by_conglome(df, conglome):
    return df[df['conglome'] == conglome]

def filter_by_region(df, region):
    return df[df['region'] == region]

def filter_by_poverty(df, category):
    return df[df['categoria_pobreza'] == category]

def mostrar_filtros(df):
    st.sidebar.title("Filtros")
    departamento = st.sidebar.selectbox("Departamento", sorted(df['departamento'].dropna().unique()))
    categoria_pobreza = st.sidebar.selectbox("Categoría de pobreza", sorted(df['pobreza'].dropna().unique()))
    edad_min = int(df['edad'].min())
    edad_max = int(df['edad'].max())
    edad_range = st.sidebar.slider("Rango de edad", min_value=edad_min, max_value=edad_max, value=(edad_min, edad_max))
    return departamento, categoria_pobreza, edad_range

def aplicar_filtros(df, departamento, categoria_pobreza, edad_range):
    return df[
        (df['departamento'] == departamento) &
        (df['pobreza'] == categoria_pobreza) &
        (df['edad'] >= edad_range[0]) &
        (df['edad'] <= edad_range[1])
    ]
