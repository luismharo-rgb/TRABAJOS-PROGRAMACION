# Lista ordenada de códigos de productos
import time
alumnos = []

print("_"*50)
print("Listado de Alumnos")
print ("_"*50)

while True:
    nombre=input(f"Ingrese el nombre del alumno (o escriba 'fin' para terminar): ")
    if nombre.lower()=="fin":
        break
    else:
        alumnos.append(nombre)
print("Ordenando alumnos...")
time.sleep(1)
print("_"*50)
print("Listado de Alumnos Ingresados y ordenados")
print("_"*50)
alumnos.sort()  # Ordenar la lista de alumnos por nombre
print(alumnos)
    
# Búsqueda binaria de un producto por su código
def busqueda_binaria(alumnos, nombre_a_buscar):
    bajo = 0
    alto = len(alumnos) - 1

    while bajo <= alto:
        medio = (bajo + alto) // 2
        if alumnos[medio] == nombre_a_buscar:
            return medio  # Alumno encontrado
        elif alumnos[medio] < nombre_a_buscar:
            bajo = medio + 1
        else:
            alto = medio - 1

    return -1  # Alumno no encontrado

# Buscar el alumno con nombre "Pedro"
print("_"*50)
print("Busqueda de alumnos")
print("_"*50)
busca_alumno= input("Ingrese el nombre del alumno a buscar: ")
resultado = busqueda_binaria(alumnos, busca_alumno)
if resultado != -1:
    print(f"Alumno encontrado en la posición: {resultado}")
else:
    print(f"Alumno no encontrado")
