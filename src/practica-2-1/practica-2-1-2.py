#!/usr/bin/env python3

og_pass = "contraseña"

user_pass = input("Introduce la contraseñ: ").lower()

if user_pass == og_pass:
    print(f"La contraseña es correcta: {user_pass}")
else:
    print("La contraseña no es correcta.")
