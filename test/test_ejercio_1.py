import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# from ejercicio_1 import calcular_imc, interpretar_imc
import pytest
from io import StringIO
from contextlib import redirect_stdout
from ejercicio_1 import calcular_imc, interpretar_imc

def test_calcular_imc_correcto():
    # Capturar la salida impresa
    salida = StringIO()
    with redirect_stdout(salida):
        resultado = calcular_imc(70, 1.75)
    salida_texto = salida.getvalue().strip()

    # Verificar resultados
    assert round(resultado, 2) == 22.86
    assert "El IMC es 22.86" in salida_texto

def test_calcular_imc_altura_cero():
    salida = StringIO()
    with redirect_stdout(salida):
        resultado = calcular_imc(70, 0)
    salida_texto = salida.getvalue().strip()

    assert resultado is None
    assert "La altura debe ser mayor que cero." in salida_texto

@pytest.mark.parametrize("imc, esperado", [
    (17.0, "Bajo peso"),
    (22.0, "Estable"),
    (27.0, "Sobrepeso"),
    (32.0, "Obesidad"),
])
def test_interpretar_imc(imc, esperado):
    assert interpretar_imc(imc) == esperado
