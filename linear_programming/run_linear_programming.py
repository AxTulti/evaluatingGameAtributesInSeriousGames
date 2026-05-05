from pulp import *

def run_linear_programming(df):
    
    # Grab 100 random rows
    
    df = df.sample(n=100, replace=True) 
    
    
    for row in df.rows:
        
    

if __name__ == "__main__":
    run_linear_programming()