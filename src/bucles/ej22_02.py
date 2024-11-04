#!/usr/bin/env python3

try:
    edad = int(input("Introduce tu edad: "))

    print("Has cumplido todos estos años:")
    for i in range(edad):
        n = i+1

        print(n)
except ValueError:
    print("No has introducido un número!")