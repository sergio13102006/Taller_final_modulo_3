def filitrar_aprobados(estudiantes):
    """
    Vamos a utilizar los estudiantes que tiene nota mayor o igual a 3.0 usando filter() y
    funcion lambda
    :param estudiantes: son la variable que usamos para entrar y filtrar

    :return: el resultado de estudiantes y la lista filtrada
     """
    aprobados = list(filter(lambda e:e[1]>=3.0,estudiantes))
    return aprobados
def main():
    estudiantes=[
        ("Ana",4.5),
        ("Juan",2.5),
        ("Maria",6.5),
        ("Andres",5.5)
    ]
    estudiantes_aprobados = filitrar_aprobados(estudiantes)
    for nombre,nota in estudiantes_aprobados:
        print(f"{nombre}-nota:{nota}")
if __name__ == "__main__":
    main()
