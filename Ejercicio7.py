# Introducir los lados de un triángulo y visualizar por pantalla si dicho
# triángulo es equilátero, isósceles o escaleno.

# Introducir lados
lado1 = float(input("Introduzca la medida del lado 1 en cm: "))
lado2 = float(input("Introduzca la medida del lado 2 en cm: "))
lado3 = float(input("Introduzca la medida del lado 3 en cm: "))

# Equilátero, isósceles o escaleno
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")