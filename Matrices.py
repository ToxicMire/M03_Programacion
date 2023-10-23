import random

matriz = []
Filas = 3
Columnas = 3

for i in range(Filas):
    matriz.append([])
    for j in range(Columnas):
        matriz[i].append(random.randint(0, 20))

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(str(matriz[i][j]).rjust(5), end="")
    print()

# Ordenar matriz
for f in range(len(matriz)):
    for i in range(len(matriz)-1):
        for j in range(len(matriz)-1-i):
            if matriz[f][j] > matriz[f][j+1]:
                matriz[f][j], matriz[f][j+1] = matriz[f][j+1], matriz[f][j]

print('*'*22)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(str(matriz[i][j]).rjust(5), end="")
    print()

print("Listo esta ordenado todo :)")