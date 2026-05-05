import pandas as pd
import numpy as np
import json

## Standarizing column names

# |Spanish Feature Concept      |Parent Category      |Importance Code|Rating Code|
# |-----------------------------|---------------------|---------------|-----------|
# |Desafío                      |Challenge            |CH1            |CH2        |
# |Equilibrio Habilidades/Tareas|Challenge            |CH3            |CH4        |
# |Estructura de Progresión     |Challenge            |CH5            |CH6        |
# |Inmersión                    |Immersion            |I1             |I2         |
# |Involucramiento Emocional    |Immersion            |I3             |I4         |
# |Narrativa Atractiva          |Immersion            |I5             |I6         |
# |Animación y Sonido           |Immersion            |I7             |I8         |
# |Concentración                |Concentration        |C1             |C2         |
# |Claridad de Objetivos        |Goal Clarity         |G1             |G2         |
# |Retroalimentación            |Feedback             |F1             |F2         |
# |Autonomía                    |Autonomy             |A1             |A2         |
# |Interacción Social           |Social Interaction   |S1             |S2         |
# |Mejora del Conocimiento      |Knowledge Improvement|K1             |K2         |
# |Calificación Global          |Overall              |O1             |—          |

def run_preprocessing(df):
    with open('./subattributes.json', 'r', encoding='utf-8') as f:
        subattributes = json.load(f)
    
    df = df.iloc[:, 4:]

    old_cols = list(df.columns)
    
    normalization_mapping = dict(zip(old_cols, subattributes.keys()))

    df.columns = [normalization_mapping.get(c) for c in df.columns]

    df.to_excel("respuestas_de_encuesta_preprocesados.xlsx", index=False, sheet_name='data')
    
    return df

if __name__ == "__main__":
    run_preprocessing()