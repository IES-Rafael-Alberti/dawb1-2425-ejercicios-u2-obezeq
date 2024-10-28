#!/usr/bin/env python3

try:
    num = int(input("Introduce un número entero positivo: "))
    if num < 0:
        print("ERROR: ¡No has introducido un número positivo!")
    else:
        print(f"Todos los números impares desde el 1 hasta el {num} son: ")
        for i in range(num):
            i += 1
            if i % 2 != 0:
                if i == num or i == (num-1):
                    print(i, end = ".")
                else:
                    print(i, end = ", ")
except ValueError:
    print("ERROR: ¡No has introducido un número!")