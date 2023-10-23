nombres = []
lista1=['Cristina-Anabel-Raul']
lista2=['Maria-Anabel-Raul']
lista3=['Gio-Galo-Anna']

nombres.append(lista1)
nombres.append(lista2)
nombres.append(lista3)

print(nombres)

posiciones =[]
for n in range(len(nombres)):
    posiciones.append([])
    if '-' in nombres[n][0]:
        init = 0
        while '-' in nombres[n][0][init:]:
            print('init=', init)
            posguion = (nombres[n][0][init:]).index('-')
            posguion +=init
            print('nombres [n][0][init:] =',nombres[n][0][init:])
            print('posicion =',posguion)
            posiciones[n].append(posguion)
            int= posguion+1

        



#


