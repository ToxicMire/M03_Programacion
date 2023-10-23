#lista de opciones, pasos y soluciones 

paso1 = "Está en el inicio del Bosque Maldito,\n" +"Donde se encuentra 3 caminos ... ¿por donde irá?"

Opcion1_1 = "Escoge el camino de la izquierda, a lo lejos se ve un puente colgante.,"

resolucion_opcion_1_1 = "Decidido, piensas que es el camino más rapido. Para atravesar el bosque. "

paso1_1 = "Efectivamente, el puente es el cámino mas corto, no contabas con que el puente se descolgaría y NO SOBREVIVES a la caida." 

Opcion1_2 = "Escoge el camino del centro, del que parecen provenir. Ruidos de ramas al romperse y astillarse …"

resolucion_opcion_1_2 = "Piensas que para ser digno de la espada de las valkirias,\n Debes de afrontar tus miedos y peligros que acechan"

paso1_2 = "Sorteando los peligros, llegas de noche al centro del bosque, y ves clavada en un cadaver una  espada llameante que te susurra al oido...\n¿ Que haces ?"

Opcion1_2_1 = "Arrancas la espada de cuajo. "

resolucion_opcion1_2_1 = "¡La espada es tuya, te invade la ira y la locura y vuelves \n " \
                        "Al poblado..."
paso1_2_1 = "Matas a toda tu gente, e invadido por la tristeza, decides arrancarte la vida."


Opcion1_2_2 = "Atento a lo que dice la espada, escuchas levemente \n" \
              " Las palabras ...matalos a todos ... por lo que decides  No cogerla."

resolucion_opcion1_2_2 = "¡La espada, al ver que eres un hombre fuerte y sensato, \n " \
                            "que eres capaz lo que dice, se entrega a ti como tu fiel\n Aliada."

paso1_2_2 = "Mas fuerte que nunca, decides que es el momento de erradicar el mal junto \n " +\
            " A tu nueva aliada, y te embarcas en una nueva aventura."

paso1_3 = paso1

Opcion1_3 = "Escoge el camino de la derecha, lleno de flores, ardillas …"

resolucion_opcion_1_3 = "¿Que malo puede pasar?, parece salido de Disney.\n Con lo que no contabas es " \
                        "que en realidad has entrado al laberinto Sombrio, \n " \
                        "y al rato vuelves a la misma encruzijada "


#historia
max_lenght = 150
tittle= ' La historia del bosque maldito y sus caminos sinuosos '
gracias = ' GRACIAS POR JUGAR ^.^ Nos vemos en la proxima U.U '

personaje = input('Dime el nombre del persojane > ')
print('Ahora vamos a conocer la historia ^.^')
print('-'*max_lenght)
print('')

#titulo
print('*'*max_lenght)
sides = max_lenght-len(tittle)+1 / 2
if sides % 2 == 0:
        print('*'*int(sides/2) + tittle + '*'*int(sides/2))
else:
        print('*'*int((sides+1)/2) + tittle + '*'*int(sides/2))
print('*'*max_lenght)
print('')
print('Presiona cualquier tecla ... > ')
input()


#Introduccion
print('-'*max_lenght)
print('Nuestro personaje es {} aventurer@. Tu formas parte de la historia '.format(personaje))
print('')
print(paso1)
print('')
print('Presiona cualquier tecla ... > ')
input()
print('')
print('-'*max_lenght)
print('1 >', Opcion1_1)
print('-'*max_lenght)
print('')
print('Presiona cualquier tecla ... > ')
input()
print('-'*max_lenght)
print('2 >', Opcion1_2)
print('-'*max_lenght)
print('')
print('Presiona cualquier tecla ... > ')
print('-'*max_lenght)
print('3 >', Opcion1_3)
print('-'*max_lenght)
print('')
print('Presiona cualquier tecla ... > ')
input()

#primera eleccion
elec1= int(input('Cual camino elijes ? > '))
if elec1 == 1:
        print('')
        print('Presiona cualquier tecla ... > ')
        input()
        print('-'*max_lenght)
        print(resolucion_opcion_1_1)
        print('-'*max_lenght)
        input()
        print('-'*max_lenght)
        print(paso1_1)
        print('-'*max_lenght)

if elec1 == 2:
        print('')
        print('Presiona cualquier tecla ... > ')
        input()
        print('-'*max_lenght)
        print(resolucion_opcion_1_2)
        print('-'*max_lenght)
        print('')
        print('Presiona cualquier tecla ... > ')
        input()
        print('-'*max_lenght)
        print(paso1_2)
        print('-'*max_lenght)
        print('')
        print('Presiona cualquier tecla ... > ')
        input()
        print('-'*max_lenght)
        print('1 >',Opcion1_2_1 )
        print('-'*max_lenght)
        print('')
        print('2 >', Opcion1_2_2 )
        print('-'*max_lenght)
        print('')
        print('Presiona cualquier tecla ... > ')
        input()
        elec2 = int(input(' Cual es tu eleccion ? > '))

        if elec2 == 1:
                print('')
                print('Presiona cualquier tecla ... > ')
                input()
                print('-'*max_lenght)
                print(resolucion_opcion1_2_1)
                print('-'*max_lenght)
                print('')
                print('Presiona cualquier tecla ... > ')
                input()
                print('-'*max_lenght)
                print(paso1_2_1)
                print('-'*max_lenght)
                print(' '*72 ,'FIN')
                print('*'*max_lenght)

        if elec2 == 2:
                print('')
                print('Presiona cualquier tecla ... > ')
                input()
                print('-'*max_lenght)
                print(resolucion_opcion1_2_2)
                print('-'*max_lenght)
                print(paso1_2_2)
                print(' '*72 ,'FIN')
                print('*'*max_lenght)

if elec1 == 3:
        print('')
        print('Presiona cualquier tecla ... > ')
        input()
        print('-'*max_lenght)
        print(resolucion_opcion_1_3)
        print('-'*max_lenght)
        print(paso1_3)
        print('-'*max_lenght)
        print('Así eternamente hasta que mueres')
        print('-'*max_lenght)
        print(' '*72 ,'FIN')
        print('*'*max_lenght)

#Final de programa 
print('')
print('')
print('~'*max_lenght)
sides = max_lenght-len(gracias)+1 / 2
if sides % 2 == 0:
        print('~'*int(sides/2) + gracias + '~'*int(sides/2))
else:
        print('~'*int((sides+1)/2) + gracias + '~'*int(sides/2))
print('~'*max_lenght)
print('')
print('')