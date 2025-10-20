def crear_perfil(nombre: str, edad: int, *hobbies: str, **redes_sociales: str) -> str:
    """
    Genera un perfil de usuario con su nombre, edad, hobbies y redes sociales.

    Parámetros:
        nombre (str): Nombre del usuario. Solo puede contener letras y espacios.
        #edad (int): Edad del usuario. Debe ser un número positivo.
        *hobbies (str): Lista variable de hobbies del usuario.
        **redes_sociales (str): Redes sociales con el formato red=usuario.

    Retorna:
        str: Cadena con la información del perfil formateada.
    """

    #  Validaciones básicas
    if not nombre.strip():
        raise ValueError("El nombre no puede estar vacío.")
    if not all(c.isalpha() or c.isspace() for c in nombre):
        raise ValueError("El nombre solo debe contener letras y espacios.")
    if not isinstance(edad, int) or edad <= 0:
        raise ValueError("La edad debe ser un número entero positivo.")

    #  Limpiar hobbies (quitar espacios y validar caracteres)
    hobbies_limpios = []
    for h in hobbies:
        limpio = h.strip()
        if limpio and all(c.isalnum() or c.isspace() for c in limpio):
            hobbies_limpios.append(limpio)
        elif limpio:
            raise ValueError(f"Hobby inválido: '{h}'. No debe contener símbolos especiales.")

    hobbies_str = ", ".join(hobbies_limpios) if hobbies_limpios else "No especificados"

    #  Formatear redes sociales
    if redes_sociales:
        redes_str = "\n".join([f"{k.capitalize()}: {v}" for k, v in redes_sociales.items()])
    else:
        redes_str = "No tiene redes sociales."

    #  Devolver perfil formateado
    perfil = (
        f" PERFIL DE USUARIO\n"
        f"Nombre: {nombre}\n"
        f"Edad: {edad}\n"
        f"Hobbies: {hobbies_str}\n"
        f"Redes Sociales:\n{redes_str}"
    )

    return perfil


def main():
    """Función principal que pide datos al usuario y muestra su perfil."""

    print("=== CREAR PERFIL DE USUARIO ===")

    # Pedir nombre y edad
    nombre = input("Ingresa tu nombre: ").strip()
    while not nombre:
        print(" El nombre no puede estar vacío.")
        nombre = input("Ingresa tu nombre: ").strip()

    try:
        edad = int(input("Ingresa tu edad: "))
        if edad <= 0:
            raise ValueError
    except ValueError:
        print(" Edad inválida. Debe ser un número entero positivo.")
        return

    # Pedir hobbies
    hobbies = input("Escribe tus hobbies separados por comas (ej: leer, correr, jugar): ").split(",")
    hobbies = [h.strip() for h in hobbies if h.strip()]

    # Pedir redes sociales
    twitter = input("Usuario de Twitter (opcional): ").strip()
    instagram = input("Usuario de Instagram (opcional): ").strip()

    redes = {}
    if twitter:
        redes["twitter"] = twitter
    if instagram:
        redes["instagram"] = instagram

    try:
        # Crear y mostrar el perfil
        perfil = crear_perfil(nombre, edad, *hobbies, **redes)
        print("\n" + perfil)
    except ValueError as e:
        print(f" Error: {e}")


# 🔹 Ejecutar solo si se corre directamente
if __name__ == "__main__":
    main()
