print ("_"*50)
try:
    # usamos "x" para crear el archivo solo si no existe
    with open("prestamos.txt", "x", encoding="utf-8") as archivo:
        # encoding="utf-8" para soportar caracteres especiales
        # al codificar en mi caso en mac, no es necesario, 
        # pero en Windows ahorra errores como las "ñ" y los acentos
        archivo.write("LISTA PRESTAMOS LIBROS\n")
    print("Archivo creado con éxito.")
except FileExistsError:
    # esta excepcion funciona si el archivo ya existe.
    print("Archivo prestamos.txt ya existe, se procede a abrir para su modificación.")
print ("_"*50)
print("\nLISTA DE PRÉSTAMOS DE LIBROS\n")
while True:
    print("""
    === MENÚ DE PRÉSTAMOS ===
    1. Registrar Préstamo
    2. Ver Historial
    3. Salir
    """)
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        print("\n-> Entrando a registrar préstamo...\n")
    elif opcion == "2":
        print("\n-> Mostrando historial...\n")
    elif opcion == "3":
        print("\n¡Gracias por usar el sistema!")
        break # Rompe el bucle y cierra el programa
    else:
        print("\n[!] Opción inválida, intenta de nuevo.\n")

