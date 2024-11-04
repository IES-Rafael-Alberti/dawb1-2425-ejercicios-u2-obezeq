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

suma = 0
for n in list:
    suma += n

if suma.is_integer():
    suma = int(suma)

print(f"La suma de todos los números que has introducido es: {suma}")