#!/usr/bin/env python3

def calculadora_inversion(cantidad: str, interes:str, anos: str) -> str:
    

    try:

        cantidad = float(cantidad)
        interes = float(interes.replace('%', ''))
        interes_multi = (interes / 100) + 1
        anos = int(anos)

        dinero = cantidad
        for _ in range(anos):
            dinero = dinero * interes_multi

        dinero = round(dinero, 2)

        return f"Tu cantidad de dinero despues de {anos} años con un {interes}% de interes es: {dinero}"

    except ValueError:
        return "ERROR: No has introducido un número"

def main():

    cantidad = input("Introduce la cantidad a invertir: ")
    interes = input("Introduce el interés anual (en porcentaje): ")
    anos = input("Introduce el número de años: ")

    result = calculadora_inversion(cantidad, interes, anos)
    print(result)

if __name__ == '__main__':
    main()