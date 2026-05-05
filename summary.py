import pandas as pd
import numpy as np

def generate_mean_and_std_df(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la media y la desviación estándar para cada atributo numérico.
    Diferencia las respuestas por género (Global, Masculino, Femenino).
    """
    # 1. Seleccionamos solo las columnas numéricas para los cálculos
    numeric_cols = input_df.select_dtypes(include=[np.number]).columns
    
    # 2. Cálculos Globales (Todos los datos juntos)
    global_mean = input_df[numeric_cols].mean().rename('Media Global')
    global_std = input_df[numeric_cols].std().rename('Desv. Est. Global')
    
    # Iniciamos el DataFrame de resumen con los datos globales
    summary_df = pd.concat([global_mean, global_std], axis=1)
    
    # 3. Cálculos por Género
    if 'genero' in input_df.columns:
        # Agrupamos los datos numéricos por la columna 'genero'
        grouped = input_df.groupby('genero')[numeric_cols]
        
        # Calculamos media y desviación estándar transpuestas (para que los atributos sean las filas)
        mean_df = grouped.mean().T
        std_df = grouped.std().T
        
        # Añadimos prefijos claros a las columnas (ej. "Media Masculino", "Desv. Est. Femenino")
        mean_df.columns = [f'Media {col}' for col in mean_df.columns]
        std_df.columns = [f'Desv. Est. {col}' for col in std_df.columns]
        
        # Unimos las estadísticas por género al DataFrame principal
        summary_df = pd.concat([summary_df, mean_df, std_df], axis=1)
    else:
        print("⚠️ Advertencia: No se encontró la columna 'genero' en el DataFrame. "
              "Solo se calcularon las estadísticas globales.")
        
    # Redondeamos a 2 decimales para mantener la tabla limpia y profesional
    summary_df = summary_df.round(2)
    
    # Nombramos el índice para que se vea bien al imprimirlo con rich en tables.py
    summary_df.index.name = 'Atributo'
    
    # Rellenar los NaN con "N/A" por si algún grupo no tuvo varianza (ej. un solo encuestado de un género)
    summary_df = summary_df.fillna("N/A")
    
    return summary_df