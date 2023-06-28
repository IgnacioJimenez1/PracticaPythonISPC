# 1. Realice un programa que muestre el mensaje “Hola Aula X (Indicar el número de aula a la que pertenecen),
# ¿Qué tal?” en tres veces intercambiados entre ellos otro mensajes a su elección. 


def intercambiar_mensajes(aula):
    print(f"Hola Aula {aula}, ¿Qué tal?")

    # Intercambio de mensajes
    mensaje1 = input("Ingresa el primer mensaje: ")
    mensaje2 = input("Ingresa el segundo mensaje: ")
    mensaje3 = input("Ingresa el tercer mensaje: ")

    print(f"Aula {aula} dice: {mensaje3}")
    print(f"Aula {aula + 1} dice: {mensaje2}")
    print(f"Aula {aula + 2} dice: {mensaje1}")


# Solicitar número de aula al usuario
num_aula = int(input("Ingresa el número de aula: "))

# Mostrar el mensaje y realizar el intercambio de mensajes tres veces
for _ in range(3):
    intercambiar_mensajes(num_aula)
    num_aula += 3
