from operator import le


tupla = ('asdf',4,(34,45),[3.4],'pepe')

print('-'*20)
print(type(tupla))
print(tupla)
print(tupla[1])

print('-'*20)
tupla1 = ()
print(tupla1)

print('-'*20)
tupla2= (3,) #tenemos que poner la coma para que no sea un entero
print(tupla2)
print(type(tupla2))

print('-'*20)
print((tupla2+tupla))

print('-'*20)
print((tupla)*5)

print('-'*20)
print(tupla[1:]) # como en listas 

print('-'*20) 
#desepaquetar o colocar los elementos de la tupla y seleccionarlos a un nombre
tupla3 = ('paco','pepe','pedro') 
nom1, nom2,nom3 = tupla3 #tiene que ser de la misma longitud de la tupla 
print(nom2)

print('-'*20)
tupla4= ('paco','pepe','ana') 
print(tupla3 == tupla4) #para ser iguales tienen que tener los mismos elementos y orden de ellos
print(tupla3 < tupla4) # compara elemento a elemento 

print('-'*20)
for i in range(len(tupla)):
    print(tupla[i])
print('-'*20)
for elemento in tupla:
    print(elemento)
print('-'*20)

#si el elemnto que esta en la tupla es una lista si se puede modificar esa lista 
print(tupla[3])

tupla[3][0] = 34

print(tupla)
#se puede editar y utilizar als cosas de la lista 

print('-'*20)
#hace una copia de la tupla y la pasa a lista 
tistafrmtupla = list(tupla)
print(tistafrmtupla)


print('-'*20)

lsita= [1,2,3,4]

tuplafromlista = tuple(lsita)
print(tuplafromlista)
print(type(tuplafromlista))

print('-'*20)
