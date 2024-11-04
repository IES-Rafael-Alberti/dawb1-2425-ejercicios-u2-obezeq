#!/usr/bin/env python3

def make_div(n1: str, n2: str) -> str:

    try:
        n1 = float(n1)
        n2 = float(n2)

        if n2 == 0:
            return "ERROR: El divisor no puede ser 0!"
        else:
            division = n1 / n2
            return f"La division de {n1}/{n2} = {division}"
            
    except ValueError:
        return "No has introducido un número!"

def main():

    n1 = input("Introduce el número 1: ")
    n2 = input("Introduce el número 2: ")

    result = make_div(n1, n2)
    print(result)

if __name__ == '__main__':
    main()