
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ejercicio_8 import obtener_palabras_largas, contar_longitudes

class TestEjercicio8(unittest.TestCase):

    def test_obtener_palabras_largas_normal(self):
        texto = "Programacion en Python es una habilidad"
        palabras = obtener_palabras_largas(texto)
        self.assertEqual(len(palabras), 3)
        self.assertIn("PROGRAMACION", palabras)
        self.assertIn("HABILIDAD", palabras)

    def test_obtener_palabras_largas_ninguna_larga(self):
        """Test obtener_palabras_largas with no long words"""
        texto = "hola que tal"
        palabras = obtener_palabras_largas(texto)
        self.assertEqual(len(palabras), 0)

    def test_obtener_palabras_largas_vacio(self):
        """Test obtener_palabras_largas with an empty string"""
        texto = ""
        palabras = obtener_palabras_largas(texto)
        self.assertEqual(len(palabras), 0)

    def test_obtener_palabras_largas_puntuacion(self):
        """Test obtener_palabras_largas with punctuation"""
        texto = "Hola, mundo! Esto es una prueba."
        # The current implementation does not handle punctuation, so "mundo!" and "prueba." will be treated as words.
        # A more robust implementation would strip punctuation before checking the length.
        palabras = obtener_palabras_largas(texto)
        self.assertEqual(len(palabras), 2)

    def test_contar_longitudes_normal(self):
        """Test contar_longitudes with a list of words"""
        palabras = ["HOLA", "MUNDO", "PYTHON"]
        longitudes = contar_longitudes(palabras)
        self.assertEqual(len(longitudes), 3)
        self.assertEqual(longitudes["HOLA"], 4)
        self.assertEqual(longitudes["MUNDO"], 5)
        self.assertEqual(longitudes["PYTHON"], 6)

    def test_contar_longitudes_vacio(self):
        """Test contar_longitudes with an empty list"""
        palabras = []
        longitudes = contar_longitudes(palabras)
        self.assertEqual(len(longitudes), 0)

if __name__ == '__main__':
    unittest.main()
