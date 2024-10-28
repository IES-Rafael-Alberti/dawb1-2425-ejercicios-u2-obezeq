#!/usr/bin/env python3

import os

numero = input("Introduce un número entero positivo: ").replace(' ', '')

if ('.' in numero) or (',' in numero):
    print("Tienes que introducir un número entero.")
    os._exit(0)
else:
    try:
        numero = int(numero)
        if numero < 0:
            print("ERROR: Tienes que introducir un número positivo.")
            os._exit(0)
        else:
            impares = []
            for i in range(numero):
                n = i + 1
                if n % 2 != 0:
                    impares.append(n)

            print("Los años impares desde que naciste hasta tu edad son:")
            print(str(impares).replace('[', '').replace(']', ''))

    except ValueError:
        print("ERROR: No has introducido un número!")
        os._exit(0)
