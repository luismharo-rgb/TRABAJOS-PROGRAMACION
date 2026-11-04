
print("PROGRAMA VERIFICADOR NUMEROS")
print("")
#  Pedimos el dato al usuario
dato = input("Ingresa un número entero: ")
# Usamos un bloque try-except para manejar posibles errores de conversión
try:
    # Intentamos convertir el dato a un número entero
    numero = int(dato)
    # Si la conversión es exitosa, continuamos con el programa    
    #  Verificamos uno por uno si el número es múltiplo de 2, 3, 5, 7, 9, 10 y 11
    if numero % 2 == 0: # El operador % devuelve el resto de la división. 
       # Si el resultado es 0, entonces el número es múltiplo del divisor.
        print(numero, "es múltiplo de 2")
    else:
        print(numero, "no es múltiplo de 2")
    if numero % 3 == 0:
        print(numero, "es múltiplo de 3")
    else:
        print(numero, "no es múltiplo de 3")
    if numero % 5 == 0:
        print(numero, "es múltiplo de 5")
    else:
        print(numero, "no es múltiplo de 5")
    if numero % 7 == 0:
       print(numero, "es múltiplo de 7")
    else:
        print(numero, "no es múltiplo de 7")
    if numero % 9 == 0:
        print(numero, "es múltiplo de 9")   
    else:
        print(numero, "no es múltiplo de 9")
    if numero % 10 == 0:
        print(numero, "es múltiplo de 10")        
    else:
        print(numero, "no es múltiplo de 10")
    if numero % 11 == 0:
        print(numero, "es múltiplo de 11")
    else:
        print(numero, "no es múltiplo de 11")   
    print("presione una tecla para continuar...")
 # Si el usuario ingresó algo que no se puede convertir a entero, se ejecuta el bloque except   
except ValueError:
    # Si el usuario escribió letras o símbolos
    print("Error: Solo puedes ingresar números enteros.")
    print("presione una tecla para continuar...")
input()
