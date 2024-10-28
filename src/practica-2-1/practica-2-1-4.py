#!/usr/bin/env python3

n = input("Introduce un número entero: ")

if str(float(n)) == f"{n}.0":
    n = int(n)

    if n % 2:
        print(f"El número {n} es par.")
    else:
        print(f"El número {n} es impar.")
else:
    print("El número que has introducido no es entero.")