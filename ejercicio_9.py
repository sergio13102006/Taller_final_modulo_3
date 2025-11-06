from functools import reduce
def suma_numeros(numeros):
    return reduce(lambda x, y: x + y, numeros)
def concatenar_frase(texto):
    return reduce(lambda x, y: x + y, texto)
def main():
    numeros=[1,2,3,1,4,5]
    suma_total=suma_numeros(numeros)
    print("La suma de los numeros:")
    print(suma_total)
    frase=["Hola"," ","SENA","!"]
    concatenar=concatenar_frase(frase)
    print(f"La frase concatenada es {concatenar}")
if __name__ == '__main__':
    main()
