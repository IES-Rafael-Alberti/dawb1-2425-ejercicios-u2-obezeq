#!/usr/bin/env python3

try:
    n1 = float(input("Introduce el número 1: "))
    n2 = float(input("Introduce el número 2: "))

    if n2 == 0:
        print("ERROR: El divisor no puede ser 0!")
    else:
        division = n1 / n2
        print(f"La division de {n1}/{n2} = {division}")
        
except ValueError:
    print("No has introducido un número!")