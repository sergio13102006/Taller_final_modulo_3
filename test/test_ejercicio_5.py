import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import ejercicio_5

class TestEjercicio5(unittest.TestCase):

    def setUp(self):
        """Set up for tests"""
        self.initial_IVA = 0.19
        # Reset precio_IVA to its initial value before each test
        ejercicio_5.precio_IVA = self.initial_IVA

    def test_calcular_IVA_default(self):
        """Test calcular_IVA with the default IVA"""
        self.assertAlmostEqual(ejercicio_5.calcular_IVA(100), 19.0)

    @patch('builtins.input', return_value=ejercicio_5.CLAVE_GLOBAL)
    def test_cambiar_IVA_clave_correcta(self, mock_input):
        """Test changing IVA with the correct key"""
        nuevo_iva = 0.21
        with patch('sys.stdout', new=StringIO()) as fake_out:
            ejercicio_5.cambiar_IVA(nuevo_iva)
            self.assertIn(f"Nuevo IVA global: {nuevo_iva}", fake_out.getvalue().strip())
        self.assertEqual(ejercicio_5.precio_IVA, nuevo_iva)

    @patch('builtins.input', return_value="clave incorrecta")
    def test_cambiar_IVA_clave_incorrecta(self, mock_input):
        """Test changing IVA with an incorrect key"""
        nuevo_iva = 0.21
        with patch('sys.stdout', new=StringIO()) as fake_out:
            ejercicio_5.cambiar_IVA(nuevo_iva)
            self.assertIn("Clave incorrecta. No se puede modificar el IVA.", fake_out.getvalue().strip())
        self.assertEqual(ejercicio_5.precio_IVA, self.initial_IVA)

    @patch('builtins.input', return_value=ejercicio_5.CLAVE_GLOBAL)
    def test_calcular_IVA_despues_de_cambio(self, mock_input):
        """Test calcular_IVA after the IVA has been changed"""
        nuevo_iva = 0.25
        ejercicio_5.cambiar_IVA(nuevo_iva)
        self.assertAlmostEqual(ejercicio_5.calcular_IVA(100), 25.0)

if __name__ == '__main__':
    unittest.main()