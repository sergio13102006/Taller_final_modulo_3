import unittest
from ejercicio_1 import calcular_imc, interpretar_imc


class TestIMC(unittest.TestCase):
    """
    Pruebas unitarias para las funciones calcular_imc e interpretar_imc.
    """

    def test_calcular_imc(self):
        """
        Verifica que calcular_imc devuelva elpy valor correcto.
        """
        resultado = calcular_imc(70, 1.75)
        self.assertAlmostEqual(resultado, 22.86, places=2)

    def test_interpretar_imc_bajo_peso(self):
        self.assertEqual(interpretar_imc(17.0), "Bajo peso")

    def test_interpretar_imc_normal(self):
        self.assertEqual(interpretar_imc(22.0), "Normal")

    def test_interpretar_imc_sobrepeso(self):
        self.assertEqual(interpretar_imc(27.0), "Sobrepeso")

    def test_interpretar_imc_obesidad(self):
        self.assertEqual(interpretar_imc(31.0), "Obesidad")

    def test_altura_invalida(self):
        with self.assertRaises(ValueError):
            calcular_imc(60, 0)


if __name__ == "__main__":
    unittest.main()
