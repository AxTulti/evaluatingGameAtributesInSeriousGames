# Phase 4
import pandas as pd

def question_segmentation(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Creates 2 new DataFrames.

    df_importance: 
        Contains the columns with questions regarding importance.

    df_scoring:  
        Contains the columns with questions regarding the scoring of each aspect
        and a global score for the serious game selected
    """
    
    try:
    
        # for both dfs
        base_columns = [
            "genero",
            "edad",
            "nombre_videojuego",
            "categoria_videojuego"
        ]

        # questions about importance
        importance_columns = [
            "desafio_importancia",
            "retroalimentacion_importancia",
            "inmersion_importancia",
            "concentracion_importancia",
            "claridad_de_objetivos_importancia",
            "autonomia_importancia",
            "interaccion_social_importancia",
            "mejora_del_conocimiento_importancia",
            "involucramiento_emocional_importancia",
            "equilibrio_entre_habilidades_y_tareas_importancia",
            "narrativa_atractiva_importancia",
            "estructura_de_progresion_importancia",
            "animacion_y_sonido_importancia"
        ]

        # questions about score
        score_columns = [
            "desafio_calificacion",
            "retroalimentacion_calificacion",
            "inmersion_calificacion",
            "concentracion_calificacion",
            "claridad_de_objetivos_calificacion",
            "autonomia_calificacion",
            "interaccion_social_calificacion",
            "mejora_del_conocimiento_calificacion",
            "involucramiento_emocional_calificacion",
            "equilibrio_entre_habilidades_y_tareas_calificacion",
            "narrativa_atractiva_calificacion",
            "estructura_de_progresion_calificacion",
            "animacion_y_sonido_calificacion",
            "calificacion_global"
        ]

        # new dfs
        df_importance = df[base_columns + importance_columns].copy()
        df_scoring = df[base_columns + score_columns].copy()

        return df_importance, df_scoring
    except: 
        raise RuntimeError("Error al agrupar datos")