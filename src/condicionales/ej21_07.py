#!/usr/bin/env python3

def calcular_renta(renta: str):
    try:
        renta = float(renta)

        if renta < 10000:
            impositivo = 0.05
        elif renta >= 10000 and renta <= 20000:
            impositivo = 0.15
        elif renta > 20000 and renta < 35000:
            impositivo = 0.2
        elif renta >= 35000 and renta < 60000:
            impositivo = 0.3
        elif renta >= 60000:
            impositivo = 0.45
        else:
            return "Algo ha salido mal con tu renta!"
        
        return f"Tu tipo de impositivo es: {int(impositivo*100)}%"

    except ValueError:
        return "No has introducido un número!"

def main():
    renta = input("Introduce tu renta anual: ")
    
    result = calcular_renta(renta)
    print(result)

if __name__ == '__main__':
    main()