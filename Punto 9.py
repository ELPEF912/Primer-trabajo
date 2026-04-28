#Compresión de Datos Básica: Escribe una función que reciba una lista de
#caracteres repetidos y devuelva una lista de sublistas con el carácter y su frecuencia


letras = ['a', 'b', 'a', 'c', 'c', 'a', 'z', 'a', 'b']
resultado = []
contados = []

for i in letras:
    if i not in contados: #Hace que no se cuente una letra que ya se contó.
        resultado.append([i, letras.count(i)])
        contados.append(i)

print(resultado)