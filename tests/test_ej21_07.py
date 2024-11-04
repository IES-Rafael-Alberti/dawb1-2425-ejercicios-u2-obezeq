#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_07 import calcular_renta

def test_calcular_renta():
    # INPUTS VÁLIDOS
    assert calcular_renta("5000") == "Tu tipo de impositivo es: 5%"
    assert calcular_renta("15000") == "Tu tipo de impositivo es: 15%"
    assert calcular_renta("25000") == "Tu tipo de impositivo es: 20%"
    assert calcular_renta("40000") == "Tu tipo de impositivo es: 30%"
    assert calcular_renta("70000") == "Tu tipo de impositivo es: 45%"

    # INPUTS INVÁLIDOS
    assert calcular_renta("abc") == "No has introducido un número!"
    assert calcular_renta("") == "No has introducido un número!"
    assert calcular_renta("100.5") == "Tu tipo de impositivo es: 5%"

if __name__ == '__main__':
    pytest.main()