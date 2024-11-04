#!/usr/bin/env python3

def calcular_precio(edad: str) -> str:

    try:
        edad = int(edad)

        if edad < 0:
            return "ERROR: Ha habido un problema con tu edad."
        if edad < 4:
            precio = 0
        if edad >= 4 and edad <= 18:
            precio = 5
        if edad > 18:
            precio = 10

        return f"Como tienes {edad} años tienes que pagar: {precio}€."

    except ValueError:
        return "ERROR: No has introducido un número!"

def main():
    edad = int(input("Introduce tu edad: "))

    resultado = calcular_precio(edad)
    print(resultado)

if __name__ == '__main__':
    main()