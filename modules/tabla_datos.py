import streamlit as st

def mostrar_tabla_datos(filtered_df):
    st.subheader("Vista previa de los datos filtrados")
    st.dataframe(filtered_df.head(50))
