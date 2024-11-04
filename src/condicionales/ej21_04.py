#!/usr/bin/env python3

def check_par_impar(n: str) -> str:

    try:

        n = float(n)

        if n.is_integer():
            n = int(n)

            if n % 2:
                return f"El número {n} es impar."
            else:
                return f"El número {n} es par."
        else:
            return "El número que has introducido no es entero!"
        
    except ValueError:
        return "El número que has introducido no es entero!"

def main():
    n = input("Introduce un número entero: ")

    result = check_par_impar(n)
    print(result)


if __name__ == '__main__':
    main()