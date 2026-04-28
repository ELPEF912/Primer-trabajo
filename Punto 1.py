#Calculadora de Promedio Móvil: Escribe un programa que reciba una lista de
#números y devuelva una nueva lista donde cada elemento sea el promedio entre el
#número actual y el anterior (el primero se queda igual).

numeros = []
promedio = []
n = int(input(f"¿Cuántos números desea almacenar?: "))

if n == 0:
    print(f"No ingresó ningún número.")
    exit()
else:
    for i in range (n):
        num = float(input(f"Ingrese el número {i+1}: "))
        numeros.append(num)
    for i in range(len(numeros)):
        if i == 0:
            promedio.append(numeros[i])
        else:
            prom = (numeros[i] + numeros[i - 1]) / 2
            promedio.append(prom)
print(numeros)
print(promedio)
