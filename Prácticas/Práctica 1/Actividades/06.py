# EJERCICIO 6 PRACTICA 1
# Modifique el ejercicio 4 para que dada la lista de número genere dos nuevas listas, una
# con los número pares y otras con los que son impares. Imprima las listas al terminar de
# procesarlas.

numeros = [7, 2, 9, 1, 4, 11, 2, 20, 91, 10]
pares = []
impares = []

for num in numeros:
    if num % 2 != 0:  # Si el número no es par
        impares.append(num) # Agrego a la lista de impares
    else:
        pares.append(num) 

print("Lista pares: ")
for num in pares:
    print(num)

print("Lista impares: ")
for num in impares:
    print(num)
