import random
#info
dado0,dado1,dado2 = 0,0,0
separador = '-'*80
titulo = 'El juego del 10000'
Titulo = titulo.center(80,'-') 
normas = 'Normas del juego'
Normas = normas.center(80,'*') 
reglas = 'Gana quien llegue a 10000 pt antes, jugaras contra una ia.\n\nReglas: \n\n -Si alguien consigue un trio de numero 1 = 1000 pt \n -Si no tenemos un trio de 1 pero si un par de 1 se añaden +100pt adicionales \n -Cualquier trio de cualquier numero diferente a 1 cale *100 el numero de dados \n -Cualquier dado que tenga un 5 obtendra 50 pt adicionales'
separador2 = '*'*80
nombre = 'Dime tu nombre jugador '
saludo = 'Hola {}'
tirada = 'Presiona enter para ver la tirada de {}'
boot = 'IA'
dados = 'Dado1 = {}, Dado2 = {} , Dado3 = {}'
d1 = 0
d2 = 0
d3 = 0
puntosia = 0
puntosjuga = 0
continuar = 'True'
puntostotal = 10000
Puntos = 'Los puntos del jugador son {} los puntos de la ia son {} '
Pregunta= 'Quieres seguir jugando? True/False '

#programa 
print(separador)
print(Titulo)
print(separador)
print()
print(separador2)
print(Normas)
print(separador2)
print()
print(reglas)
print(separador)
print(nombre)
nom = input('> ')
print(separador)
print(saludo.format(nom))
print(separador)
while True:

    while puntosia<puntostotal and puntosjuga<puntostotal  :
                           
            #ia
            print(tirada.format(boot))
            input()
            #random
            dado0 = random.randint(1,6)
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            d1 = dado0
            d2 = dado1
            d3 = dado2
            print(dados.format(dado0,dado1,dado2))
            #print(d1,d2,d3)
            
            
            if d1 and d2 and d3 == d1:
                    aux = (d1+d2+d3) * 100
                    puntosia += aux 
                    print('Puntos extra por numero de trio {} pt'.format(aux))

            if d1 and d2 and d3 == 1:
                    puntosia += 1000
                    print('Trio de numero 1 + 1000 pt')
                #pareja de 1
            elif (d1 and d2) or (d1 and d3) or (d2 and d3) == 1:
                    aux= d1+d2+d3
                    puntosia += 100 + aux
                    print('Puntos extra por pareja de numero 1 + 100 pt')
            else:
                    if d1 or d2 or d3 == 5:
                        aux= d1+d2+d3
                        aux1= 50
                        puntosia += aux+ aux1
                    else:
                        puntosia += d1+d2+d3
            print(separador2)

            #jugador
            print(tirada.format(nom))
            input()
            #random
            dado0 = random.randint(1,6)
            dado1 = random.randint(1,6)
            dado2 = random.randint(1,6)
            d1 = 1
            d2 = 1
            d3 = 1
            print(dados.format(dado0,dado1,dado2))
            #print(d1,d2,d3)
            
                #trios
            if d1 and d2 and d3 == d1:
                    aux = (d1+d2+d3) * 100
                    puntosjuga += aux 
                    print('Puntos extra por numero de trio {} pt'.format(aux))

            if d1 and d2 and d3 == 1:
                    puntosjuga += 1000
                    print('Trio de numero 1 + 1000 pt')
                #pareja de 1
            elif (d1 and d2) or (d1 and d3) or (d2 and d3) == 1:
                    aux= d1+d2+d3
                    puntosjuga += 100 + aux
                    print('Puntos extra por pareja de numero 1 + 100 pt')
            else:
                    if d1 or d2 or d3 == 5:
                        aux= d1+d2+d3
                        aux1= 50
                        puntosjuga += aux+ aux1
                    else:
                        puntosjuga += d1+d2+d3
            print(separador)
            print()
            print(Puntos.format(puntosjuga, puntosia))
            print()
            print(separador)
           
    if puntosia > puntostotal :
        print('Gana la ia con {} '.format(puntosia))
        break

    if puntosjuga > puntostotal:
        print('Gana el jugador con {} '.format(puntosjuga))
        break  

    print(Pregunta)
    respuesta =input('> ')

    if respuesta == False:
        print('Abandonas el juego ^.^ Nos vemos a la proxima')
        break
    else:
        puntosia = 0
        puntosjuga = 0
            
            
           
                    
         
        