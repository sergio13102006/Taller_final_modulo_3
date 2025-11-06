import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch
from io import StringIO
from ejercicio_10 import explorar_estructura

class TestEjercicio10(unittest.TestCase):

    def test_estructura_compleja(self):
        """Test with a complex nested structure"""
        estructura = [1, [2, 3], {"a": 4, "b": [5, {"c": 6}]}]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            explorar_estructura(estructura)
            output = mock_stdout.getvalue()
            self.assertIn("Valor: 1, Profundidad: 2", output)
            self.assertIn("Valor: 2, Profundidad: 3", output)
            self.assertIn("Valor: 3, Profundidad: 3", output)
            self.assertIn("Valor: 4, Profundidad: 3", output)
            self.assertIn("Valor: 5, Profundidad: 4", output)
            self.assertIn("Valor: 6, Profundidad: 5", output)

    def test_lista_simple(self):
        """Test with a simple list"""
        estructura = [10, 20, 30]
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            explorar_estructura(estructura)
            output = mock_stdout.getvalue()
            self.assertIn("Valor: 10, Profundidad: 2", output)
            self.assertIn("Valor: 20, Profundidad: 2", output)
            self.assertIn("Valor: 30, Profundidad: 2", output)

    def test_diccionario_simple(self):
        """Test with a simple dictionary"""
        estructura = {"x": 100, "y": 200}
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            explorar_estructura(estructura)
            output = mock_stdout.getvalue()
            self.assertIn("Valor: 100, Profundidad: 2", output)
            self.assertIn("Valor: 200, Profundidad: 2", output)

    def test_lista_vacia(self):
        """Test with an empty list"""
        estructura = []
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            explorar_estructura(estructura)
            output = mock_stdout.getvalue()
            self.assertEqual(output, "")

    def test_no_iterable(self):
        """Test with a non-iterable element"""
        estructura = 42
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            explorar_estructura(estructura)
            output = mock_stdout.getvalue()
            self.assertIn("Valor: 42, Profundidad: 1", output)

    def test_con_tuplas_y_sets(self):
        """Test with a structure containing tuples and sets"""
        estructura = (1, {2, 3}, [4, (5,)])
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            explorar_estructura(estructura)
            output = mock_stdout.getvalue()
            self.assertIn("Valor: 1, Profundidad: 2", output)
            self.assertIn("Valor: 2, Profundidad: 3", output)
            self.assertIn("Valor: 3, Profundidad: 3", output)
            self.assertIn("Valor: 4, Profundidad: 3", output)
            self.assertIn("Valor: 5, Profundidad: 4", output)

if __name__ == '__main__':
    unittest.main()
