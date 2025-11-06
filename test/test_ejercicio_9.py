
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functools import reduce
from ejercicio_9 import suma_numeros, concatenar_frase

class TestEjercicio9(unittest.TestCase):

    def test_suma_numeros_positivos(self):
        """Test suma_numeros with positive integers"""
        numeros = [1, 2, 3, 4, 5]
        self.assertEqual(suma_numeros(numeros), 15)

    def test_suma_numeros_negativos(self):
        """Test suma_numeros with negative numbers"""
        numeros = [-1, -2, 3, 4, 5]
        self.assertEqual(suma_numeros(numeros), 9)

    def test_suma_numeros_lista_vacia(self):
        """Test suma_numeros with an empty list"""
        with self.assertRaises(TypeError):
            suma_numeros([])

    def test_suma_numeros_flotantes(self):
        """Test suma_numeros with float numbers"""
        numeros = [1.5, 2.5, 3.0]
        self.assertAlmostEqual(suma_numeros(numeros), 7.0)

    def test_concatenar_frase_normal(self):
        """Test concatenar_frase with a list of strings"""
        frase = ["Hola", " ", "mundo", "!"]
        self.assertEqual(concatenar_frase(frase), "Hola mundo!")

    def test_concatenar_frase_con_strings_vacios(self):
        """Test concatenar_frase with empty strings"""
        frase = ["Hola", "", "mundo"]
        self.assertEqual(concatenar_frase(frase), "Holamundo")

    def test_concatenar_frase_lista_vacia(self):
        """Test concatenar_frase with an empty list"""
        with self.assertRaises(TypeError):
            concatenar_frase([])

if __name__ == '__main__':
    unittest.main()
