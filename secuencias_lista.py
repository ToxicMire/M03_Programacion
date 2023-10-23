lista = []
print('*'*60)
print(type(lista))

lista= ['fnenwfie',5,0.2,'fjesjfe',5,'pepe',5,[2,3,4],'fjesjfe',[2,3,4],5,5]

print(lista)
print('*'*60)
#añadir elemento
#lista.append([7,5,6])
print(lista)
print('*'*60)
#borrar elemento
lista.remove('fjesjfe')
print(lista)
print('*'*60)
lista.remove([2,3,4])
print(lista)
print('*'*60)
lista.remove(lista[3])
print(lista)
print('*'*60)
#clonar una lista

lista2 = lista
print(lista2)
print('*'*60)
#acceder a un elemento de la lista 
print(lista[0])
print('*'*60)
#tamaño de la lista
print(len(lista))
print('*'*60)
#modificar un elemento de la lista
lista[2] = 36
#lista[7][0] = 'pepe'
print(lista)
print('*'*60)


#ordenar una lista

print(lista.index(5))
print('*'*60)
print(lista.index(5,4))
print('*'*60)
#como saber si existe ese elemento

print(4 in lista)
print('*'*60)
#saber si existe un elemento en la lista
print(lista.count(5))
print('*'*60)
#todos los elementos iguales en una lista 
print(lista)
inicio = 0
for i in range(lista.count(5)):
    print(lista.index(5,inicio))
    inicio = lista.index(5,inicio)+1
print('*'*60)

# info de la lista incluye el primero pero no el ultimo
print(lista[2:4])
print(lista[2:])#coge todo hasta al final
print(lista[:5])#coge todo hasta el num
#para stituir y añadir un nuevo elemento  
# print(lista[2:5]) = ['a','b','c'] 



