#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calcular_total_factura(cantidad_sin_iva, porcentaje_iva=21):
    total = cantidad_sin_iva + cantidad_sin_iva * porcentaje_iva / 100
    return total


cantidad = float(input("Ingrese la cantidad sin IVA: "))
porcentaje = float(input("Ingrese el porcentaje de IVA (opcional): "))

total_factura = calcular_total_factura(cantidad, porcentaje)
print("Total de la factura:", total_factura)
