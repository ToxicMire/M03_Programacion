import random

lista = []
for i in range(20):
    lista.append((random.randint(0, 100)))
print(lista)
for i in range(len(lista)):
    for j in range(len(lista)-1):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
print(lista)
