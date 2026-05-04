from clean import load_data, clean_data, normalize_genders
from cli import data_path, ask_gender_segmentation, ask_age_segmentation
from segment import gender_segmentation, age_segmentation
from group import question_segmentation
from export import export_to_excel


def main():
    try:
        file_path = data_path()

        # Fase 1 y 2
        df = load_data(file_path)
        df = clean_data(df)
        df = normalize_genders(df)

        # Fase 3
        genders = ask_gender_segmentation()
                
        if genders:
            df = gender_segmentation(df, genders)

        ages = ask_age_segmentation()
        
        if ages:
            df = age_segmentation(df, ages)

        # Fase 4
        df_importance, df_scoring = question_segmentation(df)

        # Fase 5
        export_to_excel(df, df_importance, df_scoring)
    except Exception as error:
        print(error)
    finally:
        print("Proceso terminado")


if __name__ == "__main__":
    main()