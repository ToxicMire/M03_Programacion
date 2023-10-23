import random
num = 3
lista = []

for i in range(num):
    lista.append([])
    for j in range(num):
        lista[i].append(random.randint(-5,20))



print("Matriz sin ordenar")

for i in range(num):
    print()
    for j in range(num):
        print(str(lista[i][j]).ljust(5),end="")

print()
print("\n********************")


for pasada in range(num-1):
    for comp in range(len(lista)-1-pasada):

        if lista[comp][len(lista) - 1 - comp] > lista[comp+1][len(lista) - 1 - (comp+1)]:

            lista[comp][len(lista) - 1 - comp],  lista[comp + 1][len(lista) - 1 - (comp + 1)] = lista[comp+1][len(lista)- 1 - (comp+1)], lista[comp][len(lista) - 1 - comp]


for i in range(num):
    print()
    for j in range(num):
        print(str(lista[i][j]).ljust(5),end="")
print()

print("Todo listo :)\n")