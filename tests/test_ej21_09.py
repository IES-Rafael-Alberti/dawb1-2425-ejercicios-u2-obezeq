#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_09 import calcular_precio

def test_calcular_precio():
    # INPUTS VÁLIDOS
    assert calcular_precio("0") == "Como tienes 0 años tienes que pagar: 0€."
    assert calcular_precio("3") == "Como tienes 3 años tienes que pagar: 0€."
    assert calcular_precio("4") == "Como tienes 4 años tienes que pagar: 5€."
    assert calcular_precio("10") == "Como tienes 10 años tienes que pagar: 5€."
    assert calcular_precio("18") == "Como tienes 18 años tienes que pagar: 5€."
    assert calcular_precio("19") == "Como tienes 19 años tienes que pagar: 10€."
    assert calcular_precio("30") == "Como tienes 30 años tienes que pagar: 10€."
    assert calcular_precio("-1") == "ERROR: Ha habido un problema con tu edad."

    # INPUTS INVÁLIDOS
    assert calcular_precio("abc") == "ERROR: No has introducido un número!"
    assert calcular_precio("") == "ERROR: No has introducido un número!"

if __name__ == '__main__':
    pytest.main()