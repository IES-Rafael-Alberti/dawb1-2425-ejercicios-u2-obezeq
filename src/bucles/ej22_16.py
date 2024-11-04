#!/usr/bin/env python3

list = []

while True:
    n = input("Introduce un número: ")

    try:
        if float(n) == 0:
            break
        else:
            if float(n) > 0:
                list.append(float(n))

    except ValueError:
        print("ERROR: No has introducido un número!")

mayor = max(list)

if mayor.is_integer():
    suma = int(mayor)

print(f"El número mayor introducido es: {mayor}")