# EJERCICIO 7 PRACTICA 1
# Escribe un programa que tome una lista de números enteros como entrada del usuario.
# Luego, convierte cada número en la lista a string y únelos en una sola cadena,
# separados por guiones ('-'). Sin embargo, excluye cualquier número que sea múltiplo
# de 3 de la cadena final.

lista = []

print("CARGA DE LA LISTA: ")

num = float(input("Ingresar un numero: "))

while num != 0 :
    lista.append(num)
    num = float(input("Ingresar un numero: "))

cadena = ""
for num in lista:
    if num % 3 == 0:
        continue
    cadena = cadena + f" {num} - "
print(cadena)