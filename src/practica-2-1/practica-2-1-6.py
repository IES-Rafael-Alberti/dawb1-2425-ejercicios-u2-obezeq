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

nombre = str(input("Introduce tu nombre: ").lower())

primera_letra = nombre[0]
primera_letra_decimal = ord(primera_letra)

sexo = input("Introduce tu sexo (F/M): ").lower().replace(" ", "")

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
    print("ERROR: No has introducido el sexo correcto.")

print(f"Eres del grupo: {grupo}")