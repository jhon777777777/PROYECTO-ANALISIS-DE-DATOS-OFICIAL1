import pandas as pd

def load_data(path):
    # Carga del CSV con separador punto y coma y codificación latin1
    df = pd.read_csv(path, sep=';', encoding='latin1')

    # Limpieza completa de nombres de columnas:
    # - elimina BOM o caracteres raros
    # - pasa todo a minúsculas
    # - elimina espacios al inicio, final y dentro del nombre
    # - decodifica a utf-8 para seguridad
    df.columns = (
        df.columns
        .str.encode('utf-8')
        .str.decode('utf-8')
        .str.strip()                   # quita espacios al inicio y final
        .str.replace("ï»¿", "", regex=False)  # quita BOM
        .str.lower()                   # pasa a minúsculas
        .str.replace(" ", "", regex=False)     # elimina espacios dentro del nombre
    )

    # Diccionario para renombrar columnas si fuera necesario
    renombrar = {
        'conglome': 'conglome',
        'vivienda': 'vivienda',
        'hogar': 'hogar',
        'dparedes': 'dparedes',
        'dpisos': 'dpisos',
        'dtechos': 'dtechos',
        'dagua': 'dagua',
        'ddesague': 'ddesague',
        'codperso': 'codperso',
        'edad': 'edad',
        'dsexo': 'sexo',
        'educ': 'educ',
        'ocu500': 'ocupacion',
        'ingresostot': 'ingresototal',
        'ubigeo': 'ubigeo',
        'mieperho': 'miembros',
        'gasto_pc': 'gastopc',
        'estrsocial': 'estrato',
        'pobreza': 'pobreza',
        'ocupado': 'ocupado',
        'ingresopc': 'ingresopc',
        'departamento': 'departamento'
    }

    # Aplica renombrado solo si las columnas existen en el DataFrame
    columnas_presentes = {k: v for k, v in renombrar.items() if k in df.columns}
    df.rename(columns=columnas_presentes, inplace=True)

    # Imprime columnas para verificar (puedes comentar esta línea después)
    print("Columnas cargadas y limpias:", df.columns.to_list())

    return df
