#Realice un programa que contenga una función que se llame “sumayresta”, que la misma contenga dos variables locales nombradas suma y resta, respectivamente.
#Recuerda: en estos ejercicios trabajamos argumentos para este ejercicio sería dos.

def sumayresta(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

# Solicitar los dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Llamar a la función "sumayresta" y obtener los resultados
resultado_suma, resultado_resta = sumayresta(num1, num2)

# Mostrar los resultados
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
