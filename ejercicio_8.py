def obtener_palabras_largas(texto):
    """
    Tomamos una lista con plabras que tengan 5 o mas letras y esten en mayuscula
    :param texto: nos da el texto para hacer el ciclo
    :return: nos return
    """
    palabras =texto.upper().split()
    palabras_largas=[]
    for palabra in palabras:
        if len(palabra) > 5:
            palabras_largas.append(palabra)
    return palabras_largas
def contar_longitudes(palabras):
    """
    Creamos un diccionario con una palabra clave para saber su longitud y ese va hacer como el valor

    :param palabras:
    :return:
    """
    longitud={}
    for palabra in palabras:
        longitud[palabra]=len(palabra)
    return longitud
def main():
    texto="""Programacion en Python es una habilidad que se desarrolla con el tiempo y practica"""
    palabras_largas=obtener_palabras_largas(texto)
    print("La palabra es")
    print(palabras_largas)
    diccionario_longitudes=contar_longitudes(palabras_largas)
    print("\nEl diccionario con longitudes de palabras:")
    print(diccionario_longitudes)
if __name__ == "__main__":
    main()