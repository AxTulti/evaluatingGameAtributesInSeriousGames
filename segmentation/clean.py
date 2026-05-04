import pandas as pd

# Fase 1 — Carga de datos y limpieza inicial

def load_data(excel_path):
    try:    
        raw_data = pd.read_excel(excel_path, header=None)

        print("Original entries:", len(raw_data))
        
        return raw_data
    except:
        raise ValueError("Archivo no Encontrado")

# Fase 2 — Selección y renombramiento de columnas

def clean_data(raw_data):
    try:
        data = raw_data[(raw_data[2] == "Si") & (raw_data[14] == "Sí")]

        print("Filtered entries:", len(data))
        
        new_columns = {
            4: "genero",
            5: "edad",
            21: "nombre_videojuego",
            22: "categoria_videojuego",
            23: "desafio_importancia",
            24: "desafio_calificacion",
            25: "retroalimentacion_importancia",
            26: "retroalimentacion_calificacion",
            27: "inmersion_importancia",
            28: "inmersion_calificacion",
            29: "concentracion_importancia",
            30: "concentracion_calificacion",
            31: "claridad_de_objetivos_importancia",
            32: "claridad_de_objetivos_calificacion",
            33: "autonomia_importancia",
            34: "autonomia_calificacion",
            35: "interaccion_social_importancia",
            36: "interaccion_social_calificacion",
            37: "mejora_del_conocimiento_importancia",
            38: "mejora_del_conocimiento_calificacion",
            39: "involucramiento_emocional_importancia",
            40: "involucramiento_emocional_calificacion",
            41: "equilibrio_entre_habilidades_y_tareas_importancia",
            42: "equilibrio_entre_habilidades_y_tareas_calificacion",
            43: "narrativa_atractiva_importancia",
            44: "narrativa_atractiva_calificacion",
            45: "estructura_de_progresion_importancia",
            46: "estructura_de_progresion_calificacion",
            47: "animacion_y_sonido_importancia",
            48: "animacion_y_sonido_calificacion",
            49: "calificacion_global"
        }   
        
        data = data.rename(columns=new_columns).loc[:, new_columns.values()]
        
        return data
    except:
        raise RuntimeError("Error al limpiar datos")

def normalize_genders(data):
        
    data.loc[~data["genero"].isin(["Masculino", "Femenino"]), "genero"] = "Otro"
    
    return data