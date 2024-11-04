#!/usr/bin/env python3

def calcular_primo(num):
    primo = True
    if num == 1:
        primo = False
    else:
        for i in range(2, num):
            if num % i == 0:
                primo = False

    return primo

contador = 0
while True:
    try:
        num = int(input("Ingresa un número mayor a 1: ").replace(' ', ''))
        if num == 0:
            break
        elif num < 1 and num != 0:
            print("ERROR: No has introducido un número mayor a 1")
        else:
            if calcular_primo(num):
                contador += 1
    except ValueError:
        print("ERROR: No has introducido un número.")

print(f"Has ingresado {contador} números primos.")