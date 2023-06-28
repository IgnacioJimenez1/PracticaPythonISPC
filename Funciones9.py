#Escribir una función que convierta un número decimal en los otros dos sistemas:
# Binario y Hexadecimal. Mostrar mensajes pertenecientes a cada función.


def convertir_sistemas(numero_decimal):
    print(f"Convirtiendo el número decimal {numero_decimal} a binario...")
    numero_binario = bin(numero_decimal)[2:]
    print("El número binario es:", numero_binario)

    print(f"\nConvirtiendo el número decimal {numero_decimal} a hexadecimal...")
    numero_hexadecimal = hex(numero_decimal)[2:]
    print("El número hexadecimal es:", numero_hexadecimal.upper())



decimal = int(input("Ingrese un número decimal: "))
convertir_sistemas(decimal)
