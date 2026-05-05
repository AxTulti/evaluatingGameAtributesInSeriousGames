from pulp import *
import pandas as pd
import numpy as np

def run_linear_programming(grouped_df: pd.DataFrame, n_of_iterations: int) -> pd.DataFrame:
    
    # Grab 100 random rows
    
    df = df.sample(n=100, replace=True) 
    
    
    for row in df.rows:
        pass    
    



def run_linear_programming_iteration(grouped_df: pd.DataFrame) -> pd.DataFrame:
    
    # Grab 100 random rows
    df = grouped_df.sample(n=100, replace=False) # No va a haber remplazo en una sola iteración para no 
                                                 # biasear los weights al repetirse una entrada
    
    
    ######## Planteamiento del Modelo de Programación Lineal Usando PuLP
    
    ##### Definición de variables
    
    index_rows = df.index
    features = [col for col in df.columns if col != 'O1']

    # Weights for each feature
    B = LpVariable.dicts("Beta", features, lowBound=0, cat='Continuous')
    
    Li = LpVariable.dicts("Missing", index_rows, lowBound=0, cat='Continuous')
    Ei = LpVariable.dicts("Excedent", index_rows, lowBound=0, cat='Continuous')
    
    prob = LpProblem("best_weights", LpMinimize)
    
    # Min z
    # z = Singma(forall i) L_i + E_i
    prob += lpSum([Li[i] + Ei[i] for i in index_rows]), "Minimize diviation"
    
    prob += lpSum([B[column] for column in features])  == 1, "Weights_Normality"
    
    for idx, row in df.iterrows():
        prob += lpSum([B[column] * row[column] for column in features]) + Li[idx] - Ei[idx] == row['O1'], f"Restriction_{idx}"
    
    # Obtener Resultados
    prob.solve()
    #print(f"Resultado de la optimización: {LpStatus[prob.status]}")

    # for f in features:
    #     print(f"Peso {f}: {value(B[f]):.4f}")

    # print(f"Suma total de desviaciones: {value(prob.objective):.4f}")
    
    
    result_dict = {}
    for column in features:
        result_dict[f'peso_{column}'] = value(B[column])
        
    result_dict['desviaction_total'] = value(prob.objective)
    
    return result_dict 

if __name__ == "__main__":
    run_linear_programming()