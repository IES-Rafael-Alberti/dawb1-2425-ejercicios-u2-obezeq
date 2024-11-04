#!/usr/bin/env python3

def check_pass(user_pass: str) -> str:
    og_pass = "diegoponmeun10"
    if user_pass == og_pass:
        return f"La contraseña es correcta: {user_pass}"
    else:
        return "La contraseña no es correcta."

def main():

    user_pass = input("Introduce la contraseña: ")
    
    result = check_pass(user_pass)
    print(result)

if __name__ == '__main__':
    main()
