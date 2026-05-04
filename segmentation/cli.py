# Library for aestetic CLI
# do:
# pip install questionary
# if not already installed
import questionary 

def data_path() -> str:
    return questionary.path("¿Cuál es tu ruta al archivo de datos?").ask() 

def binary_question(prompt:str, choices = ['Sí', 'No']) -> bool:
    question = questionary.select(
        prompt,
        choices=choices).ask()
    
    return (question == 'Sí')


def normalize_age(age:str):
    if age == 'Hasta los 18 años':
        return ['Menor a 15', 'Entre 15 y 18']
    if age == 'Entre 19 y 30 años':
        return ['Entre 19 y 22', 'Menor a 22', 'Entre 23 y 30']
    if age == '31 años o más':
        return ['Entre 31 y 50', 'Más de 50']
    
    return []

    

def ask_gender_segmentation():
    '''
    Returns False if no segmentation is selected
    Returns a tuple containing one or more of the following:
        {'Masculino', ''Femenino', 'Otro'}
    '''
    do_gender_segmentation = binary_question('¿Desea segmentar por género?')
    if not do_gender_segmentation: return False
    
    selected_genders = questionary.checkbox(
        'Selecciona el género a segmentar:',
        choices=[
            'Masculino',
            'Femenino',
            'Otro'
        ]
    ).ask()
    
    # If no option is selected, we don't segmentate
    if len(selected_genders) == 0: return False
    
    # If all options are selected, we don't segmentate
    if len(selected_genders) == 3: return False
    
    return selected_genders

def ask_age_segmentation():
    '''
    Returns Empty Tuple if no segmentation is selected
    Returns a tuple containing one or more of the following:
        {'Menor a 15', 'Entre 15 y 18', 'Entre 19 y 22', 'Menor a 22', 'Entre 23 y 30', 'Entre 31 y 50', 'Más de 50'} 
    '''
    
    do_age_segmentation = binary_question('¿Desea segmentar por rangos de edad?')
    if not do_age_segmentation: return False
    
    selected_ages = questionary.checkbox(
        'Selecciona la edad a segmentar:',
        choices=[
            'Hasta los 18 años',
            'Entre 19 y 30 años',
            '31 años o más'
        ]
    ).ask()
    
    # If no option is selected, we don't segmentate
    if len(selected_ages) == 0: return False
    
    # If all options are selected, we don't segmentate
    if len(selected_ages) == 3: return False
    
    
    # Cast selection into return format
    selected_ages = [normalize_age(age) for age in selected_ages]
    
    # This contains a list of tupples, we will flatten them
    selected_ages = [label for inner_tuple in selected_ages for label in inner_tuple]
    
    return selected_ages
    
def ask_segmentation():
    ''' 
        Returns False if no segmentation is required,
        Returns a tuple according to segmentation choices:
        (genders, ages)
        Where genders is a tuple containing one or more of the following:
        {'Masculino', ''Femenino', 'Otro'}
        
        And Age is a tuple containing one or more of the following
        {'Menor a 15', 'Entre 15 y 18', 'Entre 19 y 22', 'Menor a 22', 'Entre 23 y 30', 'Entre 31 y 50', 'Más de 50'} 

    '''
    do_segmentation = binary_question('¿Desea segmentar los datos?')
    if not do_segmentation: return False
    
    # Gender
    genders = ask_gender_segmentation()
    
    # Age
    ages = ask_age_segmentation()
    
    return (genders, ages)


if __name__ == "__main__":
    print("--- Tests ---")
    resultado = ask_segmentation()

    print("\n" + "="*40)
    if resultado:
        genders, ages = resultado
        print("RESULTADO DE SEGMENTACIÓN:")
        print(f"  > Géneros seleccionados: {genders if genders else 'Ninguno/Todos'}")
        print(f"  > Edades normalizadas:   {ages if ages else 'Ninguno/Todos'}")
    else:
        print("El usuario decidió NO segmentar los datos.")
    print("="*40)
