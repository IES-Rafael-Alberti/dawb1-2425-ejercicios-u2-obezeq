#!/usr/bin/env python3

try:
    edad = int(input("Introduce tu edad: "))
    ingresos = float(input("Introduce tus ingresos mensuales en euros: "))

    if edad >= 16 and ingresos >= 1000:
        print("Debes tributar.")
    else:
        print("No hace falta que tributes.")

except ValueError:
    print("No has introducido un número!")