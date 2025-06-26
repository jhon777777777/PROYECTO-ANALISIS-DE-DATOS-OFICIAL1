from sklearn.cluster import KMeans
import plotly.express as px

def run_clustering_analysis(df):
    df_cluster = df[['ingper', 'miembros']].dropna()

    kmeans = KMeans(n_clusters=3, random_state=42)
    df_cluster['cluster'] = kmeans.fit_predict(df_cluster[['ingper', 'miembros']])

    fig = px.scatter(
        df_cluster,
        x='ingper',
        y='miembros',
        color='cluster',
        title='Agrupamiento de Hogares según Ingreso y Miembros',
        labels={'ingper': 'Ingreso per cápita', 'miembros': 'Miembros del hogar'}
    )
    return fig