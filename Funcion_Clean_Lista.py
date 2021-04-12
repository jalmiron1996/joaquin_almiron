# Escriba un programa que, partiendo de las dos siguientes listas con nombres, borre a la lista 1 los nombres de la lista 2

lista_uno = ['Mario', 'Paula', 'David', 'Ana', 'Jorge', 'Ivan', 'Laura', 'Beatriz']
lista_dos = ['Paula', 'Francisco', 'Jorge', 'Juan', 'David']

# La forma más directa es utilizar la función .remove() ya que simplemente iremos borrando cada coincidencia, si el nombre no está en la lista 1, no hacemos nada

def clean_names(list_one, list_two):
    """
    Función que recibe dos listas y devuelve la priemera lista
    sin las coincidencias de la segunda
    
    input
    list_one: list
    list_two: list
    
    output
    list_one: list
    """
    for item in list_two:
        if item in list_one:
            list_one.remove(item)
        else:
            pass
       
    return list_one

    #Programa principal

    if __name__ == '__main__': lista_limpia = clean_names(list_one=lista_uno, list_two=lista_dos)
    # Limpiamos la lista 
    print('Lista limpia: ', lista_limpia)
