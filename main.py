from segmentation.run_segmentation import run_segmentation
from preprocessing.run_preprocessing import run_preprocessing
from summary.run_summary import run_summary

def main():
    df, df_importance, df_scoring = run_segmentation()
    
    df = run_preprocessing(df)
    
    df = run_summary(df)
    
    

if __name__ == "__main__":
    main()