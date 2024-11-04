#!/usr/bin/env python3

import os

def refresh():
    os.system('cls') if os.name == 'nt' else os.system('clear')

refresh()

print("┌─────────────────────────────────────────┐")
print("│ SELECCIONA EL TIPO DE PIZZA QUE QUIERAS │")
print("└─────────────────────────────────────────┘")
print("[1] Pizza vegetariana")
print("[2] Pizza no vegetariana")
print("───────────────────────────────────────────")

pizza = input("\n~> ")
refresh()

print("┌─────────────────────────────────────────────────────┐")
print("│ MENU DE PIZZA - Selecciona solamente un ingrediente │")
print("└─────────────────────────────────────────────────────┘")
if pizza == "1":
    print("- Ingredientes vegetarianos: Pimiento y tofu.")
elif pizza == "2":
    print("- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")
else:
    print("ERROR: No has seleccionado una pizza correcta.")
    os._exit(0)
print("──────────────────────────────────────────────────────────────────────")

og_input_ingrediente = input("\n~> ")
input_ingrediente = og_input_ingrediente.lower().replace(" ", "")

refresh()

if input_ingrediente == "":
    print("Tienes que elegir un ingrediente.")

# Lista de posibles ingredientes
ingredientes_vegetariano = ["pimiento", "tofu"]
ingredientes_no_vegetariano = ["peperoni", "jamon", "jamón", "salmon", "salmón"]

# Lista con ingredientes añadidos por usuario
lista_ingredientes = ["Mozzarella", "Tomate"]

not_added = True

if pizza == "1":
    pizza = "es vegetariana"
    for ingrediente in ingredientes_vegetariano:
        if input_ingrediente == ingrediente:
            lista_ingredientes.append(ingrediente.capitalize())
            not_added = False
    if not_added:
        print(f"ERROR: No se ha encontrado ningun ingrediente '{og_input_ingrediente}' en el menú")
        os._exit(0)

else:
    pizza = "no es vegetariana"
    for ingrediente in ingredientes_no_vegetariano:
        if input_ingrediente == ingrediente:
            lista_ingredientes.append(ingrediente.capitalize())
            not_added = False
    if not_added:
        print(f"ERROR: No se ha encontrado ningun ingrediente '{og_input_ingrediente}' en el menú")
        os._exit(0)

print(f"Su pizza {pizza} y tiene la siguiente lista de ingredientes:")
for ingrediente in lista_ingredientes:
    print(f"- {ingrediente}")