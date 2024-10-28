#!/usr/bin/env python3

print("──────────────────────────────────")
print("INTRODUCE TU NIVEL DE RENDIMIENTO:")
print("──────────────────────────────────")
print("Inaceptable: 0.0")
print("Inaceptable: 0.4")
print("Inaceptable: 0.6 o más")
print("──────────────────────────────────")

try:
    rendimiento = float(input("~> "))

    if rendimiento == 0.0 or rendimiento == 0.4 or rendimiento >= 0.6:
        dinero = round((rendimiento * 2400), 2)
        print(f"Tu nivel de rendimiento es {rendimiento} y has conseguido: {dinero}€")
    else:
        print("ERROR: Tienes que poner alguna de las puntuaciones mencionadas.")

except ValueError:
    print("ERROR: No has introducido un nivel de rendimiento correcto.")