#!/usr/bin/env python3

import os

numero = input("Introduce un número entero positivo: ").replace(' ', '')

if ('.' in numero) or (',' in numero):
    print("Tienes que introducir un número entero.")
    os._exit(0)
else:
    try:
        numero = int(numero)
        num_list = []
        if numero < 0:
            print("ERROR: Tienes que introducir un número positivo.")
            os._exit(0)
        else:
            triangulo = []
            for i in range(numero):
                n = i+1
                dot = ""
                for i in range(n):
                    dot = dot + "*"
                triangulo.append(dot)

            for t in triangulo:
                print(t)

    except ValueError:
        print("ERROR: No has introducido un número!")
        os._exit(0)
