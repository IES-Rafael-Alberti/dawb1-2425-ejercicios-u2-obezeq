#!/usr/bin/env python3

lineas = 0
digitos = 0

while True:
    libro = input("Libro: ").strip()

    if libro == "*":
        break

    elif libro == "/":
        print(f"Linea completa. Aparecen {digitos} dígitos numéricos.")
        digitos = 0
        lineas += 1

    else:
        for p in libro:
            if p.isdigit():
                digitos += 1


print(f"Fin. Se leyeron {lineas} líneas completas.")