#!/usr/bin/env python3

def es_primo(numero):
    
    if numero.isdigit():
        try:
            numero = int(numero)
            if numero == 1:
                primo = False
            else:
                primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    primo = False
                    break

            return primo

        except ValueError:
            print("ERROR: ¡No has introducido un número enntero!")
    else:
        print("ERROR: ¡No has introducido un número!")

def main():
    numero = input("Introduce un número entero: ")
    p = es_primo(numero)
    if p:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

if __name__ == '__main__':
    main()