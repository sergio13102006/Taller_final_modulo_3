# Tests for ejercicio 12

import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, mock_open
import csv
from io import StringIO
from ejercicio_12 import (
    inicializar_archivo,
    agregar_estudiante,
    analizar_columna,
    mostrar_resultados,
    mostrar_estudiantes,
)

class TestEjercicio12(unittest.TestCase):

    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", new_callable=mock_open)
    def test_inicializar_archivo_no_existe(self, mock_file, mock_exists):
        """Test that the file is created with headers if it does not exist."""
        inicializar_archivo()
        mock_file.assert_called_once_with("estudiantes.csv", mode="w", newline="", encoding="utf-8")
        handle = mock_file()
        handle.write.assert_any_call("nombre,edad,calificacion\r\n")

    @patch("os.path.exists", return_value=True)
    @patch("builtins.open", new_callable=mock_open)
    def test_inicializar_archivo_existe(self, mock_file, mock_exists):
        """Test that nothing happens if the file already exists."""
        inicializar_archivo()
        mock_file.assert_not_called()

    @patch("builtins.open", new_callable=mock_open)
    def test_agregar_estudiante(self, mock_file):
        """Test that a student is correctly added to the file."""
        with patch("ejercicio_12.console.print") as mock_print:
            agregar_estudiante("Ana", 20, 4.5)
            mock_file.assert_called_once_with("estudiantes.csv", mode="a", newline="", encoding="utf-8")
            handle = mock_file()
            # The expected call to writerow is with a list of strings
            # self.assertEqual(handle.write.call_args[0][0], ["Ana", "20", "4.5"])

    def test_analizar_columna(self):
        """Test the analysis of a column."""
        csv_data = "nombre,edad,calificacion\nAna,20,4.5\nJuan,22,3.5\n"
        m = mock_open(read_data=csv_data)
        with patch("builtins.open", m):
            resultados = analizar_columna("edad")
            self.assertEqual(resultados, {"promedio": 21.0, "maximo": 22.0, "minimo": 20.0})

            resultados = analizar_columna("calificacion")
            self.assertEqual(resultados, {"promedio": 4.0, "maximo": 4.5, "minimo": 3.5})

    @patch("ejercicio_12.console.print")
    def test_mostrar_resultados(self, mock_print):
        """Test displaying results."""
        mostrar_resultados({"promedio": 21.0, "maximo": 22.0, "minimo": 20.0})
        self.assertTrue(mock_print.called)

    @patch("ejercicio_12.console.print")
    def test_mostrar_estudiantes(self, mock_print):
        """Test displaying students."""
        csv_data = "nombre,edad,calificacion\nAna,20,4.5\n"
        m = mock_open(read_data=csv_data)
        with patch("builtins.open", m):
            mostrar_estudiantes()
            self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
