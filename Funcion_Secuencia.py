secuencia = (1, 89, 54, 98, 45, 23, 32.8, 1.3, 9.5) # No hay limitación de extensión
# Ni del tipo de número (entro o decimal)

print(secuencia)

def sequence_stats(input_secuencia):
    """
    Función que recibe una secuencia de números y devuelve su estadística
    (len, min, max, mean)
    
    input: list
    output: number, number, number, float
    """
    
    # Logitud de la secuencia
    length = len(input_secuencia)
    
    # Valor máximo
    max_value = max(input_secuencia)
    
    # Valor mínimo
    min_value = min(input_secuencia)
    
    # Calculamos la media
    # Primero inicializamos una variable para la suma de los valores
    suma = 0
    
    for item in input_secuencia:
        suma += item # Sumamos a la suma actual el siguiente valor de la secuencia
        
    media = round(suma/length, 2)
    
    return length, min_value, max_value, media

    #Programa Principal

    if __name__ == '__main__':longitud, minimo, maximo, media = sequence_stats(input_secuencia=secuencia)
    print('-'*25)
    print('- La longitud de la secuencia es: {}'.format(longitud))
    print('- El valor mínimo de la secuencia es: {}'.format(minimo))
    print('- El valor máximo de la secuencia es: {}'.format(maximo))
    print('- La valor medio de la secuencia es: {}'.format(media))
    print('-'*25)