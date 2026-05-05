from pulp import *
import pandas as pd
import numpy as np
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tables import print_df

def run_linear_programming(grouped_df: pd.DataFrame, n_of_iterations: int) -> pd.DataFrame:
    
    results_list = []
    
    for i in range(n_of_iterations):
        results_list.append(run_linear_programming_iteration(grouped_df))
        
    results_df = pd.DataFrame(results_list)
    
    return results_df
    



def run_linear_programming_iteration(grouped_df: pd.DataFrame) -> dict:
    
    # Grab 100 random rows
    df = grouped_df.sample(n=100, replace=False) # No va a haber remplazo en una sola iteración para no 
                                                 # biasear los weights al repetirse una entrada
 
    # Planteamiento del Modelo de Programación Lineal Usando PuLP
    # Definición de variables
    
    index_rows = df.index
    features = [col for col in df.columns if col != 'O1']

    # Weights for each feature
    B = LpVariable.dicts("Beta", features, lowBound=0, cat='Continuous')
    
    Li = LpVariable.dicts("Missing", index_rows, lowBound=0, cat='Continuous')
    Ei = LpVariable.dicts("Excedent", index_rows, lowBound=0, cat='Continuous')
    
    prob = LpProblem("best_weights", LpMinimize)
    
    # Min z
    # z = Singma(forall i) L_i + E_i
    prob += lpSum([Li[i] + Ei[i] for i in index_rows]), "Minimize_deviation"
    
    prob += lpSum([B[column] for column in features])  == 1, "Weights_Normality"
    
    for idx, row in df.iterrows():
        prob += lpSum([B[column] * row[column] for column in features]) + Li[idx] - Ei[idx] == row['O1'], f"Restriction_{idx}"
    
    # Get Restults
    prob.solve(PULP_CBC_CMD(msg=False))
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
    path = input("Enter the path to your Excel file (e.g., data/my_file.xlsx): ").strip()
    
    try:
        raw_df = pd.read_excel(path)

        if 'O1' not in raw_df.columns:
            print("Error: Target column 'O1' not found in the Excel sheet.")
        else:
            n_iters = int(input("Enter the number of iterations: "))
            
            print(f"Starting {n_iters} iterations...")

            results = run_linear_programming(raw_df, n_iters)
            
            results_numeric = results.apply(pd.to_numeric, errors='coerce').fillna(0)

            to_print = results_numeric.T
            to_print.columns = [f"Iter_{c}" for c in to_print.columns]
            
            print_df(to_print, show_index=True)
            
            
            

    except FileNotFoundError:
        print(f"Error: The file at {path} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")