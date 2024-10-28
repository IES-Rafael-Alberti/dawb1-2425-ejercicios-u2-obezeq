#!/usr/bin/env python3

lista = [1,2,3,4,5,6,7,8,9,10]

for x in lista:
    print(f"\nLista de multiplicar del {x}: ")
    for y in lista:
        print(f'{x} * {y} = {x*y}')