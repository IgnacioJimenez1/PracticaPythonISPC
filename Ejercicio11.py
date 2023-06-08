meses = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}

mes = int(input("Ingrese un número entre 1 - 12: "))

if mes in meses:
    nombre_mes = meses[mes]
    print("El mes seleccionado es", nombre_mes)
else:
    print("Número no válido. Ingrese un número del 1 al 12.")