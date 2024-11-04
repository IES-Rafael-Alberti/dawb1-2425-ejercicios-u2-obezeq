#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_04 import check_par_impar

def test_check_par_impar():
    # TEST NÚMEROS PARES
    assert check_par_impar("2") == "El número 2 es par."
    assert check_par_impar("4") == "El número 4 es par."
    assert check_par_impar("0") == "El número 0 es par."

    # TEST NUMEROS IMPARES
    assert check_par_impar("1") == "El número 1 es impar."
    assert check_par_impar("3") == "El número 3 es impar."
    assert check_par_impar("99") == "El número 99 es impar."

    # TEST INPUTS INVALIDOS
    assert check_par_impar("abc") == "El número que has introducido no es entero!"
    assert check_par_impar("3.5") == "El número que has introducido no es entero!"
    assert check_par_impar("") == "El número que has introducido no es entero!"
    assert check_par_impar("10.0") == "El número 10 es par."

if __name__ == '__main__':
    pytest.main()