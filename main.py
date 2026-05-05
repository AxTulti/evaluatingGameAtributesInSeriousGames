from segmentation.run_segmentation import run_segmentation
from preprocessing.run_preprocessing import run_preprocessing
from summary.run_summary import run_summary
from linear_programming.run_linear_programming import run_linear_programming
from group.run_group import run_group
from tables import print_df
import questionary

def main():
    df, df_importance, df_scoring = run_segmentation()
    
    print(f'{len(df)} rows after segmentation... ')
    
    df = run_preprocessing(df)
    
    statistical_sumary = run_summary(df)
    print_df(statistical_sumary)
    
    export_path = questionary.path("¿Cuál es tu ruta para exportar el resumen estadístico (.xlsx)?").ask() 
    
    statistical_sumary.to_excel(export_path)
    
    
    df = run_group(df)
    
    iter_weights_df = run_linear_programming(df, 15)
    
    export_path = questionary.path("¿Cuál es tu ruta para exportar el archivo de pesos? (.xlsx)").ask() 
    
    iter_weights_df.to_excel(export_path)
    
    
    
    

if __name__ == "__main__":
    main()