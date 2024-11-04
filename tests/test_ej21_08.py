#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_08 import calcular_rendimiento

def test_calcular_rendimiento():
    # INPUTS VÁLIDOS
    assert calcular_rendimiento("0.0") == "Tu nivel de rendimiento es 0.0 y has conseguido: 0.0€"
    assert calcular_rendimiento("0.4") == "Tu nivel de rendimiento es 0.4 y has conseguido: 960.0€"
    assert calcular_rendimiento("0.6") == "Tu nivel de rendimiento es 0.6 y has conseguido: 1440.0€"
    assert calcular_rendimiento("1.0") == "Tu nivel de rendimiento es 1.0 y has conseguido: 2400.0€"

    # INPUTS RENDIMIENTOS NO MENCIONADO
    assert calcular_rendimiento("0.5") == "ERROR: Tienes que poner alguna de las puntuaciones mencionadas."
    assert calcular_rendimiento("0.3") == "ERROR: Tienes que poner alguna de las puntuaciones mencionadas."
    assert calcular_rendimiento("0.59") == "ERROR: Tienes que poner alguna de las puntuaciones mencionadas."

    # INPUTS INVÁLIDOS
    assert calcular_rendimiento("abc") == "ERROR: No has introducido un nivel de rendimiento correcto."
    assert calcular_rendimiento("") == "ERROR: No has introducido un nivel de rendimiento correcto."
    assert calcular_rendimiento("2.0") == "Tu nivel de rendimiento es 2.0 y has conseguido: 4800.0€"

if __name__ == '__main__':
    pytest.main()