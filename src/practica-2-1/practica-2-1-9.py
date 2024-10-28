#!/usr/bin/env python3

try:
    edad = int(input("Introduce tu edad: "))

    if edad < 4:
        precio = 0
    if edad >= 4 and edad <= 18:
        precio = 5
    if edad > 18:
        precio = 10
    else:
        print("ERROR: Ha habido un problema con tu edad.")

    print(f"Como tienes {edad} años tienes que pagar: {precio}€.")

except ValueError:
    print("ERROR: No has introducido un número!")