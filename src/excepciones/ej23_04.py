#!/usr/bin/env python3

try:
    num = int(input("Introduce un número entero: "))
except Exception as e:
    print(f"ERROR: La entrada no es correcta:\n{e}")