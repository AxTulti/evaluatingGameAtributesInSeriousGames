from segmentation.run_segmentation import run_segmentation
from preprocessing.run_preprocessing import run_preprocessing

def main():
    df, df_importance, df_scoring = run_segmentation()
    df = run_preprocessing(df)
    
    

if __name__ == "__main__":
    main()