lista = [2,3,'cadena1','cadena2',3,3.5,True,False,['a','b','c'],'lalala',3]

print(len(lista)) #Nº DE LAS POSICIONES DE LA LISTA
print('cadena1' in lista) #encontrar info en las listas
print(lista.index('cadena2')) # posicion donde se encuentra el primer numero a no se que se explique  .index(a,b,c) mirar info 
print(lista.count(3)) #veces que aparece el elemento en la lista 
lista[3] = 'X' #cambia el valor en la posicion por la lista
print(lista)
lista.append('X')# se añade elemento al final
lista.insert(2,'x') 
lista.remove('x') #solo elimina el primero 
#para eliminar buscar y añadir todo a una nueva lista 
lista[2:8] = [1,2,3]#sustituye todo lo que este en esas posiciones 


elemento = 3

if elemento in lista:
    posicion = 0
    for i in range(lista.count(elemento)):
        print(lista.index(elemento,posicion))
        posicion = lista.index(elemento,posicion)+1
        
else:
    print('{} no esta en la lista'.format(elemento))
########################################################################
lista = [34,54,234,34,65]
lista = ['123','abc','9']
print(max(lista)) # el maximo
print(min(lista)) # el minimo

########################################################################
lista1 = [1] # aun que lo pongas vacio es una lista 
print(type(lista1))

lista2 = 'aeiou'
print(lista[2]) # dice la posicion de la lista 