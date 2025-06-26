import streamlit as st
import plotly.express as px

def mostrar_grafico_pie(df, departamento):
    st.subheader(f"Distribución de la pobreza en {departamento}")
    pie_data = df[df['departamento'] == departamento]['pobreza'].value_counts().reset_index()
    pie_data.columns = ['Categoria', 'Cantidad']

    fig = px.pie(
        pie_data,
        names='Categoria',
        values='Cantidad',
        title=f"Distribución de pobreza en {departamento}",
        hole=0.4,
        color_discrete_sequence=px.colors.sequential.Reds
    )

    fig.update_layout(
        plot_bgcolor='#121212',
        paper_bgcolor='#121212',
        font_color='white',
        margin=dict(t=40, b=40)
    )
    st.plotly_chart(fig, use_container_width=True)
