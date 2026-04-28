#El Filtro de Nombres: Crea una función que reciba una lista de nombres y
#devuelva solo aquellos que comiencen con una vocal y tengan más de 5
#caracteres.

nombres = []
nombres2 = []
vocales = "aAeEiIoOuU"
ingresados = 0

n = int(input(f"Que onda negrito, cuantos nombres queres ingresar?: "))

while ingresados < n:
    pp = input(f"Ingrese un nombre: ")
    if not pp.isalpha():
        print(f"Dale amigo, solo letras, no seas tarado.")
    else:
        nombres.append(pp)
        ingresados = ingresados + 1
        if pp[0] in vocales and len(pp) > 5:
            nombres2.append(pp)

print(nombres, "- Estos no  cumplen los requisitos.")
print(nombres2, "- Estos sí cumplen los requisitos.")