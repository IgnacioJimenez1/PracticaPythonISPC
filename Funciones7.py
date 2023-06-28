#Realizar un programa de funciones que contengan funciones con bucles y control de flujo fuera de la función decoradora. Al menos se deben tener dos condicionales o bucles.

def decorador(funcion):
    def wrapper(*args, **kwargs):
        print("¡Inicio de la función decorada!")
        resultado = funcion(*args, **kwargs)
        print("¡Fin de la función decorada!")
        return resultado
    return wrapper

@decorador
def funcion_con_bucles(n):
    print("¡Inicio de la función con bucles!")
    for i in range(n):
        if i % 2 == 0:
            print(f"Número par: {i}")
        else:
            print(f"Número impar: {i}")
    print("¡Fin de la función con bucles!")

@decorador
def funcion_con_condicionales(a, b):
    print("¡Inicio de la función con condicionales!")
    if a > b:
        print(f"{a} es mayor que {b}")
    elif a < b:
        print(f"{a} es menor que {b}")
    else:
        print(f"{a} es igual a {b}")
    print("¡Fin de la función con condicionales!")


# Llamar a la función decorada con bucles
funcion_con_bucles(5)

# Llamar a la función decorada con condicionales
funcion_con_condicionales(5, 6)

