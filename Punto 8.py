#Análisis de Rango: Dada una lista de 10 números aleatorios, encuentra el valor
#máximo, el mínimo y calcula la diferencia entre ellos.

import random

numeros = [random.randint(1, 100) for _ in range(10)] #Busca un número random del 1 al 100.

maximo = max(numeros)
minimo = min(numeros)
diferencia = maximo - minimo

print(f"Lista: {numeros}")
print(f"Máximo: {maximo}")
print(f"Mínimo: {minimo}")
print(f"Diferencia: {diferencia}")