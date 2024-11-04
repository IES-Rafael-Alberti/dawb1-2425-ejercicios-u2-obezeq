#!/usr/bin/env python3

import os

num = input("Introduce un número entero: ")

try:
    if num.isdigit():
        num = int(num)

        list = []
        n = 0 if num % 2 == 0 else 1

        while n <= num:
            list.append(n)
            for i in list[::-1]:
                print(i, end=" ")
            print()
            n += 2

    else:
        print("ERROR: No has introducido un número entero.")
        os._exit(0)
except ValueError:
    print("ERROR: No has introducido un número!")