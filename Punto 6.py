#Conversor de Binario a Decimal: Solicita al usuario una lista de ceros y unos
#(un número binario) y calcula su equivalente decimal manualmente usando ciclos.

binario = input("Ingresá un número binario: ") #Uso string porque necesito recorrer cada dígito del número binario.

bits = [int(i) for i in binario] #Convierte todos los carácteres a números.

decimal = 0

for i in range(len(bits)):
    exponente = len(bits) - 1 - i
    decimal += bits[i] * (2 ** exponente)

print(f"El número decimal es: {decimal}")