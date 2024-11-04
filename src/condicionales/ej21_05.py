#!/usr/bin/env python3

def check_tributar(edad: str, ingresos: str) -> str:
    try:
        edad = int(edad)
        ingresos = float(ingresos)

        if edad >= 16 and ingresos >= 1000:
            return "Debes tributar."
        else:
            return "No hace falta que tributes."
        
    except ValueError:
        return "No has introducido un número!"

def main():
    edad = input("Introduce tu edad: ")
    ingresos = input("Introduce tus ingresos mensuales en euros: ")

    result = check_tributar(edad, ingresos)
    print(result)

if __name__ == '__main__':
    main()