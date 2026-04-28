#Simulador de Carrito de Compras: Crea un programa que permita al usuario
#ingresar nombres de productos y sus precios hasta que escriba "fin". Al terminar,
#debe mostrar el total gastado y el producto más caro.

carrito = []
precios = []

while True:
    producto = input(f"Ingresá un producto (o 'fin' para terminar): ")
    
    if producto.lower() == "fin": #por si a uno le pinta poner todo en mayusculas o "Fin". Que se yo, para asegurar.
        break
    
    precio = float(input(f"Ingresá el precio de {producto}: "))
    carrito.append(producto)
    precios.append(precio)

if len(precios) == 0:
    print("No se ingresaron productos")
else:
    total = sum(precios)
    mas_caro = carrito[precios.index(max(precios))] #Busca el índice del precio más caro así lo asocia con el producto.

    print(f"Total gastado: ${total}")
    print(f"Producto más caro: {mas_caro}")
