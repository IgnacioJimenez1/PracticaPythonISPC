#Realizar un programa que permita ingresar “f” o “m” y determinar si vota en mesa femenina o masculina.

# Pedir ingreso de género

genero = input("Ingrese su género (f/m): ")


if genero.lower() == "f":
    print("Usted vota en la mesa femenina")
elif genero.lower() == "m":
    print("Usted vota en la mesa masculina")
else:
    print("El género ingresado no es válido")