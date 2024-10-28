#!/usr/bin/env python3

def n_letras(frase, letra):
    counter = 0
    for l in frase:
        if l == letra:
            counter += 1

    return counter

def main():
    frase = input("Introduce una frase: ")
    letra = input("Introduce una letra: ")

    n = n_letras(frase, letra)
    print(f"En la frase '{frase}' hay {n} número de letras.")

if __name__ == '__main__':
    main()