
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, mock_open
import json
from ejercicio_15 import (
    cargar_biblioteca,
    guardar_biblioteca,
    prestar_libro,
    devolver_libro,
    buscar_libro,
    ver_libros_prestados,
    mostrar_tabla,
)

class TestEjercicio15(unittest.TestCase):

    def setUp(self):
        """Set up a sample library for testing."""
        self.libros_de_prueba = [
            {"libro_id": "001", "titulo": "Cien Años de Soledad", "prestado_a": None},
            {"libro_id": "002", "titulo": "Don Quijote", "prestado_a": "Juan"},
        ]

    @patch("os.path.exists", return_value=False)
    @patch("ejercicio_15.guardar_biblioteca")
    def test_cargar_biblioteca_no_existe(self, mock_guardar, mock_exists):
        """Test loading the library when the file does not exist."""
        libros = cargar_biblioteca()
        self.assertTrue(mock_guardar.called)
        self.assertEqual(len(libros), 3) # Should return the initial books

    @patch("builtins.open", new_callable=mock_open)
    def test_guardar_biblioteca(self, mock_file):
        """Test saving the library."""
        guardar_biblioteca(self.libros_de_prueba)
        mock_file.assert_called_once_with("biblioteca.json", "w", encoding="utf-8")
        # Further checks could inspect the content written to the file handle

    @patch("ejercicio_15.cargar_biblioteca")
    @patch("ejercicio_15.guardar_biblioteca")
    def test_prestar_libro_exitoso(self, mock_guardar, mock_cargar):
        """Test successfully lending a book."""
        mock_cargar.return_value = self.libros_de_prueba
        with patch("ejercicio_15.console.print") as mock_print:
            prestar_libro("001", "Maria")
            self.assertEqual(self.libros_de_prueba[0]["prestado_a"], "Maria")
            mock_guardar.assert_called_once()

    @patch("ejercicio_15.cargar_biblioteca")
    @patch("ejercicio_15.guardar_biblioteca")
    def test_devolver_libro_exitoso(self, mock_guardar, mock_cargar):
        """Test successfully returning a book."""
        mock_cargar.return_value = self.libros_de_prueba
        with patch("ejercicio_15.console.print") as mock_print:
            devolver_libro("002")
            self.assertIsNone(self.libros_de_prueba[1]["prestado_a"])
            mock_guardar.assert_called_once()

    @patch("ejercicio_15.cargar_biblioteca")
    def test_buscar_libro(self, mock_cargar):
        """Test searching for a book."""
        mock_cargar.return_value = self.libros_de_prueba
        with patch("ejercicio_15.mostrar_tabla") as mock_mostrar:
            resultados = buscar_libro("Quijote")
            self.assertEqual(len(resultados), 1)
            self.assertEqual(resultados[0]["titulo"], "Don Quijote")
            mock_mostrar.assert_called_once()

    @patch("ejercicio_15.cargar_biblioteca")
    def test_ver_libros_prestados(self, mock_cargar):
        """Test viewing loaned books."""
        mock_cargar.return_value = self.libros_de_prueba
        with patch("ejercicio_15.mostrar_tabla") as mock_mostrar:
            prestados = ver_libros_prestados()
            self.assertEqual(len(prestados), 1)
            self.assertEqual(prestados[0]["prestado_a"], "Juan")
            mock_mostrar.assert_called_once()

    @patch("ejercicio_15.console.print")
    def test_mostrar_tabla(self, mock_print):
        """Test displaying the table."""
        mostrar_tabla(self.libros_de_prueba, "Test Table")
        self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
