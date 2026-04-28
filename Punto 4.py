#Buscador de Duplicados: Dada una lista con elementos repetidos, genera una
#nueva lista que contenga únicamente los elementos que aparecían más de una vez,
#pero sin repetirlos en el resultado final.

lista = [1, 9, 2, 3, 2, 4, 4, 3, 8, 9, 1] 
repetidos = []

for i in lista:
    if lista.count(i) > 1 and i not in repetidos: #Asegura que no meta en la lista de repetidos uno que ya está.
        repetidos.append(i) #lo mete en los numeros repetidos.

print(repetidos)