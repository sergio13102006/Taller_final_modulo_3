from typing import Callable, List

# Función de orden superior
def aplicar_validador(datos: List, validador: Callable) -> List:
    """
    Aplica la función validar a cada elemento de la lista datos.
    Devuelve una nueva lista solo con los elementos que pasaron la validación.
    """
    return [dato for dato in datos if validador(dato)]


# Función de validación 1: verifica si un email es válido (muy básico)
def es_email_valido(email: str) -> bool:
    return "@" in email and "." in email

# Función de validación 2: verifica si un número es mayor a 10
def numero_mayor(numero: int) -> bool:
    return numero > 10


emails = ["juan@mail.com", "maria.com", "pedro@mail", "ana@gmail.com"]
numeros = [110,80,1,6,70,90,100,0]

# Aplicamos el validador de emails
emails_validos = aplicar_validador(emails, es_email_valido)
print("Emails válidos:", emails_validos)

# Aplicamos el validador de números
numeros_mayores = aplicar_validador(numeros, numero_mayor)
print("Números mayores a 10:", numeros_mayores)
