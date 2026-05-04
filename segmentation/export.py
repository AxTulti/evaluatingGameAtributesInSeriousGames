# Phase 5
import os
import pandas as pd
from openpyxl.utils import get_column_letter


def export_to_excel(
    df_complete: pd.DataFrame,
    df_importance: pd.DataFrame,
    df_scoring: pd.DataFrame,
    output_filename: str = "resultados_encuesta.xlsx"
) -> str:
    
    """
    Combines our 3 dataframes into 1 excel file and exports it to a set path
    """
    try:
        #Where to save file
        output_path = os.path.join(os.getcwd(), output_filename)

        # Create excel sheets
        with pd.ExcelWriter(output_path, engine="openpyxl") as writer:
            df_complete.to_excel(writer, sheet_name="Datos Completos", index=False)
            df_importance.to_excel(writer, sheet_name="Importancia", index=False)
            df_scoring.to_excel(writer, sheet_name="Calificaciones", index=False)

            for sheet_name, dataframe in {
                "Datos Completos": df_complete,
                "Importancia": df_importance,
                "Calificaciones": df_scoring
            }.items():
                worksheet = writer.book[sheet_name]


                # Adjusting column width based on title 
                for col_idx, column_name in enumerate(dataframe.columns, start=1):
                    title_length = len(str(column_name))
                    adjusted_width = min(title_length + 2, 50) # Add small padding
                    col_letter = get_column_letter(col_idx)
                    worksheet.column_dimensions[col_letter].width = adjusted_width

        return output_path
    except:
        raise RuntimeError("Error al exportar archivo")
