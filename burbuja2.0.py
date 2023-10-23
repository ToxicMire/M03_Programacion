import random

lista = []
for i in range(20):
    lista.append((random.randint(0, 1000)))
print('*'*80)
print(lista)
for i in range(len(lista)-1):
    for j in range(len(lista)-1 - i):
        if lista[j] > lista[j + 1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]

print('*'*80)
print("La lista ordenada ^.^")
print('*'*80)
print(lista)