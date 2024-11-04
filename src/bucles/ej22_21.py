#!/usr/bin/env python3

print("[+] Introduce los montos de tu compra: ")

montos = 0
while True:
    try:
        monto = round(float(input("~> $")), 2)
        if monto == 0:
            break
        elif monto < 0:
            print("[-] El monto es negativo")
            print("[+] Introduce de nuevo el monto de compra")
        elif monto > 1000:
            monto *= 0.9
            montos += monto
        else:
            montos += monto
    except ValueError:
        print("[-] ERROR: No se ha introducido un número.")

print(f"El monto total ha pagar es: ${montos:.2f}")