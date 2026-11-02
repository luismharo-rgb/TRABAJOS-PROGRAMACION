class Nodo:
    def __init__(self, key):
        self.izq = None
        self.der = None
        self.val = key

# =====================================================================
# 1. FUNCIÓN PARA INSERTAR (Mantiene el árbol auto-ordenado)
# =====================================================================
def insertar(nodo, valor):
    if nodo is None:
        return Nodo(valor)
    if valor < nodo.val:
        nodo.izq = insertar(nodo.izq, valor)
    else:
        nodo.der = insertar(nodo.der, valor)
    return nodo

# =====================================================================
# 2. RECORRIDO INORDEN (Extrae los datos ya ordenados)
# =====================================================================
def recorrido_inorden(nodo):
    if nodo is not None:
        # 1. Ir lo más a la izquierda posible (valores más chicos)
        recorrido_inorden(nodo.izq)
        
        # 2. Procesar la raíz actual
        print(nodo.val, end=" ")
        
        # 3. Ir a la derecha (valores más grandes)
        recorrido_inorden(nodo.der)

# =====================================================================
# 3. PRUEBA EN VIVO
# =====================================================================

# Tu inventario desordenado
inventario_desordenado = [105, 103, 101, 104, 102]
print(f"1. Lista desordenada original: {inventario_desordenado}\n")

# Creamos la raíz con el primer elemento
raiz = Nodo(inventario_desordenado[0])

# Insertamos el resto de los elementos en el árbol
for producto in inventario_desordenado[1:]:
    insertar(raiz, producto)

print("2. Insertando elementos en el árbol...")
print("¡El árbol se acomodó solo en memoria!")

print("\n3. Extrayendo datos con recorrido Inorden:")
recorrido_inorden(raiz)
print() # Salto de línea limpio para la terminal
