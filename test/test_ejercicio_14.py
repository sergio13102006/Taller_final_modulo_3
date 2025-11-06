

import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, mock_open
import json
import csv
from io import StringIO
# There is a typo in the source file name
from ejercicio_14 import (
    inicializar_archivos,
    leer_csv,
    leer_json,
    generar_reporte,
    guardar_reporte,
    mostrar_reporte_con_rich,
)

class TestEjercicio14(unittest.TestCase):

    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", new_callable=mock_open)
    def test_inicializar_archivos(self, mock_file, mock_exists):
        """Test that files are created if they do not exist."""
        inicializar_archivos()
        # Check that both files are created
        mock_file.assert_any_call("estudiantes.csv", mode="w", newline="", encoding="utf-8")
        mock_file.assert_any_call("cursos.json", mode="w", encoding="utf-8")

    def test_leer_csv(self):
        """Test reading a CSV file."""
        csv_data = "id,nombre\n1,Ana\n2,Juan\n"
        m = mock_open(read_data=csv_data)
        with patch("builtins.open", m):
            estudiantes = leer_csv("dummy.csv")
            self.assertEqual(estudiantes, {1: "Ana", 2: "Juan"})

    def test_leer_json(self):
        """Test reading a JSON file."""
        json_data = '[{"id_estudiante": 1, "curso": "Python"}]'
        m = mock_open(read_data=json_data)
        with patch("builtins.open", m):
            cursos = leer_json("dummy.json")
            self.assertEqual(len(cursos), 1)
            self.assertEqual(cursos[0]["curso"], "Python")

    def test_generar_reporte(self):
        """Test report generation."""
        estudiantes = {1: "Ana", 2: "Juan"}
        cursos = [{"id_estudiante": 1, "curso": "Python"}, {"id_estudiante": 2, "curso": "Java"}]
        reporte = generar_reporte(estudiantes, cursos)
        self.assertIn("Ana:", reporte)
        self.assertIn("- Python", reporte)
        self.assertIn("Juan:", reporte)
        self.assertIn("- Java", reporte)

    @patch("builtins.open", new_callable=mock_open)
    def test_guardar_reporte(self, mock_file):
        """Test saving the report."""
        contenido = "Este es el contenido del reporte."
        with patch("ejercicio_14.console.print") as mock_print:
            guardar_reporte("reporte.txt", contenido)
            mock_file.assert_called_once_with("reporte.txt", mode="w", encoding="utf-8")
            mock_file().write.assert_called_once_with(contenido)

    @patch("ejercicio_14.console.print")
    def test_mostrar_reporte_con_rich(self, mock_print):
        """Test displaying the report with rich."""
        contenido = "Contenido de prueba"
        mostrar_reporte_con_rich(contenido)
        self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
