#Realice un programa que contengan funciones de los tres tipos de triángulos.
# Los mismos deben estar acompañados de los mensajes respecto a la función decoradora.
#   Para mejorarlo pueden agregar los nombres de cada función según los triángulos.

def decorador_tipo_triangulo(funcion_tipo_triangulo):
    def wrapper(a, b, c):
        print(f"¡Calculando información sobre el triángulo {funcion_tipo_triangulo.__name__.capitalize()}!")
        funcion_tipo_triangulo(a, b, c)
        print("¡Cálculos completados!")
        print("----------------------")
    return wrapper

@decorador_tipo_triangulo
def triangulo_equilatero(a, b, c):
    if a == b == c:
        print("Es un triángulo equilátero.")
    else:
        print("No es un triángulo equilátero.")

@decorador_tipo_triangulo
def triangulo_isosceles(a, b, c):
    if (a == b or a == c or b == c)  and not (a == b == c):
        print("Es un triángulo isósceles.")
    else:
        print("No es un triángulo isósceles.")

@decorador_tipo_triangulo
def triangulo_escaleno(a, b, c):
    if a != b and a != c and b != c:
        print("Es un triángulo escaleno.")
    else:
        print("No es un triángulo escaleno.")


# Solicitar las longitudes de los lados al usuario
a = float(input("Ingrese la longitud del lado A: "))
b = float(input("Ingrese la longitud del lado B: "))
c = float(input("Ingrese la longitud del lado C: "))

# Calcular y mostrar información sobre el triángulo equilátero
triangulo_equilatero(a, b, c)

# Calcular y mostrar información sobre el triángulo isósceles
triangulo_isosceles(a, b, c)

# Calcular y mostrar información sobre el triángulo escaleno
triangulo_escaleno(a, b, c)
