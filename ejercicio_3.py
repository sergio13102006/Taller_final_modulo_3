def crear_contador():
    """contador independiente """
    conteo = 0  # Variable del ámbito externo

    def incrementar():
        nonlocal conteo  # Permite modificar la variable externa
        conteo += 1
        return conteo

    return incrementar  # Devuelve la función interna


def main():
    # Crear dos contadores independientes
    contador_a = crear_contador()
    contador_b = crear_contador()

    print("Contador A:")
    print(contador_a())  # → 1
    print(contador_a())  # → 2
    print(contador_a())  # → 3

    print("\nContador B:")
    print(contador_b())  # → 1
    print(contador_b())  # → 2

    print("\nContador A sigue independiente:")
    print(contador_a())  # → 4


if __name__ == "__main__":
    main()
