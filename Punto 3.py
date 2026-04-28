#Inversión de Frases: Pide al usuario una frase y devuelve las palabras en orden
#inverso utilizando listas

frase = input("Ingresá una frase: ")
palabras = frase.split()
inversion = palabras[::-1]
resultado = " ".join(inversion) #Si no pongo " " me pone todo junto.
print(resultado)