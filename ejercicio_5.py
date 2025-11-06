precio_IVA = 0.19  # variable global
CLAVE_GLOBAL = "clave global"  # clave para permitir cambios

def cambiar_IVA(nuevo_valor: float):
    """Permite modificar la variable global precio_IVA solo si ingresa la clave correcta"""
    clave = input("Ingresa la clave para modificar el IVA: ")
    if clave == CLAVE_GLOBAL:
        global precio_IVA
        precio_IVA = nuevo_valor
        print(f" Nuevo IVA global: {precio_IVA}")
    else:
        print("Clave incorrecta. No se puede modificar el IVA.")

def calcular_IVA(precio: float) -> float:
    """Calcula el IVA usando la variable global"""
    return precio * precio_IVA

def main():
    precio = float(input("Ingresa el precio: "))
    print(f"IVA actual: {calcular_IVA(precio):.2f}")

    # Intento de cambiar el IVA
    nuevo_iva = float(input("Ingresa el nuevo valor de IVA (ej: 0.21): "))
    cambiar_IVA(nuevo_iva)

    # Mostrar el cálculo con el posible nuevo IVA
    print(f"IVA con valor actualizado: {calcular_IVA(precio):.2f}")

if __name__ == "__main__":
    main()
