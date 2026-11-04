print(".        TRANSFORMACION DE TEMPERATURAS         .")
print(" ")
# ingresamos la temperatura en grados Celsius
print("Ingrese la temperatura en grados Celsius: ")
# asignamos a celsius el valor ingresado por el usuario, convirtiéndolo a un número decimal (float)
celsius = float(input())
# La formula para convertir de grados Celsius a grados Fahrenheit es: (celsius * 9/5) + 32
# Fahrenheit: F=(C×59​)+32
fahrenheit = (celsius * 9/5) + 32
# se muestra el resultado al usuario
print("La temperatura en grados Fahrenheit es: ", fahrenheit)
print(" ")
# para comprobar que la formula es correcta, se muestra la formula al usuario
print("La formula para convertir de grados Celsius a grados Fahrenheit es: (celsius * 9/5) + 32")
print("presione una tecla para continuar...")
input()
