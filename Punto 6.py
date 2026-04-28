#Conversor de Binario a Decimal: Solicita al usuario una lista de ceros y unos
#(un número binario) y calcula su equivalente decimal manualmente usando ciclos.

binario = input("Ingresá un número binario: ") #Uso string porque necesito recorrer cada dígito del número binario.

if not all(i in "01" for i in binario): #Valida si alguien pone algo distinto de ceros y unos.
    print("Ingresá solo 0 y 1.")
else:
    bits = [int(i) for i in binario] #Convierte todos los carácteres a números.

    decimal = 0

    for i in range(len(bits)):
        exponente = len(bits) - 1 - i
        decimal += bits[i] * (2 ** exponente)

    print(f"El número decimal es: {decimal}")
