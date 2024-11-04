#!/usr/bin/env python3

while True:
    print("─────────────────────────")
    print("ELIGE UNA DE LAS OPCIONES")
    print("─────────────────────────")
    print("[1] Comenzar programa")
    print("[2] Imprimir listado")
    print("[3] Finalizar programa")
    print("─────────────────────────\n")

    opcion = input("Introduce una de las opciones: ").lower().replace(' ', '')

    if opcion == "1" or opcion == "2":
        print("\n~> Impresion de Texto\n")
    elif opcion == "3":
        break
    else:
        print("\nERROR: Opción incorrecta\n")