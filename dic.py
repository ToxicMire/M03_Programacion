# diccionario = {"clave1":"valor1", 23:"valor2", (2,3):"valor3", 21:[2,3,4,(5,6[7,8])]       }
# # diccionario
# print(diccionario[23])
# print(diccionario[(2,3)])
# print(diccionario[21])
#
# diccionario["clave2"]=[4,5,6]
# print(diccionario["clave2"])
# diccionario["clave1"] = (5,6,7)


# diccionarios
dicionario = {}
print(dicionario)
dicionario[5] = [5,6,7]
dicionario[6] = [5,6,7,6,7]
dicionario["clave1"] = "valor 1"
print(dicionario)


for t in dicionario:
    print(t) #imprime las claves del dicionarios
    print(dicionario[t])

del(dicionario["clave1"])
print(dicionario)
dicionario.clear() #limpia el contenido del diccionario
print(dicionario)


# copia de diccionario
dic2 = dicionario.copy()
print(dic2)

dicionario2 = {}

lista = ["elemento1", "elemento2", "elemento3"]
dicci = dict.fromkeys(lista, "valor por defecto") #crea un diccionario apartir de una lista
print(dicci)

diccc = {'elemento1': 'valor por defecto', 'elemento2': 'valor por defecto', 'elemento3': 'valor por defecto'}

# print(diccc.get["elemento1"])
print(diccc.get("elemento1"))
print(diccc.get("elemento12")) #devuelve none si no existe el elemento
print(diccc.get("elemento12", "valor por defecto"))

print(diccc.keys())
print(list(diccc.keys()))
print(type(list(diccc.keys())))

print(diccc.values())
print(type(list(diccc.values())))

print(len(diccc))


for clave, valor in diccc.items():
    print("clave = ", clave, "/", "valor =" , valor)


diccc["Elemento1"] = (3,4)
print(diccc)