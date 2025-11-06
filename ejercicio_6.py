def aplicar_descuento(productos):
    """
    tulizar una funcion para aplicar descuento de los productos por un 10%
    :param productos:la variabnle que vamosa utilizar para que entren los productos
    :return:
    """
    precio_descuento =list(map(lambda p: p["precio"]*0.1, productos))
    return precio_descuento
def main():

 productos=[
    {"nombre": "camisa","precio": 5000},
    {"nombre": "zapatos","precio": 1000},
    {"nombre": "pantalon","precio": 2000},
]
 precios_descuento = aplicar_descuento(productos)
 print("El precio con 10% es:")
 for precio in precios_descuento:
     print(f"El precio es: {precio}")
if __name__ == "__main__":
    main()