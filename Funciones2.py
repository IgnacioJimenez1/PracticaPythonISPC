#A partir del siguiente ejemplo “Hola Ana, ¿Qué tal?” realizar el programa la ejecución del mismo
# con al menos otros dos nombres más, es decir, tres mensajes con tres nombres distintos.
#Recuerda: en estos ejercicios trabajamos argumentos.


def mensaje_saludo(nombre):
    mensaje = f"Hola {nombre}, ¿Qué tal?"
    return mensaje

nombres = ["Ana", "Juan", "María"]

for nombre in nombres:
    saludo = mensaje_saludo(nombre)
    print(saludo)
