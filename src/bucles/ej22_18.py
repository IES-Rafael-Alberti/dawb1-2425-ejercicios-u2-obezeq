#!/usr/bin/env python3

#!/usr/bin/env python3

list = []

while True:
    n = input("Introduce un número: ")

    try:
        if float(n) == -1:
            break
        elif float(n) < 0 and float(n) != -1:
            print("[-] ERROR: No has introducido un número positivo\n")
        elif float(n).is_integer() == False:
            print("[-] ERROR: No has introducido un número entero positivo\n")
        else:
            list.append(int(n))
            
    except ValueError:
        print("ERROR: No has introducido un número!")

suma = 0
pares = 0
for n in list:
    suma += n
    if n % 2 == 0:
        pares += 1

print(f"La suma de todos los números enteros y positivos que has introducido es: {suma} y hay {pares} pares.")