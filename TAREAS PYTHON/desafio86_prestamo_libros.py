import os
import time

def inicializar_archivo():
    # Verifica si el archivo existe
    print ("_"*50)
    try:
    # usamos "x" para crear el archivo solo si no existe
        with open("prestamos.txt", "x", encoding="utf-8") as archivo:
        # encoding="utf-8" para soportar caracteres especiales
        # al codificar en mi caso en mac, no es necesario, 
        # pero en Windows ahorra errores como las "ñ" y los acentos
            archivo.write("_"*30 + "\n")
            archivo.write("LISTA PRESTAMOS LIBROS\n")
            archivo.write("_"*30 + "\n")
            print("Archivo creado con éxito.")
    except FileExistsError:
    # esta excepcion funciona si el archivo ya existe.
        print("Archivo prestamos.txt ya existe, se procede a abrir para su modificación.")
        print ("_"*50)
    return True

def ingreso_prestamo(nombre_libro, nombre_usuario, fecha_prestamo):
    with open("prestamos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"Libro: {nombre_libro}, Usuario: {nombre_usuario}, Fecha: {fecha_prestamo}\n")
    print("Préstamo registrado con éxito.")
def mostrar_libros():
    #if not os.path.exists("prestamos.txt"):
    #    print("No hay historial de préstamos.")
    #    return
    try:
        with open("prestamos.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido)
    except Exception as e:
            print(f"Error al leer el archivo: {e}, no lo habrás borrado...¿cierto?")


inicializar_archivo()
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
        time.sleep(1)  # Pausa de 1 segundo para simular carga
        ingreso_prestamo(
            input("Nombre del libro: "),
            input("Nombre del usuario: "),
            input("Fecha de préstamo (dd/mm/aaaa): ")
        )
    elif opcion == "2":
        print("\n-> Mostrando historial...\n")
        mostrar_libros()
    elif opcion == "3":
        print("\n¡SALIENDO DEL PROGRAMA!")
        break # Rompe el bucle y cierra el programa
    else:
        print("\n[!] Opción inválida, intenta de nuevo.\n")

