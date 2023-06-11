numeros = []
for i in range(15):
    numero = int(input("Ingresa un número negativo: "))
    numeros.append(abs(numero))  
    
print("Números convertidos a positivos:")
for numero in numeros:
    print(numero)
