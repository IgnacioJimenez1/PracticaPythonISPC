#Realizar un programa de funciones que contengan 3 parámetros, el cual derive en una suma. Mostrar el resultado dos veces.

def suma_parametros(a, b, c):
    suma = a + b + c
    return suma

# Solicitar los tres parámetros

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

# Calcular la suma utilizando la función y mostrar el resultado 2 veces

resultado = suma_parametros(a, b, c)
print("El resultado es:", resultado)
print("El resultado es:", resultado)
