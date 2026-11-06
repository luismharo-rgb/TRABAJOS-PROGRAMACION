print("CALCULO DE PROMEDIO DE NOTAS DE ESTUDIANTES\n")
# ingreso de notas
entrada = input("Ingrese las notas de los estudiantes (entre 1 y 12) separadas por comas: ")
# lista para guardar las notas validas
notas = []
# este for hace de contador para cada elemento de la lista y luego quita las comas
for item in entrada.split(","):

    item_limpio = item.strip()  # Elimina espacios en blanco sobrantes
    if item_limpio:  #  Este es el valor correcto a validar 
        try:
            nota = int(item_limpio) # se pasa a entero
            # Verificamos que esté dentro del rango permitido (1 a 12)
            if 1 <= nota <= 12:
                notas.append(nota) # se agrega a la lista notas
            else:
                # si el valor no corresponde, se informa al usuario y se descarta
                print(f"La nota {nota} no está entre 1 y 12, por lo que fue descartada.")
                # pero el for no se detiene, por tanto un error no borra todos los datos ingresados, solo el que no corresponde
        except ValueError:
            # si el valor no es un número, se informa al usuario y se descarta igualmente
            print(f"'{item_limpio}' no es un número válido y fue descartado.")
# si la lista tiene numeros validos, se calcula el promedio y se informa al usuario si aprobó o reprobó el año
if len(notas) > 0:
    promedio = sum(notas) / len(notas)
    print(f"\nNotas consideradas: {notas}")
    print(f"El promedio de las notas es: {promedio:.2f}, por tanto el estudiante ha {'aprobado' if promedio >= 6 else 'reprobado'} el año.")
else:
    print("No se ingresaron notas válidas para calcular el promedio.")