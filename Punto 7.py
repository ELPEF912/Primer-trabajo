#El Traductor de &quot;P&quot;: Crea un programa que transforme una palabra añadiendo
#una &quot;p&quot; y repitiendo la vocal después de cada vocal encontrada (Ejemplo: &quot;hola&quot; -
#&gt; &quot;hopolapa&quot;).

palabra = input(f"Ingresá una palabra: ")

vocales = "aAeEiIoOuU"
resultado = ""

for i in palabra: #Recorre la palabra
    resultado += i #Agrega cada letra al resultado de la palabra
    if i in vocales: 
        resultado += "p" + i #Si tiene vocal le agrega la "p" + la vocal

print(resultado)