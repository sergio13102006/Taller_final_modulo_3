import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ejercicio_2 import crear_perfil

class TestCrearPerfil(unittest.TestCase):

    #  --- PRUEBAS CORRECTAS ---
    def test_perfil_completo(self):
        resultado = crear_perfil("Sergio", 23, "Programar", "Jugar", twitter="@sergioklk")
        self.assertIn("Sergio", resultado)
        self.assertIn("23", resultado)
        self.assertIn("Programar, Jugar", resultado)
        self.assertIn("Twitter: @sergioklk", resultado)

    def test_sin_hobbies(self):
        resultado = crear_perfil("Ana", 30, twitter="@ana30")
        self.assertIn("No especificados", resultado)

    def test_sin_redes_sociales(self):
        resultado = crear_perfil("Luis", 20, "Leer", "Bailar")
        self.assertIn("No tiene redes sociales", resultado)

    def test_hobbies_con_espacios(self):
        resultado = crear_perfil("Camila", 27, "  Leer  ", "  Correr ")
        self.assertIn("Leer, Correr", resultado)

    #  --- PRUEBAS DE VALIDACIONES ---
    def test_nombre_vacio(self):
        with self.assertRaises(ValueError):
            crear_perfil("", 25, "Leer")

    def test_nombre_con_numeros(self):
        with self.assertRaises(ValueError):
            crear_perfil("Sergio123", 25, "Jugar")

    def test_edad_negativa(self):
        with self.assertRaises(ValueError):
            crear_perfil("Sergio", -5, "Jugar")

    def test_edad_invalida_tipo(self):
        with self.assertRaises(ValueError):
            crear_perfil("Sergio", "veinte", "Jugar")  # edad debe ser int

    def test_hobby_con_caracteres_especiales(self):
        with self.assertRaises(ValueError):
            crear_perfil("Carlos", 30, "Correr!", "Dormir💤")

    #  --- CASO CON VARIAS REDES SOCIALES ---
    def test_multiples_redes(self):
        resultado = crear_perfil("Laura", 19, "Leer", instagram="@laura19", twitter="@lau19")
        self.assertIn("Instagram: @laura19", resultado)
        self.assertIn("Twitter: @lau19", resultado)


# 🔹 Ejecutar automáticamente los tests y mostrar porcentaje
loader = unittest.defaultTestLoader
suite = loader.loadTestsFromTestCase(TestCrearPerfil)
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

# Calcular porcentaje de éxito
total = result.testsRun
fallas = len(result.failures) + len(result.errors)
exitos = total - fallas
porcentaje = (exitos / total) * 100 if total > 0 else 0

# Mostrar resultados
print("\n RESULTADO FINAL")
print(f"Total de pruebas: {total}")
print(f" Éxitos: {exitos}")
print(f" Fallos: {fallas}")
print(f"Porcentaje de éxito: {porcentaje:.2f}%")

