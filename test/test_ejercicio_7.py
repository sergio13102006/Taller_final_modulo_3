
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from ejercicio_7 import filitrar_aprobados

class TestEjercicio7(unittest.TestCase):

    def test_filtrar_aprobados_mixto(self):
        """Test filitrar_aprobados with a mixed list of students"""
        estudiantes = [
            ("Ana", 4.5),
            ("Juan", 2.5),
            ("Maria", 3.5),
            ("Andres", 2.9)
        ]
        aprobados = filitrar_aprobados(estudiantes)
        self.assertEqual(len(aprobados), 2)
        self.assertIn(("Ana", 4.5), aprobados)
        self.assertIn(("Maria", 3.5), aprobados)

    def test_filtrar_todos_aprobados(self):
        """Test filitrar_aprobados when all students have passed"""
        estudiantes = [
            ("Ana", 4.5),
            ("Juan", 3.0),
            ("Maria", 3.5),
        ]
        aprobados = filitrar_aprobados(estudiantes)
        self.assertEqual(len(aprobados), 3)

    def test_filtrar_ninguno_aprobado(self):
        """Test filitrar_aprobados when no students have passed"""
        estudiantes = [
            ("Juan", 2.5),
            ("Andres", 2.9)
        ]
        aprobados = filitrar_aprobados(estudiantes)
        self.assertEqual(len(aprobados), 0)

    def test_filtrar_lista_vacia(self):
        """Test filitrar_aprobados with an empty list"""
        estudiantes = []
        aprobados = filitrar_aprobados(estudiantes)
        self.assertEqual(len(aprobados), 0)

    def test_filtrar_nota_exacta(self):
        """Test filitrar_aprobados for students with a grade of 3.0"""
        estudiantes = [
            ("Juan", 3.0),
            ("Andres", 2.9)
        ]
        aprobados = filitrar_aprobados(estudiantes)
        self.assertEqual(len(aprobados), 1)
        self.assertIn(("Juan", 3.0), aprobados)

if __name__ == '__main__':
    unittest.main()
