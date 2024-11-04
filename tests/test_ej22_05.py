#!/usr/bin/env python3

import pytest
from src.bucles.ej22_05 import calculadora_inversion

def test_calculadora_inversion():
    # INPUTS VÁLIDOS
    assert calculadora_inversion("1000", "5%", "10") == r"Tu cantidad de dinero despues de 10 años con un 5.0% de interes es: 1628.89"
    assert calculadora_inversion("500", "10%", "5") == r"Tu cantidad de dinero despues de 5 años con un 10.0% de interes es: 805.26"
    assert calculadora_inversion("2000", "3.5%", "7") == r"Tu cantidad de dinero despues de 7 años con un 3.5% de interes es: 2544.56"

    assert calculadora_inversion("0", "5%", "10") == r"Tu cantidad de dinero despues de 10 años con un 5.0% de interes es: 0.0"
    assert calculadora_inversion("1000", "0%", "10") == r"Tu cantidad de dinero despues de 10 años con un 0.0% de interes es: 1000.0"

    # INPUTS INVÁLIDOS
    assert calculadora_inversion("abc", "5%", "10") == "ERROR: No has introducido un número"
    assert calculadora_inversion("1000", "xyz", "10") == "ERROR: No has introducido un número"
    assert calculadora_inversion("1000", "5%", "abc") == "ERROR: No has introducido un número"
    assert calculadora_inversion("", "5%", "10") == "ERROR: No has introducido un número"

if __name__ == '__main__':
    pytest.main()