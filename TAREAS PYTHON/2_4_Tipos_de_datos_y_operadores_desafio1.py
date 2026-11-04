# Entrada de datos: Tres números distintos
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

# Verificamos todas las posibles combinaciones 
if a < b < c:
    menor, medio, mayor = a, b, c
elif a < c < b:
    menor, medio, mayor = a, c, b
elif b < a < c:
    menor, medio, mayor = b, a, c
elif b < c < a:
    menor, medio, mayor = b, c, a
elif c < a < b:
    menor, medio, mayor = c, a, b
else:
    menor, medio, mayor = c, b, a

# Mostrar el resultado 
print(f"\nLos números ordenados son: {menor} < {medio} < {mayor}")
