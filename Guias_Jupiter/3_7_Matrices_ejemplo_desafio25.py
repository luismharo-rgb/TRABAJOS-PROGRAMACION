"""
ATENCION: NO TOMAR EN CUENTA ESTE EJERCICIO, NO LO HICE YO SINO QUE LO PEDI A UNA IA, SOLO LO PONGO
PARA VER COMO FUNCIONA, NO ES PARTE DE LA GUIA
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ==========================================
# 1. CREAR EL TABLERO DE JUEGO
# ==========================================
def crear_tablero(n, m, patron="aleatorio"):
    """
    Crea una matriz de n x m con estados iniciales (0 o 1).
    """
    if patron == "aleatorio":
        # Llena la matriz con 0s y 1s de forma aleatoria (20% de probabilidad de estar vivo)
        return np.random.choice([0, 1], size=(n, m), p=[0.8, 0.2])
    
    elif patron == "glider":
        # Un patrón famoso ("planeador") que se desplaza infinitamente por el tablero
        tablero = np.zeros((n, m))
        tablero[1, 2] = 1
        tablero[2, 3] = 1
        tablero[3, 1:4] = 1
        return tablero
    
    return np.zeros((n, m))

# ==========================================
# 2. DEFINIR LAS REGLAS DEL JUEGO
# ==========================================
def actualizar_tablero(tablero):
    """
    Aplica las reglas de Conway para calcular la siguiente generación del tablero.
    """
    n, m = tablero.shape
    nuevo_tablero = tablero.copy()
    
    # Recorremos cada celda del tablero
    for i in range(n):
        for j in range(m):
            # 1. Contar los 8 vecinos de la celda (i, j) usando rebanado de matriz
            # Se usa max/min para evitar salirnos de los bordes del tablero
            vecinos_vivos = np.sum(tablero[max(0, i-1):min(n, i+2), max(0, j-1):min(m, j+2)]) - tablero[i, j]
            
            # 2. Aplicar las reglas de evolución
            if tablero[i, j] == 1: # Si la celda está VIVA
                if vecinos_vivos < 2 or vecinos_vivos > 3:
                    nuevo_tablero[i, j] = 0 # Muere por subpoblación o sobrepoblación
            else:                  # Si la celda está MUERTA
                if vecinos_vivos == 3:
                    nuevo_tablero[i, j] = 1 # Nace por reproducción
                    
    return nuevo_tablero

# ==========================================
# 3. Y 4. SIMULAR Y VISUALIZAR LA EVOLUCIÓN
# ==========================================
# Configuración inicial del tablero
N, M = 30, 30
tablero = crear_tablero(N, M, patron="aleatorio")

# Configurar el gráfico de Matplotlib para la animación
fig, ax = plt.subplots(figsize=(6, 6))
# cmap="binary" mostrará 0 como blanco y 1 como negro
im = ax.imshow(tablero, cmap="binary")
ax.axis("off") # Ocultar los ejes numéricos

def animar(frame):
    """Función que Matplotlib llamará en cada fotograma para actualizar el juego"""
    global tablero
    tablero = actualizar_tablero(tablero)
    im.set_array(tablero) # Actualiza los datos visuales
    return [im]

# Crear la animación (actualiza cada 200 milisegundos)
ani = animation.FuncAnimation(fig, animar, frames=50, interval=200, blit=True)

plt.show()
