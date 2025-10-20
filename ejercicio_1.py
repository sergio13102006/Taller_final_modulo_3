def calcular_imc(peso: float, altura: float) -> float:
    """
    Calcula y devuelve el IMC (Índice de Masa Corporal).
    """
    if altura <= 0:
        print("La altura debe ser mayor que cero.")
        return None  # o podrías lanzar un error
    resultado = peso / (altura ** 2)
    print(f"El IMC es {resultado:.2f}")
    return resultado


def interpretar_imc(imc: float) -> str:
    """
    Interpreta el valor del IMC y devuelve una descripción.
    """
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"


def main():
    peso = float(input("Ingrese el peso (kg): "))
    altura = float(input("Ingrese la altura (m): "))
    imc = calcular_imc(peso, altura)
    if imc is not None:
        categoria = interpretar_imc(imc)
        print(f"Resultado ,{categoria}")


if __name__ == "__main__":
    main()
