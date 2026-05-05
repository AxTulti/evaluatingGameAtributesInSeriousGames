import pandas as pd
import numpy as np
import json
pd.set_option('future.no_silent_downcasting', True)

def run_summary(input_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calcula la media y la desviación estándar para cada Subatributo numérico.
    Diferencia las respuestas por género (Global, Masculino, Femenino).
    """
    
    with open('./subattributes.json', 'r', encoding='utf-8') as f:
        subattributes = json.load(f)
    
    # Cálculos Globales (Todos los datos juntos)
    global_mean = input_df.mean().rename('Media Global')
    global_std = input_df.std().rename('Desv. Est. Global')
    
    new_index = list(subattributes.values())
    
    # Iniciamos el DataFrame de resumen con los datos globales
    summary_df = pd.concat([global_mean, global_std], axis=1)
    summary_df = summary_df.reset_index()
    
    summary_df.columns = ['Código', 'Media Global', 'Desv. Est. Global']
    summary_df['Subatributo'] = summary_df['Código'].map(subattributes)
    
    cols = ['Subatributo', 'Código', 'Media Global', 'Desv. Est. Global']
    summary_df = summary_df[cols]
        
    # Redondeamos a 2 decimales
    summary_df = summary_df.round(2)
    
    # Nombramos el índice para que se vea bien al imprimirlo con rich en tables.py
    summary_df.index.name = 'Subatributo'
    
    # Rellenar los NaN con "N/A" por si algún grupo no tuvo varianza (ej. un solo encuestado de un género)
    summary_df = summary_df.fillna("N/A")
    
    summary_df.to_excel("respuestas_de_encuesta_resumen.xlsx", index=False, sheet_name='data')
    
    return summary_df

if __name__ == "__main__":
    run_summary()