#!/usr/bin/env python3

def calcular_rendimiento(rendimiento: str) -> str:
    try:
        rendimiento = float(rendimiento)

        if rendimiento == 0.0 or rendimiento == 0.4 or rendimiento >= 0.6:
            dinero = round((rendimiento * 2400), 2)
            return f"Tu nivel de rendimiento es {rendimiento} y has conseguido: {dinero}€"
        else:
            return "ERROR: Tienes que poner alguna de las puntuaciones mencionadas."

    except ValueError:
        return "ERROR: No has introducido un nivel de rendimiento correcto."

def main():
    print("──────────────────────────────────")
    print("INTRODUCE TU NIVEL DE RENDIMIENTO:")
    print("──────────────────────────────────")
    print("Inaceptable: 0.0")
    print("Inaceptable: 0.4")
    print("Inaceptable: 0.6 o más")
    print("──────────────────────────────────")

    rendimiento = input("~> ")

    result = calcular_rendimiento(rendimiento)
    print(result)

if __name__ == '__main__':
    main()