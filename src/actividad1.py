#!/usr/bin/env python3

# Check nuuber
def check_num(n: str) -> (int | bool):
    try:
        n = int(n)
        return n
    except ValueError:
        return False

# Calc average
def calc_averange(n: list) -> float:
    len_list = len(n)
    sum_nums = 0

    for i in n:
        sum_nums += i

    average = sum_nums / len_list

    return sum_nums, len_list, average

def main():

    n_list = []
    salir = ""
    while salir != "fin":
        n = input("Introduzca un número: ").strip().replace(' ', '').lower()
        if n == "fin":
            if n_list == []:
                print("¡No has introducido ningún número!")
            else:
                salir = "fin"
        else:
            n = check_num(n)
            if n:
                n_list.append(n)
            else:
                print("dato erróneo")

    values_calc = calc_averange(n_list)

    sum_num = values_calc[0]
    amount = values_calc[1]
    average = values_calc[2]

    print(sum_num, amount, average)

if __name__ == '__main__':
    main()