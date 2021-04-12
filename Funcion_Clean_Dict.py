# Dado el siguiente diccionario de datos:

precios = {
    'ACCIONA': [78.60, 84.95, 77.20],
    'ACERINOX': [5.88, 51.25, 58.42],
    'INDITEX': [49.99, 57.89, 68.5],
    'ENEGAS': [0.5, 0.78, 48.75],
    'FERROVIAL': [78.58, 24.25, 65.45]
}

# Modifica cualquier precio inferior a 50 y, finalmente, devuelve el diccionario de datos actualizado por cada nombre de empresa.

# En este caso, en cada campo **key** tenemos una lista, simplemente tenemos que ir iterativamente por cada campo clave, 
# con un nuevo bucle for y modificando valores de índice <50 por 50.
# Lo primero, para modularizar el programa definiremos una función que simplemente devuelva 50 si el valor es menor que 50.

def update_value(value):
    """
    Función que actualiza un valor en función de un punto de corte.
    
    input
    value: float
    
    output
    value: float | new_value: int
    """
    
    if value < 50:
        return 50
    else:
        return value

# El siguiente paso, será implementar una nueva función para recorrer cada elemento del diccionario de datos y cada lista del diccionario de datos.

def update_dict(input_dict):
    """
    Función que recibe como parámetro de entrada un diccionario de datos
    y acutaliza sus valores, devolviendo el diccionario actualizado
    
    input 
    input_dict: dict
    
    output
    input_dict: dict
    """
    # Recorremos los campos clave
    for campo_clave in input_dict.keys():
        
        # Obtenemos la lista
        sub_lista = input_dict[campo_clave]
        
        # Recorremos cada valor de la lista
        for item_lista in range(len(sub_lista)):
            # Actualizamos el valor pasando como parámetro de entrada
            # el valor de la lista en cada iteracción
            sub_lista[item_lista] = update_value(value=sub_lista[item_lista])
            
        # Cuando finalizamos la actualización de la lista
        # Sobreescribimos la lista antigua por la nueva
        
        input_dict[campo_clave] = sub_lista
        
    # Devolvemos el diccionario actualizado.
    return input_dict 

    # Definimos una última lista para mostrar por pantalla los precios por el nombre de empresa.

    def show_companies(dict_object): 
        
        for item in dict_object.keys(): 
            print('La empresa {} tiene los siguientes precios {}'.format(item, dict_object[item]))
        
    # No return
    #Programa Principal
    
if __name__ == '__main__':
    clean_dict = update_dict(input_dict = precios)
    show_companies(dict_object=clean_dict)
