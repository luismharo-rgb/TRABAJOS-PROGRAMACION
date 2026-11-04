lista=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares=0
for num in lista:
    if num % 2 == 0:
        pares += 1
print(f"la cantidad de pares son: {pares}")