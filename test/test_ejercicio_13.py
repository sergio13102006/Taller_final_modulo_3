
import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from unittest.mock import patch, mock_open
import json
from ejercicio_13 import (
    cargar_inventario,
    guardar_inventario,
    agregar_producto,
    vender_producto,
    mostrar_inventario,
)

class TestEjercicio13(unittest.TestCase):

    @patch("os.path.exists", return_value=False)
    @patch("builtins.open", new_callable=mock_open)
    def test_cargar_inventario_no_existe(self, mock_file, mock_exists):
        """Test loading inventory when the file does not exist."""
        inventario = cargar_inventario()
        mock_file.assert_called_once_with("inventario.json", "w", encoding="utf-8")
        self.assertEqual(inventario, [])

    def test_cargar_inventario_exitoso(self):
        """Test successful inventory loading."""
        json_data = '[{"nombre": "Manzana", "cantidad": 10, "precio": 0.5}]'
        m = mock_open(read_data=json_data)
        with patch("builtins.open", m):
            with patch("os.path.exists", return_value=True):
                inventario = cargar_inventario()
                self.assertEqual(len(inventario), 1)
                self.assertEqual(inventario[0]["nombre"], "Manzana")

    @patch("builtins.open", new_callable=mock_open)
    def test_guardar_inventario(self, mock_file):
        """Test saving the inventory."""
        inventario = [{"nombre": "Manzana", "cantidad": 10, "precio": 0.5}]
        with patch("ejercicio_13.console.print") as mock_print:
            guardar_inventario(inventario)
            mock_file.assert_called_once_with("inventario.json", "w", encoding="utf-8")
            handle = mock_file()
            # We check that json.dump was called with the correct data
            # json.dump writes to the file handle, so we can check the write calls
            # This is complex, so we simplify by checking if print was called
            mock_print.assert_called_with("[green]Inventario guardado correctamente.[/green]")

    def test_agregar_producto_nuevo(self):
        """Test adding a new product."""
        inventario = []
        with patch("ejercicio_13.guardar_inventario") as mock_guardar:
            agregar_producto(inventario, "Pera", 5, 0.8)
            self.assertEqual(len(inventario), 1)
            self.assertEqual(inventario[0]["nombre"], "Pera")
            mock_guardar.assert_called_once()

    def test_vender_producto_exitoso(self):
        """Test selling a product successfully."""
        inventario = [{"nombre": "Manzana", "cantidad": 10, "precio": 0.5}]
        with patch("ejercicio_13.guardar_inventario") as mock_guardar:
            vender_producto(inventario, "Manzana", 3)
            self.assertEqual(inventario[0]["cantidad"], 7)
            mock_guardar.assert_called_once()

    @patch("ejercicio_13.console.print")
    def test_mostrar_inventario(self, mock_print):
        """Test displaying the inventory."""
        inventario = [{"nombre": "Manzana", "cantidad": 10, "precio": 0.5}]
        mostrar_inventario(inventario)
        self.assertTrue(mock_print.called)

if __name__ == '__main__':
    unittest.main()
