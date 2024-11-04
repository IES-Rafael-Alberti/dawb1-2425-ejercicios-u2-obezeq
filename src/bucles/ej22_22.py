#!/usr/bin/env python

pares_total = 0
impares_total = 0

while True:
    numero = input("Introduce un número entero positivo: ")
    if numero.strip() == "0":
        break
    else:
        try:
            numero = float(numero)
            if numero.is_integer():
                if numero < 0:
                    print("[-] ERROR: No has introducido un número positivo\n")
                else:
                    numero = str(int(numero))
                    par = 0
                    impar = 0
                    for n in numero:
                        if int(n) % 2 == 0:
                            par += 1
                            pares_total += 1
                        else:
                            impar += 1
                            impares_total += 1
                    print(f"El dígito {numero} tiene {par} pares y {impar} impares.\n")
            else:
                print(f"[-] ERROR: No has introducido un número entero\n")
        except ValueError:
            print(f"[-] ERROR: No has introducido un número\n")
    
print(f"\nNúmero de pares totales de todos los digitos de los números: {pares_total}")
print(f"Número de impares totales de todos los digitos de los números: {impares_total}")
