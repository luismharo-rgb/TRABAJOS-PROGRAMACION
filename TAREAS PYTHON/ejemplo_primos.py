import time
import os

def primos(n): 
 
    if n < 2: 
        return False 
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0: 
            return False 
    return True

def llenar_lista():
  
    lista = []
    print("Ingresa los numeros a comprobar por primos (ok para terminar):")
    
    while True:
        entrada = input().lower() 
        if entrada == "ok":
            break
            
        try:
            numero = int(entrada)
            lista.append(numero)
        except ValueError:
            print("ATENCIÓN: NUMERO NO VALIDO")
            
    return lista

def contar_primos(lista_numeros):
    
    contador_primo = 0
    lista_primos = []
    
    for numero in lista_numeros:
        if primos(numero):
            contador_primo += 1
            lista_primos.append(numero)
            
    return contador_primo, lista_primos


if __name__ == "__main__": # buscado como "norma de buenas costumbres" al momento de crear y 
                           # documentar códigos, así el main y este código se ejecuta solo si se presiona RUN. Puedo, gracias a esto
                          #llamar a una función como si fuera herramienta propia y no ejecutar todo el código suelto.
    os.system('cls' if os.name == 'nt' else 'clear') # borra pantalla para limpiar terminal
    print("--------- BUSCADOR DE PRIMOS --------\n")
    print("Este programa busca números primos dentro de una lista.")
    print("Primero, ingrese una lista de números para comprobar su 'primosidad':")
    
    # Carga de datos
    mi_lista = llenar_lista()
    print("\nTu lista está LISTA para ser 'primoseada': ", mi_lista)
    time.sleep(2)
    
    # Simulación de procesamiento (Animación), encontrada en internet
    # para hacer mas ' amigable ' el programa
    tempo = ""
    for i in range(5):
        tempo = tempo + "." 
        time.sleep(0.5) 
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Procesando" + tempo)
    
    # Procesamiento usando la nueva función requerida
    cantidad, los_primos = contar_primos(mi_lista) # al ser una tupla, devuelve 2 valores ubicados
    
    # Despliegue de resultados
    print(f"Se encontraron {cantidad} números primos en tu lista.")
    print("Los números primos son:")
    print(los_primos)