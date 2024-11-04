#!/usr/bin/env python3

"""
GRUPO A:
MUJERES: a-l
HOMBRES: m-z
"""

"""
GRUPO B:
El resto de alumnos
"""

def check_grupo(nombre: str, sexo: str) -> str:

    nombre = str(nombre).lower()
    sexo = sexo.lower().strip().replace(' ', '')

    primera_letra = nombre[0]
    primera_letra_decimal = ord(primera_letra)

    # SEXO FEMENINO
    if sexo == "f":
        if primera_letra_decimal >= 97 and primera_letra_decimal <= 108:
            grupo = "A"
        else:
            grupo = "B"

    # SEXO MASCULINO
    elif sexo == "m":
        if primera_letra_decimal >= 109 and primera_letra_decimal <= 122:
            grupo = "A"
        else:
            grupo = "B"

    # NO SE HA INTRODUCIDO UN SEXO CORRECTO
    else:
        return "ERROR: No has introducido el sexo correcto."

    return f"Eres del grupo: {grupo}"

def main():
    nombre = input("Introduce tu nombre: ")
    sexo = input("Introduce tu sexo (F/M): ")

    result = check_grupo(nombre, sexo)
    print(result)

if __name__ == '__main__':
    main()