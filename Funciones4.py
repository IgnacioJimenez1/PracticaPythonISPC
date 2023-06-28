#Realice un programa que lea dos números (dos parámetros), compare si son IGUALES, en ese caso, mostrar un mensaje que muestre TRUE. 

def comparar_numeros(num1, num2):
    if num1 == num2:
        print("TRUE")

#Pedir los 2 números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

#Llamar para comparar los números
comparar_numeros(num1, num2)
