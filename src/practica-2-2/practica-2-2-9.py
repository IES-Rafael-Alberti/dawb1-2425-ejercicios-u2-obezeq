#!/usr/bin/env python3

contrasena_correcta = "Dieg@PonmeUn10"
contrasena = None

while contrasena != contrasena_correcta:
    contrasena = input("[+] Introduce una contraseña: ")
    if contrasena != contrasena_correcta:
        print("[-] No has introducido la contraseña correcta!\n")
    else:
        print("Contraseña correcta :D\n")