from segmentation.run_segmentation import run_segmentation
from preprocessing.run_preprocessing import run_preprocessing
from summary.run_summary import run_summary
from linear_programming.run_linear_programming import run_linear_programming

def main():
    df, df_importance, df_scoring = run_segmentation()
    
    df = run_preprocessing(df)
    
    run_summary(df)
    
    run_linear_programming(df)
    
    

if __name__ == "__main__":
    main()