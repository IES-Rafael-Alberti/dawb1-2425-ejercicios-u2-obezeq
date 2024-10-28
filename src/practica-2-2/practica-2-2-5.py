#!/usr/bin/env python3

try:
    cantidad = float(input("Introduce la cantidad a invertir: "))
    interes = (float(input("Introduce el interés anual (en porcentaje): ").replace('%', '')) / 100) + 1
    anos = int(input("Introduce el número de años: "))

    dinero = cantidad
    for i in range(anos):
        dinero = dinero * interes

    dinero = round(dinero, 2)

    print(f"Tu cantidad de dinero despues de {anos} años con un {interes}% de interes es: {dinero}")

except ValueError:
    print("ERROR: No has introducido un número")