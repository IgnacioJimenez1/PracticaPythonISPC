#Confeccione un programa que pida un número del 1 al 7 y diga el día de
#la semana correspondiente.

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

numero_dia = int(input("Ingrese un número entre 1 y 7: "))

if 1 <= numero_dia <= 7:
    dia_semana = dias_semana[numero_dia - 1]
    print("El día de la semana correspondiente es", dia_semana)
else:
    print("Número no válido. Ingrese un número del 1 al 7.")
