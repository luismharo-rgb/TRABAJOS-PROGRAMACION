import time

print("Bienvenido al programa de operaciones matemáticas.\n")

try:    
    # Cambiado a float por si el usuario quiere usar decimales
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))   
except ValueError:
    print("Error: Debe ingresar un número válido.")
    exit()

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2


if numero2 != 0:
    division = round(numero1 / numero2, 2)
else:
    division = "No es posible dividir entre cero"


ojos = ["(o o)", "(= =)", "(> <)", "(0_0)"]
for i in range(4):
    
    print(f"\rCalculando... {ojos[i]}   ", end="", flush=True)
    time.sleep(0.5)
print("\n")

print(f"La suma de los números es: {round(suma, 2)}")
print(f"La resta de los números es: {round(resta, 2)}")
print(f"La multiplicación de los números es: {round(multiplicacion, 2)}")
print(f"La división de los números es: {division}")
