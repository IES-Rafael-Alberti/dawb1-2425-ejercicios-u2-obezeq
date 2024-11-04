#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_03 import make_div

def test_make_div():
    # DIVISIONES VÁLIDAS
    assert make_div("10", "2") == "La division de 10.0/2.0 = 5.0"
    assert make_div("9", "3") == "La division de 9.0/3.0 = 3.0"
    assert make_div("5", "2.5") == "La division de 5.0/2.5 = 2.0"
    
    # DIVISIÓN POR 0
    assert make_div("10", "0") == "ERROR: El divisor no puede ser 0!"
    
    # DIVISIÓN INVÁLIDAS
    assert make_div("abc", "2") == "No has introducido un número!"
    assert make_div("10", "xyz") == "No has introducido un número!"
    assert make_div("", "5") == "No has introducido un número!"
    assert make_div("10", "") == "No has introducido un número!"
    assert make_div("3.5", "0.5") == "La division de 3.5/0.5 = 7.0"

if __name__ == '__main__':
    pytest.main()