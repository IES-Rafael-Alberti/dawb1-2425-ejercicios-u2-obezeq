#!/usr/bin/env python3

def algoritmo_burbuja(a: list) -> list:

    iteraciones = len(a) - 1

    for i in range(iteraciones):
        j = i
        counter = 0
        while (j < iteraciones):
            
            left = a[counter]
            right = a[counter+1]
            
            if left > right:
                a[counter], a[counter+1] = a[counter+1], a[counter]

            counter +=1
            j += 1

    return a

def main():
    a = [8, 3, 1, 19, 14]
    lista_ordenada = algoritmo_burbuja(a)
    print(lista_ordenada)

if __name__ == '__main__':
    main()