import random  # Para generar de forma aleatoria las temperaturas
import time  # Para simular carga

temperaturas = []  # Lista para las temperaturas

# Genero un título para el programa
print("""
    == PROGRAMA REGISTRO ALEATORIO DE TEMPERATURAS ==
    Se generarán temperaturas aleatorias entre -10 y 40 grados Celsius.
    """)

# Luego el usuario ingresa la cantidad de temperaturas a registrar
cantidad_temperaturas = int(input("Ingrese la cantidad de temperaturas a registrar: "))

# En el for se genera aleatoriamente la cantidad de temperaturas
# y se redondea a 2 decimales
for _ in range(cantidad_temperaturas):
    temp_aleatoria = round(random.uniform(-10.0, 40.0), 2)
    temperaturas.append(temp_aleatoria)

# Luego este for solo es para mostrar una 'pantalla de carga'
for i in range(10):
    point = "." * (i + 1)  # Suma puntos(".") para simular carga
    # Esto permite que no salte de linea y se sobreescriba la misma linea
    print(f"\rEspere {point}", end="")
    time.sleep(0.25)  # Pausa de 0.25 segundos para simular carga

print()
print("Temperaturas registradas: ", temperaturas)  # Muestra temperaturas
