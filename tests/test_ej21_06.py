#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_06 import check_grupo

def test_check_group():
    # NOMBRES DE MUJER
    assert check_grupo("Ana", "F") == "Eres del grupo: A"
    assert check_grupo("Laura", "F") == "Eres del grupo: A"
    assert check_grupo("María", "F") == "Eres del grupo: B"
    assert check_grupo("Zoe", "F") == "Eres del grupo: B"

    # NOMBRES DE HOMBRE
    assert check_grupo("Miguel", "M") == "Eres del grupo: A"
    assert check_grupo("Luis", "M") == "Eres del grupo: B"
    assert check_grupo("Pedro", "M") == "Eres del grupo: A"
    assert check_grupo("Alberto", "M") == "Eres del grupo: B"

    # INPUT SEXO INVÁLIDO
    assert check_grupo("Carlos", "X") == "ERROR: No has introducido el sexo correcto."
    assert check_grupo("Sofia", "") == "ERROR: No has introducido el sexo correcto."
    assert check_grupo("Javier", "male") == "ERROR: No has introducido el sexo correcto."

    # TEST AMBOS SEXOS
    assert check_grupo("Alba", "F") == "Eres del grupo: A"
    assert check_grupo("Nicolas", "M") == "Eres del grupo: A"


if __name__ == '__main__':
    pytest.main()