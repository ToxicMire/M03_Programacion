cadeana = "abcd"
print(cadeana[3])
print(len(cadeana))
#imprime los elementos de la cadena
#solo si quiero un elemento de una cadena si pones : es el resto del elemento
tupla = (1,"string", 3.4, "otro string")
#tipo de secuencia

print(len(tupla))

for i in range(len(tupla)):
    print(tupla[i])

print(tupla[:3])
#no se inclulle el elemento colocado
print(tupla[2:])
#ahora si se incluye el elemento colocado


print("string" in tupla) #comporbar si el elemento esta dentro de la tupla o lista

tupla1 = (1,"string", 3.4, "otro string", ("1", "2", "3","4","5"))

print(len(tupla1[4])) #logitud de la tupla

print(tupla1[4][1:3])

print(max(cadeana))
# coje el valor mas al  to
print(min(cadeana))
#elije el valor mas chiquito

tupla2 = (3,4,5,6)

print(max(tupla2))

tupla3 = (1,2,3,4,5,)

lista1 = [1,2,3,4,5,6,7,8,9]