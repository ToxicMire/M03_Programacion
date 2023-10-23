import random

lista = []
for i in range(20):
    lista.append((random.randint(0, 100)))
print(lista)

for i in range(len(lista)-1):
    for j in range(i+1 , len(lista)):
        if lista[i] >  lista[j]:
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux
print("Lista ordenada :)")
print(lista)