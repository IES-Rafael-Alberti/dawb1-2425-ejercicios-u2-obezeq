#!/usr/bin/env python3

palabra = input("Introduce una palabra: ")

list = []
for p in palabra:
    list.append(p)
    
list = list[::-1]

for l in list:
    print(l)