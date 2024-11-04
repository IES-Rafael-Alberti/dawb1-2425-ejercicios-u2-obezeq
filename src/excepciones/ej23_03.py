#!/usr/bin/env python3


while True:

    try:
        num = int(input("Introduce un número entero positivo: "))
        if num < 0:
            print("ERROR: ¡No has introducido un número positivo!")
        else:
            break
    except ValueError:
        print("ERROR: ¡No has introducido un número correcto!")


n = num
while n >= 0:
    if n == 0:
        print(n, end = ".")
    else:
        print(n, end = ", ")
        
    n -= 1