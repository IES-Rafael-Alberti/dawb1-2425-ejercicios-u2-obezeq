#!/usr/bin/env python3

try:
    edad = int(input("Introduce tu edad: "))

    print("Has cumplido todos estos años: ")
    
    for i in range(edad):
        i += 1
        if i == edad:
            print(i, end="")
        else:
            print(i, end=", ")

except ValueError:
    print("ERROR: ¡No has introducido una edad correcta!")