#Análisis de Rango: Dada una lista de 10 números aleatorios, encuentra el valor
#máximo, el mínimo y calcula la diferencia entre ellos.

import random

numeros = []

for i in range(10): #Genera 10 números random del 1 al 100.
    numeros.append(random.randint(1, 100))

maximo = max(numeros)
minimo = min(numeros)
diferencia = maximo - minimo

print(f"Lista: {numeros}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Diferencia: {diferencia}")
