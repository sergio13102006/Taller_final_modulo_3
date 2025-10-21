import unittest
from ejercicio_1 import calcular_imc, interpretar_imc


class TestIMC(unittest.TestCase):
    """
    Pruebas unitarias para las funciones calcular_imc e interpretar_imc.
    """

    # -------------------------------
    # Pruebas para calcular_imc
    # -------------------------------
    def test_calcular_imc_valor_correcto(self):
        """Debe devolver el valor correcto con datos válidos."""
        resultado = calcular_imc(50, 1.75)
        self.assertAlmostEqual(resultado, 22.86, places=2)

    def test_calcular_imc_redondeo(self):
        """Verifica el redondeo del IMC con más decimales."""
        resultado = calcular_imc(68, 1.72)
        self.assertAlmostEqual(resultado, 22.99, places=2)

    def test_calcular_imc_altura_cero(self):
        """Debe lanzar ValueError si la altura es cero."""
        with self.assertRaises(ValueError):
            calcular_imc(60, 0)

    def test_calcular_imc_altura_negativa(self):
        """Debe lanzar ValueError si la altura es negativa."""
        with self.assertRaises(ValueError):
            calcular_imc(70, -1.7)

    def test_calcular_imc_peso_negativo(self):
        """Debe lanzar ValueError si el peso es negativo."""
        with self.assertRaises(ValueError):
            calcular_imc(-65, 1.75)

    # -------------------------------
    # Pruebas para interpretar_imc
    # -------------------------------
    def test_interpretar_imc_bajo_peso(self):
        self.assertEqual(interpretar_imc(17.0), "Bajo peso")

    def test_interpretar_imc_normal(self):
        self.assertEqual(interpretar_imc(22.0), "Normal")

    def test_interpretar_imc_sobrepeso(self):
        self.assertEqual(interpretar_imc(27.0), "Sobrepeso")

    def test_interpretar_imc_obesidad(self):
        self.assertEqual(interpretar_imc(31.0), "Obesidad")

    def test_interpretar_imc_limites(self):
        """Verifica que los valores límite se interpreten correctamente."""
        casos = [
            (18.4, "Bajo peso"),
            (18.5, "Normal"),
            (24.9, "Normal"),
            (25.0, "Sobrepeso"),
            (29.9, "Sobrepeso"),
            (30.0, "Obesidad"),
        ]
        for imc, esperado in casos:
            with self.subTest(imc=imc):
                self.assertEqual(interpretar_imc(imc), esperado)


if __name__ == "__main__":
    unittest.main()
