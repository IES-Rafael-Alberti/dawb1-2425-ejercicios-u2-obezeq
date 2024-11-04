#!/usr/bin/env python3

def check_edad(edad: str) -> str:

    try:
        edad = int(edad)

        if edad < 0:
            return "ERROR: No puedes tener menos de 0 años."
        
        elif edad == 0:
            return "Bienvenido a la tierra."

        elif edad > 0 and edad < 18:
            return "Eres menor de edad."

        elif edad >= 18:
            return "Eres mayor de edad."

    except Exception:
        return "ERROR: No has introducido un número"

def main():
    edad = input("Introduce tu edad: ")
    result = check_edad(edad)
    print(result)

if __name__ == '__main__':
    main()