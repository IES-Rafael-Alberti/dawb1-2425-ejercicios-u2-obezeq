#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_05 import check_tributar

def test_check_tributar():
    # NECESITA TRIBUTAR
    assert check_tributar("16", "1000") == "Debes tributar."
    assert check_tributar("20", "1500") == "Debes tributar."
    assert check_tributar("30", "2000") == "Debes tributar."

    # NO NECESITA TRIBUTAR
    assert check_tributar("15", "1000") == "No hace falta que tributes."
    assert check_tributar("16", "500") == "No hace falta que tributes."
    assert check_tributar("30", "500") == "No hace falta que tributes."
    assert check_tributar("10", "0") == "No hace falta que tributes."

    # INPUTS INVÁLIDOS
    assert check_tributar("abc", "1000") == "No has introducido un número!"
    assert check_tributar("16", "xyz") == "No has introducido un número!"
    assert check_tributar("", "1000") == "No has introducido un número!"
    assert check_tributar("16", "") == "No has introducido un número!"

if __name__ == '__main__':
    pytest.main()