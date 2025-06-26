import streamlit as st
import plotly.express as px

def mostrar_grafico_pobreza_departamentos(df):
    df_pobreza_depto = df.groupby('departamento')['pobreza'].apply(
        lambda x: (x != 'No pobre').mean() * 100
    ).reset_index().sort_values(by='pobreza', ascending=False)

    fig = px.bar(
        df_pobreza_depto,
        x='departamento',
        y='pobreza',
        labels={'departamento': 'Departamento', 'pobreza': '% Nivel de Pobreza'},
        title='Nivel de Pobreza por Departamentos',
        text=df_pobreza_depto['pobreza'].apply(lambda x: f'{x:.1f}%'),
        color='pobreza',
        color_continuous_scale='Reds'
    )

    fig.update_layout(
        height=700,
        plot_bgcolor='#121212',
        paper_bgcolor='#121212',
        font_color='white',
        xaxis_tickangle=-45,
        yaxis=dict(title='% de Pobreza', gridcolor='#333333'),
        coloraxis_showscale=False,
        title_x=0.0,
        title_font_size=22,
        margin=dict(t=80, b=120),
        xaxis=dict(
            tickfont=dict(size=12),
            title_font=dict(size=16),
            automargin=True
        )
    )

    fig.update_traces(
        textposition='outside',
        marker_line_width=1.5,
        marker_line_color='white',
        width=0.5
    )

    st.markdown(
        """
        <style>
        .scroll-container {
            overflow-x: auto;
            padding-bottom: 20px;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div class="scroll-container">', unsafe_allow_html=True)
    st.plotly_chart(fig, use_container_width=False)
    st.markdown('</div>', unsafe_allow_html=True)
