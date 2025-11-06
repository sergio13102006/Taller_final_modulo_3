import sys
import os
import pytest
# Agrega la ruta de la carpeta 'ejercicios' al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'ejercicios')))

from ejercicio_3 import crear_contador   # Importa la función desde ejercicios/contador.py


def test_crear_contador_independientes():
    contador_a = crear_contador()
    contador_b = crear_contador()

    # Verifica que cada contador empieza en 1 y aumenta correctamente
    assert contador_a() == 1
    assert contador_a() == 2
    assert contador_a() == 3

    assert contador_b() == 1
    assert contador_b() == 2

    # Verifica que A sigue contando donde iba, no se reinicia
    assert contador_a() == 4


def test_crear_contador_no_comparten_estado():
    contador1 = crear_contador()
    contador2 = crear_contador()

    contador1()
    contador1()
    contador2()

    # contador1 debe ir en 2 y contador2 en 1 → independientes
    assert contador1() == 3
    assert contador2() == 2
