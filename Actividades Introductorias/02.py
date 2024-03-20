# EJERCICIO 2 PRACTICA 1
#  Haz un programa que pida al usuario que ingrese una temperatura en grados Celsius y
# luego convierta esa temperatura a grados Fahrenheit, mostrando el resultado

temp_celsius = float(input("Ingresar una temperatura en grados Celsius: "))

def convertir(temp_celsius):
    temp_fahrenheit = (9/5) * temp_celsius + 32
    return temp_fahrenheit

temp_fahrenheit = convertir(temp_celsius)
print("Temperatura en grados Fahrenheit:", temp_fahrenheit)