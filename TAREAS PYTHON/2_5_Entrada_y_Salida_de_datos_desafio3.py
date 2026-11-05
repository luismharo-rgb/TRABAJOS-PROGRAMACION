# factura formateada
nombre_producto =[]
cantidad = []
precio_unitario = []

def generar_factura(nombre_producto, cantidad, precio_unitario):
    
    factura_formato = f"""
    -------------------------------
            FACTURA DE VENTA
    -------------------------------
    Producto.            ||cantidad.        ||Precio Unitario 
    """
    total = 0
    for i in range(len(nombre_producto)):
        total += (cantidad[i] * precio_unitario[i])
        factura_formato += f"""
        "{nombre_producto[i]}",          "{cantidad[i]}",              "${precio_unitario[i]:.2f}"  
        
    """
    
    factura_total=f"""
    -------------------------------
    Total a Pagar: ${total:.2f}
    -------------------------------
    """
    return factura_formato + factura_total
print("Bienvenido al programa de facturación.\n")
while True:    
    nombre_producto_respuesta = input("Ingrese el nombre del producto(o salir para terminar): ")
    if nombre_producto_respuesta.lower() == "salir":
        print("Saliendo del programa de facturación.")
        break
    else:
        try:
            nombre_producto.append(nombre_producto_respuesta)
            cantidad.append(int(input("Ingrese la cantidad de productos: ")))
            precio_unitario.append(float(input("Ingrese el precio unitario del producto: ")))
        except ValueError:
            print("Error: Debe ingresar un valor válido.")
            continue

factura = generar_factura(nombre_producto, cantidad, precio_unitario)
print(factura)
