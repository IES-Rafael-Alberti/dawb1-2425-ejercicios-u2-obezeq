#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_01 import check_edad

def test_check_edad():
    # EDADES VÁLIDAS
    assert check_edad("0") == "Bienvenido a la tierra."
    assert check_edad("5") == "Eres menor de edad."
    assert check_edad("17") == "Eres menor de edad."
    assert check_edad("18") == "Eres mayor de edad."
    assert check_edad("25") == "Eres mayor de edad."

    # EDADES INVÁLIDAS
    assert check_edad("-1") == "ERROR: No puedes tener menos de 0 años."
    assert check_edad("abc") == "ERROR: No has introducido un número"
    assert check_edad("") == "ERROR: No has introducido un número"
    assert check_edad("3.5") == "ERROR: No has introducido un número"
    assert check_edad("NaN") == "ERROR: No has introducido un número"

if __name__ == '__main__':
    pytest.main()

