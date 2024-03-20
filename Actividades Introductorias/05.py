# EJERCICIO 5 PRACTICA 1
# Implementa un programa que solicite al usuario que ingrese una lista de números.
# Luego, imprime la lista pero detén la impresión si encuentras un número negativo.
# Nota: utilice la sentencia break cuando haga falta.

lista = []

print("Ingrese una lista de numeros: ")

for i in range(5):
    nro = int(input("Ingrese un numero: "))
    lista.append(nro)

for nro in lista:
    if (nro < 0): 
        break
    print(nro)