from typing import Any

def explorar_estructura(elemento: Any, profundidad: int = 1) -> None:
    """
    Función recursiva que explora estructuras de datos anidadas
    (listas, tuplas, diccionarios, sets) e imprime los valores
    no iterables junto con su nivel de profundidad.
    """

    # Si es un diccionario, recorremos sus valores
    if isinstance(elemento, dict):
        for valor in elemento.values():
            explorar_estructura(valor, profundidad + 1)

    # Si es una lista, tupla o conjunto, recorremos sus elementos
    elif isinstance(elemento, (list, tuple, set)):
        for item in elemento:
            explorar_estructura(item, profundidad + 1)

    # Caso base: no es iterable → imprimimos el valor
    else:
        print(f"Valor: {elemento}, Profundidad: {profundidad}")


# -----------------------------
# 🔥 Bloque principal del programa
# -----------------------------
if __name__ == "__main__":
    # Estructura de ejemplo
    estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]

    print("Explorando estructura...\n")
    explorar_estructura(estructura)
