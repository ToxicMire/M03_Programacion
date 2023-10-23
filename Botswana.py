import random
#valores que se necesitan
quilometros,sed,cansacio = 0,0,0
cazadores = -20
totalquilo = 200
cantimplora = random.randint(4,10)
begut = 0 
acercando = quilometros -15

#print(quilometros,sed,cansacio,cantimplora)

#opciones del menu 
opcA = 'A.- Beure de la cantimplora'
opcB = 'B.- Velocitat moderada'
opcC = 'C.- A tota velocitat cap endevant'
opcD = 'D.- Para i descansa'
opcE = 'E.- Comprova el teu estat'
opcQ = 'Q.- Sortir'

#Formato de los textos 
separador= '='
linea = '-'
Titulo = ' 🐘 Joc de Elefant 🐘 '
comienzo = 'Benvingut a Botswana!'
introducc = 'Has robar  elefant per salvar-lo de les cruels matances, per aconseguir-ho has de travessar 200 km el desert del Kalahari'
introducc2 = 'Els caçadors furtius volen recuperar el seu elefant i surten en persecució teva!😰 \nHauràs de sobreviure al desert i córrer més que els caçadors bosquimanos.'

print(linea*50)
print(Titulo)
print(linea*50)
print()
print()
print(linea*121)
print(comienzo)
print(linea*121)
print(introducc)
print()
print(introducc2)
print(linea*121)
print()
while True:
    print(opcA)
    print(opcB)
    print(opcC)
    print(opcD)
    print(opcE)
    print(opcQ)
    print()
    opc = input('Que opcion quieres > ')
    if opc == 'A':
        # Si el jugador vol beure de la cantimplora, assegura't que quedin glops a la cantimplora.
        # Si n'hi ha, resta-li 1a la variable glops i retorna la variable set del jugador a zero.
        #  En cas contrari, que imprimeixi error.
        if  cantimplora <= 0:
            print('No tens glops')
            print(linea*50)
        else:
            cantimplora -= 1
            sed == 0
            begut += 1
            print('No tens set')
            print(linea*50)

    if opc == 'B':
        moderado = random.randint(5,12)
        print('Has recorrido {} km '.format(moderado))
        sed += 1
        cansacio += 1
        cazadores += random.randint(7,14)
        quilometros += moderado
        totalquilo -= moderado
        print(linea*50)

    if opc == 'C':
        totavelo = random.randint(5,12)
        print(totavelo)
        sed += 1
        cansacio += 1
        cazadores += random.randint(7,14)
        quilometros += totavelo
        totalquilo -= totavelo
        print('Has recorrido {} km '.format(totavelo))
        print(linea*50)

    if opc == 'D':
        cansacio == 0
        print('Se alegra per descansar')
        cazadores += random.randint(7,14)
        print(linea*50)


    if opc == 'E':
        print('Kilòmetres recorreguts : {}'.format(quilometros))
        print('Vegades que has begut de la cantimplora: {}'.format(begut))
        print('Glops que et queden : {}'.format(cantimplora))
        print('Els Bosquimanos son a {} kilòmentres darrere teu!'.format(cazadores))
        print('La distancia que queda {}'.format(totalquilo))
        print(linea*50)

    if opc == 'Q':
        break
    
    if sed > 4:
        print('Tens sed')
    
    if sed >=6: 
        print('Has muerto de sed')
        break
    if cansacio >= 5:
        print('El teu elefant esta cansat')
    if cazadores > quilometros:
        print('Ets capturat')
        break
    if cazadores> acercando:
        print('los cazadores se acercan')
    
    if totalquilo <0:
        print('Has ganado')