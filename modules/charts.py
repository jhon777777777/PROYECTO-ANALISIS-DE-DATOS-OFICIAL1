import plotly.express as px

def plot_bar(df, x, y, color=None, title="", orientation="v"):
    fig = px.bar(df, x=x, y=y, color=color, orientation=orientation, title=title)
    fig.update_layout(bargap=0.2)
    return fig

def plot_pie(df, names, values, title=""):
    fig = px.pie(df, names=names, values=values, title=title, hole=0.4)
    return fig

def generate_summary_charts(df):
    pie_data = df['categoria_pobreza'].value_counts().reset_index()
    pie_data.columns = ['Categoria', 'Cantidad']

    bar_data = df.groupby('region')['pobre_bin'].mean().reset_index()
    bar_data['pobre_bin'] *= 100
    bar_data.columns = ['Region', 'Porcentaje de Pobreza']

    return {
        "pie": plot_pie(pie_data, 'Categoria', 'Cantidad', title='Distribución de Categorías de Pobreza'),
        "bar": plot_bar(bar_data, 'Region', 'Porcentaje de Pobreza', title='Pobreza Promedio por Región')
    }