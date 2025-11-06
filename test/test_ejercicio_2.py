import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from ejercicio_2 import crear_perfil


def test_crear_perfil_valido():
    perfil = crear_perfil(
        "Juan Pérez",
        25,
        "leer", "correr",
        twitter="juanp",
        instagram="jp25"
    )

    assert "Nombre: Juan Pérez" in perfil
    assert "Edad: 25" in perfil
    assert "leer, correr" in perfil
    assert "Twitter: juanp" in perfil
    assert "Instagram: jp25" in perfil


def test_crear_perfil_sin_hobbies_ni_redes():
    perfil = crear_perfil("Ana Maria", 30)
    assert "Hobbies: No especificados" in perfil
    assert "No tiene redes sociales" in perfil


def test_nombre_vacio():
    with pytest.raises(ValueError, match="El nombre no puede estar vacío."):
        crear_perfil("", 25)


def test_nombre_con_simbolos():
    with pytest.raises(ValueError, match="El nombre solo debe contener letras y espacios."):
        crear_perfil("Juan123!", 25)


def test_edad_invalida():
    with pytest.raises(ValueError, match="La edad debe ser un número entero positivo."):
        crear_perfil("Carlos", -5)


def test_hobby_invalido():
    with pytest.raises(ValueError, match="Hobby inválido"):
        crear_perfil("Laura", 22, "bailar", "jugar@", "pintar")
