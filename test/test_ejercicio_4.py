import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejercicios')))

from ejercicio_4 import aplicar_validador, es_email_valido, numero_mayor

def test_aplicar_validador_emails_validos():
    datos = ["juan@mail.com", "maria.com", "pedro@mail", "ana@gmail.com"]
    resultado = aplicar_validador(datos, es_email_valido)
    assert resultado == ["juan@mail.com", "ana@gmail.com"]

def test_aplicar_validador_numeros_mayores():
    numeros = [110, 80, 1, 6, 70, 90, 100, 0]
    resultado = aplicar_validador(numeros, numero_mayor)
    assert resultado == [110, 80, 70, 90, 100]

def test_es_email_valido():
    assert es_email_valido("test@mail.com") is True
    assert es_email_valido("testmail.com") is False
    assert es_email_valido("test@mail") is False

def test_numero_mayor():
    assert numero_mayor(11) is True
    assert numero_mayor(10) is False
    assert numero_mayor(-5) is False
