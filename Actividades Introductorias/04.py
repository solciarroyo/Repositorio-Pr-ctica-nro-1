# EJERCICIO 4 PRACTICA 1
# Cree un programa que dada una lista de números imprima sólo los que son pares.
# Nota: utilice la sentencia continue donde haga falta.

numeros = [7, 2, 9, 1, 4, 11, 2, 20, 91, 10]

print("Números pares:")

for num in numeros:
    if num % 2 != 0:  # Si el número no es par
        continue  # Saltar al siguiente número en la lista
    print(num)

