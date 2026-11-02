import random
import time

class Nodo:
    def __init__(self, key):
        self.izq = None
        self.der = None
        self.val = key

# =====================================================================
# 1. FUNCIÓN PARA INSERTAR UN ELEMENTO EN EL LUGAR CORRECTO (BST)
# =====================================================================
def insertar_en_arbol(nodo, nuevo_valor):
    # Si el espacio está vacío, creamos el nuevo nodo aquí
    if nodo is None:
        return Nodo(nuevo_valor)
    
    # Si el valor ya existe, no lo duplicamos (opcional en inventarios)
    if nuevo_valor == nodo.val:
        return nodo
    
    # Si es menor, va a la rama izquierda
    if nuevo_valor < nodo.val:
        nodo.izq = insertar_en_arbol(nodo.izq, nuevo_valor)
    # Si es mayor, va a la rama derecha
    else:
        nodo.der = insertar_en_arbol(nodo.der, nuevo_valor)
        
    return nodo

# =====================================================================
# 2. FUNCIÓN PARA DIBUJAR EL ÁRBOL EN LA CONSOLA
# =====================================================================
def dibujar_arbol(nodo, prefijo="", es_izq=True):
    if nodo is not None:
        dibujar_arbol(nodo.der, prefijo + ("│   " if es_izq else "    "), False)
        print(prefijo + ("└── " if es_izq else "┌── ") + str(nodo.val))
        dibujar_arbol(nodo.izq, prefijo + ("    " if es_izq else "│   "), True)

# =====================================================================
# 3. PRUEBA EN VIVO CON NÚMEROS ALEATORIOS
# =====================================================================

# Iniciamos el árbol con un producto base en el centro (ej. 50)
raiz = Nodo(50)
print("Árbol inicial con raíz 50:")
dibujar_arbol(raiz)
print("-" * 40)

# Vamos a generar e insertar 5 productos aleatorios entre 1 y 100
for i in range(5):
    time.sleep(1.5)  # Pausa de 1.5 segundos para simular "tiempo de pensamiento"
    
    codigo_aleatorio = random.randint(1, 100)
    print(f"\nGenerando código aleatorio: {codigo_aleatorio}...")
    print("Insertándolo en la posición correcta...")
    
    # Insertamos el número en el árbol
    raiz = insertar_en_arbol(raiz, codigo_aleatorio)
    
    # Mostramos cómo va quedando el árbol modificado
    print("\nEstructura actual del árbol:")
    dibujar_arbol(raiz)
    print("-" * 40)
