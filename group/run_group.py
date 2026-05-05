import pandas as pd
import numpy as np

def run_group(preprocessed_df: pd.DataFrame) -> pd.DataFrame:
    """
    This function takes a preprocessed (only integer containing) df with every subatribute
    and ponders it with the importance of each subfeature
    """
    
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
    
    CH_atributes = ['CH2', 'CH4', 'CH6']
    CH_weights = ['CH1', 'CH3', 'CH5']
    
    I_atributes = ['I2', 'I4', 'I6', 'I8']
    I_weights = ['I1', 'I3', 'I5', 'I7']
    
    C_atributes = ['C2']
    C_weights = ['C1']
    
    G_atributes = ['G2']
    G_weights = ['G1']
    
    F_atributes = ['F2']
    F_weights = ['F1']
    
    A_atributes = ['A2']
    A_weights = ['A1']
    
    S_atributes = ['S2']
    S_weights = ['S1']
    
    K_atributes = ['K2']
    K_weights = ['K1']
    
    map_subatributes_to_atributes = {
        'CH' : (CH_atributes, CH_weights),
        'I' :  (I_atributes, I_weights),
        'C' :  (C_atributes, C_weights),
        'G' :  (G_atributes, G_weights),
        'F' :  (F_atributes, F_weights),
        'A' :  (A_atributes, A_weights),
        'S' :  (S_atributes, S_weights),
        'K' :  (K_atributes, K_weights)
    }
    
    processed_list = []
    
    for idx, row in preprocessed_df.iterrows():
        dict_to_append = {}
        for key, (atribute_literals, weight_literals) in map_subatributes_to_atributes.items():
            dict_to_append[key] = np.average(row.loc[atribute_literals], weights=row.loc[weight_literals])
        
        dict_to_append['O1'] = row['O1']
        
        processed_list.append(dict_to_append)
    
    
    output_df = pd.DataFrame(processed_list)
    
    return output_df