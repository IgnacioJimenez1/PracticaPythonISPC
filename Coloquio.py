#Realizar un programa en Python que conste de la conversión de °C a °F, °K.
#El mismo debe permitirle al usuario el ingreso del número a convertir en el tipo de dato que se considere correspondiente
# y con un mensaje que justifique cada conversión mostrándolo por pantalla.


def C_a_F(C):
    F = (C * 9/5) + 32
    return F

def C_a_K(C):
    K = C + 273.15
    return K

# Pedir ingreso de grados Celsius
C = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir a Fahrenheit
F = C_a_F(C)
print(f"{C} grados Celsius son {F} grados Fahrenheit.")

# Convertir a Kelvin
K = C_a_K(C)
print(f"{C} grados Celsius son {K} grados Kelvin.")
