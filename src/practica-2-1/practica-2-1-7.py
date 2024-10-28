#!/usr/bin/env python3

try:
    renta = float(input("Introduce tu renta anual: "))

    if renta < 10000:
        impositivo = 0.05
    elif renta >= 10000 and renta <= 20000:
        impositivo = 0.15
    elif renta >= 20000 and renta <= 35000:
        impositivo = 0.2
    elif renta >= 35000 and renta <= 60000:
        impositivo = 0.3
    elif renta > 60000:
        impositivo = 0.45
    else:
        print("Algo ha salido mal con tu renta!")
    
    print(f"Tu tipo de impositivo es: {int(impositivo*100)}%")

except ValueError:
    print("No has introducido un número!")