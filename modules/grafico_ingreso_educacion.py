import streamlit as st
import plotly.express as px

def mostrar_grafico_ingreso_educacion(filtered_df):
    st.markdown("### Ingreso per cápita promedio por nivel educativo")
    if not filtered_df.empty:
        # Cambia 'ingresopc' por 'ingreso_pc'
        ingreso_promedio = filtered_df.groupby('educ')['ingreso_pc'].mean().reset_index()
        fig = px.bar(
            ingreso_promedio,
            x='educ',
            y='ingreso_pc',
            labels={'educ': 'Nivel Educativo', 'ingreso_pc': 'Ingreso promedio per cápita'},
            color='ingreso_pc',
            color_continuous_scale='Viridis',
            text=ingreso_promedio['ingreso_pc'].apply(lambda x: f'{x:,.2f}')
        )
        fig.update_layout(
            plot_bgcolor='#121212',
            paper_bgcolor='#121212',
            font_color='white',
            xaxis_title='Nivel Educativo',
            yaxis_title='Ingreso promedio per cápita',
            title_x=0.0,
            title_font_size=22,
            margin=dict(t=40, b=80)
        )
        fig.update_traces(textposition='outside')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No hay datos disponibles para los filtros seleccionados.")
