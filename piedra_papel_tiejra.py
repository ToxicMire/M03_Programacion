#eje 3
import random

piedra = 1
papel = 2
tijera = 3


while True:
    elecionia= random.randint(1,3)
    print('-'*60)
    print('Vamos a jugar a piedra, papel o tijera \n1.-Piedra 2.-Papel 3.-Tijera  ')
    print('Un dos tres piedra papel y tijera ...')
    print('-'*60)
    print('La ia ya tiene su eleccion ...')
    print('-'*60)
    eleccionpersona = int(input('Cual es la tuya > '))

    if elecionia == eleccionpersona:
        print('Eleccion de la ia  {}  tu eleccion  {} '.format(elecionia,eleccionpersona))
        print('Empate')
        print(elecionia)
        print(eleccionpersona)
    #ganar
    if (elecionia == 1 )and (eleccionpersona == 2 ):  # piedra papel 1 2 tu 
        print('Eleccion de la ia  {} piedra   tu eleccion  {}  papel '.format(elecionia,eleccionpersona))
        print('Has ganado ')
        break

    if (elecionia == 2 )and (eleccionpersona == 3 ): # papel tijera 2 3 tu 
        print('Eleccion de la ia  {}  papel tu eleccion  {}  tijera'.format(elecionia,eleccionpersona))
        print('Has ganado ')
        break

    if (elecionia == 3 )and (eleccionpersona == 1 ):# tijera piedra 3 1 tu 
        print('Eleccion de la ia  {}  tiejera  tu eleccion  {}  piedra '.format(elecionia,eleccionpersona))
        print('Has ganado ')
        break


    #perder
    if (elecionia == 2 )and (eleccionpersona == 1 ): # palpel piedra 2 1 ia
        print('Eleccion de la ia  {}  papel tu eleccion  {} piedra '.format(elecionia,eleccionpersona))
        print('Has perdido ')
        break

    if (elecionia == 3 )and (eleccionpersona == 2 ): # tiejera papel 3 2 ia
        print('Eleccion de la ia  {}  tijera  tu eleccion  {} papel '.format(elecionia,eleccionpersona))
        print('Has perdido ')
        break

    if (elecionia == 1 )and (eleccionpersona == 3 ): # piedra tijera 1 3 ia 
        print('Eleccion de la ia  {} piedra tu eleccion  {} tijera '.format(elecionia,eleccionpersona))
        print('Has perdido ')
        break
    

