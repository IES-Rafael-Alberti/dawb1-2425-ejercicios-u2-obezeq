#!/usr/bin/env python3

contrasena_og = "DiegoPonmeUn10"
contrasena = input("Introduce contraseña: ")

try:
    if contrasena != contrasena_og:
        raise NameError
    else:
        print("Contraseña correcta :D")
except NameError:
    print("Incorrect Password!!")