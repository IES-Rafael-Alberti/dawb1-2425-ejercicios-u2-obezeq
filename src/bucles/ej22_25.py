#!/usr/bin/env python3

frase = input("Introduce una frase: ").strip()
palabras = frase.split(" ")

lista_palabras = []

for p in palabras:
    p = p.strip()
    if p != "":
        lista_palabras.append(p.strip())

len_max = 0
i = 0

for p in lista_palabras:
    if len(p) >= len_max:
        len_max = int(len(p))
    else:
        i += 1

print(f"La palabra más larga es: {lista_palabras[i]}")