#!/usr/bin/env python3

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

counter = 0
for l in frase:
    if letra != l:
        print(f"No hay coincidencia en la posición {counter}")
    else:
        print(f"Se ha encontrado coincidencia en la posición {counter}")
        break

    counter += 1