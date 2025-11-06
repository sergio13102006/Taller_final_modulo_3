import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, mock_open
from io import StringIO
from ejercicio_11 import agregar_tarea, ver_tarea, mostrar_tarea
class TestEjercicio11(unittest.TestCase):

    @patch("ejercicio_11.archivo_tareas", "test_tareas.txt")
    def test_agregar_y_ver_tareas(self):
        """Test adding and then viewing tasks"""
        # Mock the open function
        m = mock_open()
        with patch("builtins.open", m):
            # Add a task
            agregar_tarea("Comprar pan")
            # Check if the file was written to correctly
            m().write.assert_called_once_with("Comprar pan\n")

        # Now, test reading
        # Prepare the mock to simulate the file content
        m = mock_open(read_data="Comprar pan\nLavar ropa\n")
        with patch("builtins.open", m):
            tareas = ver_tarea()
            self.assertEqual(tareas, ["Comprar pan", "Lavar ropa"])

    def test_ver_tareas_archivo_no_encontrado(self):
        """Test viewing tasks when the file does not exist"""
        # mock_open by default will raise a FileNotFoundError if the file is not "known"
        m = mock_open()
        m.side_effect = FileNotFoundError
        with patch("builtins.open", m):
            tareas = ver_tarea()
            self.assertEqual(tareas, [])

    @patch('ejercicio_11.ver_tarea', return_value=[])
    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_tarea_sin_tareas(self, mock_stdout, mock_ver_tarea):
        """Test showing tasks when there are none"""
        mostrar_tarea()
        self.assertIn("No hay tareas registradas", mock_stdout.getvalue())

    @patch('ejercicio_11.ver_tarea', return_value=["Tarea 1", "Tarea 2"])
    @patch('rich.console.Console.print')
    def test_mostrar_tarea_con_tareas(self, mock_print, mock_ver_tarea):
        """Test showing tasks when there are tasks"""
        mostrar_tarea()
        # We expect the table to be printed. A simple check is to see if the mock was called.
        self.assertTrue(mock_print.called)
        # A more detailed check could be to inspect the arguments passed to print
        # For example, check if the table title is present in the printed output
        # This is complex with rich, so we keep it simple.
        args, kwargs = mock_print.call_args
        self.assertIn("Lista de Tareas", str(args[0].title))


if __name__ == '__main__':
    unittest.main()

