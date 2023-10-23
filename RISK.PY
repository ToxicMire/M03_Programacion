import random
separador= '*'

dado1 = 0
dado2 = 0

dadoata1 = 0 
dadoata2 = 0 
dadoata3 = 0 

dadodef1 = 0
dadodef2 = 0 

#orden de los dados 1 = A , 2= B , 3=C del atacante
dadoA = 0 
dadoB = 0
dadoC = 0


# se miran los dos dados con el punto mas alto y se comparan los 2 dados de cada lado  si es empate gana atacante
print(separador*73)
print((separador)*25+' Vamos a jugar al risk '+(separador)*25)
print(separador*73)

print('Vamos a seleccionar el atacante y el defensor . . .')

numeroia =  random.randint(1,2)
print('Es 1 o 2')
numeropersona = int(input('Dime el numero > ' ))
if numeropersona == numeroia:
        print('Eres el atacante')
else: 
    print('Eres el atacante')
print(separador*73)
#vidas y contadores
print('Ahora vamos a elejir el numero de ejercitos del defensor y el atacante ')
ejercitos =  int(input('> '))

ejercitosDefensor = ejercitos
ejercitosAtacante = ejercitos

while (ejercitosDefensor > 0 )or (ejercitosAtacante > 0):

    print('Vamos a lanzar los dados ')
    print('Al ser atacante tienes 3 dados por lanzar')
    print('Lanzamos el primer dado > ')
    print('Presiona enter...')
    input()
    dadoata1 = random.randint(1,6)
    print('Resultado dado 1 = ',dadoata1)
    print('Presiona enter...')
    input()
    dadoata2 = random.randint(1,6)
    print('Resultado dado 2 = ',dadoata2)
    print('Presiona enter...')
    input()
    dadoata3 = random.randint(1,6)
    print('Resultado dado 3 = ',dadoata3)
    print('-'*73)
    print('Tus dados son {} - {} - {}'.format(dadoata1,dadoata2,dadoata3))
    print('-'*73)
    print()
    print('Estos son los dados de la ia como es defensor tiene 2 dados')
    print('Presiona enter para que la ia tire ...')
    input()
    dadodef1 = random.randint(1,6)
    dadodef2 = random.randint(1,6)
    print('-'*73)
    print('Sus dados son {} - {} '.format(dadodef1,dadodef2))
    print('-'*73)
    print()
    print()

    #ordenar los dados del defensor

    #dado 1 mas grande de dado 2
    if dadoata1 > dadoata2:
        dadoA = dadoata1
        dadoC = dadoata2
    else:
        dadoA = dadoata2
        dadoC = dadoata1

    #dado 3 mas grande de dadoB
    if dadoata3 < dadoC:
        dadoB = dadoC
        dadoC = dadoata3
        
    else: 
        dadoB = dadoata3
    #dado A es mas grande de dadoB
    if dadoA < dadoB:
        aux = dadoA
        dadoA = dadoB
        dadoB= aux

    #ordenar los dados del defensor
    if dadodef1 < dadodef2:
        #en este caso no estan ordenados, los ordenamos
        aux = dadodef1
        dadodef1 = dadodef2
        dadodef2 = aux

    print(separador*73)
    print('Vamos a comprobar los dados del atacante')
    print(dadoA,dadoB)
    print('-'*73)
    print('Vamos a comprobar los dados del defensor')
    print(dadodef1,dadodef2)
    print(separador*73)

    #contador de la ronda
    print('Primeros dados > ')
    if dadoA > dadodef1:
        ejercitosDefensor -=1
        print('Defensor pierde Ejercito')
    if dadoA <= dadodef1:
        ejercitosAtacante -= 1
        print('Atacante pierde ejercito')
    print('-'*73)

    print('Segundos dados > ')
    if dadoB > dadodef2:
        ejercitosDefensor -=1
        print('Defensor pierde Ejercito')
    if dadoB <= dadodef2:
        ejercitosAtacante -= 1
        print('Atacante pierde ejercito')
    print('-'*73)

    print(separador*73)
    #vidas

    print('Los ejercitos que le quedan al atacante -{}- \nLos ejercitos que le quedan defensor son -{}-'.format(ejercitosAtacante,ejercitosDefensor))

    print(separador*73)
    input()
    print('-'*73)
    print()
    print(separador*73)
    print()

print('-'*73)
print('Juego terminado ya tenemos un ganador')
print('-'*73)
print()
print(separador*73)
print()