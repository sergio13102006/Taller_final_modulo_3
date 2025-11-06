
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ejercicio_6 import aplicar_descuento

class TestEjercicio6(unittest.TestCase):

    def test_aplicar_descuento_lista_productos(self):
        """Test aplicar_descuento with a list of products"""
        productos = [
            {"nombre": "camisa", "precio": 5000},
            {"nombre": "zapatos", "precio": 1000},
            {"nombre": "pantalon", "precio": 2000},
        ]
        precios_descuento = aplicar_descuento(productos)
        self.assertEqual(len(precios_descuento), 3)
        self.assertAlmostEqual(precios_descuento[0], 500.0)
        self.assertAlmostEqual(precios_descuento[1], 100.0)
        self.assertAlmostEqual(precios_descuento[2], 200.0)

    def test_aplicar_descuento_lista_vacia(self):
        """Test aplicar_descuento with an empty list"""
        productos = []
        precios_descuento = aplicar_descuento(productos)
        self.assertEqual(len(precios_descuento), 0)

    def test_aplicar_descuento_precio_cero(self):
        """Test aplicar_descuento with a product with price 0"""
        productos = [
            {"nombre": "camisa", "precio": 0},
        ]
        precios_descuento = aplicar_descuento(productos)
        self.assertEqual(len(precios_descuento), 1)
        self.assertAlmostEqual(precios_descuento[0], 0.0)

    def test_aplicar_descuento_con_numeros_flotantes(self):
        """Test aplicar_descuento with floating point prices"""
        productos = [
            {"nombre": "camisa", "precio": 50.5},
            {"nombre": "zapatos", "precio": 10.25},
        ]
        precios_descuento = aplicar_descuento(productos)
        self.assertEqual(len(precios_descuento), 2)
        self.assertAlmostEqual(precios_descuento[0], 5.05)
        self.assertAlmostEqual(precios_descuento[1], 1.025)

if __name__ == '__main__':
    unittest.main()
