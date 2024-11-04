#!/usr/bin/env python3

import pytest
from src.condicionales.ej21_02 import check_pass

def test_check_pass():
    # CONTRASEÑAS CORRECTAS
    assert check_pass("diegoponmeun10") == "La contraseña es correcta: diegoponmeun10"
    
    # CONTRASEÑAS INCORRECTAS
    assert check_pass("password") == "La contraseña no es correcta."
    assert check_pass("Contraseña") == "La contraseña no es correcta."
    assert check_pass("") == "La contraseña no es correcta."
    assert check_pass("123456") == "La contraseña no es correcta."
    assert check_pass("contraseña123") == "La contraseña no es correcta."

if __name__ == '__main__':
    pytest.main()