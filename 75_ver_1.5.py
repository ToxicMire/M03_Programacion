import random 
from colorama import init, Fore, Back, Style #Cambia el color del texto 

 # Normas, descripcion y objetivo
print(Fore.CYAN) #Cambia el color de la fuente a cian
print("***************************************************************************************************************************************************************************************")
print("*                                                                                                                                                                                     *")
print("*                                                                  7,5                                                                                                                *")
print("*                                                                                                                                                                                     *")
print("***************************************************************************************************************************************************************************************")
print("Descripción                                                                                                                                                                           *")
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*") 
print("Es un juego de cartas de baraja española con 40 cartas cada carta tiene su valor.                                                                                                     *") 
print("El valor de cada carta corresponde con su numero de carta menos los reyes (12), caballos (11) y sotas (10) que equivalen a medio punto (0,5)                                          *") 
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*") 
print("Objetivo                                                                                                                                                                              *") 
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*") 
print("Conseguir el siete y media o una puntuación más cercana a este valor sin pasarse. La banca juega individualmente contra el jugador.                                                   *") 
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*") 
print("Como se juega ?                                                                                                                                                                       *") 
print("--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------*") 
print("Primero la banca baraja y reparte una carta a cada uno, en este caso solo a la banca y a ti.                                                                                          *") 
print("Después de que tengas tu carta se te sumaran los puntos a tu contador. Si en el contador que tienes es mayor que el 7,5 has perdido, si es menor el tu decides si sigues jugando o no.*") 
print("***************************************************************************************************************************************************************************************")
print(Fore.WHITE) #Coloca el color al que esta de base (blanco)

#jugador 1
print(Fore.BLUE) #Cambia el color de la fuente a amarillo
print("**********************************************") 
print("*                                            *")
print("*             Eres el jugador 1              *")
print("*                                            *")
print("**********************************************") 
print(Fore.WHITE) #Coloca el color al que esta de base (blanco)
print(Fore.BLUE) #Coloca el color a azul
print("JUEGO DE LAS 7 Y MEDIA")
nombre = input("¿Cómo se llama? ")
print(Fore.WHITE) #Coloca el color al que esta de base (blanco)

baraja = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,11,11,11,11,12,12,12,12] 
random.shuffle(baraja)

puntosJugador = 0
turnoJugador = True
puntosCroupier = 0

while turnoJugador:
    print("¿Quiere carta?")
    print("1-Sí")
    print("2-No")
    print("Ha de introducir un 1 o un 2.")
    quiereCarta = int(input())
    if quiereCarta == 1:
        carta = baraja.pop(0)
        print(Fore.YELLOW) #Coloca el color a amarillo
        print(f"La carta que le ha salido es {carta}")
        if carta >=10:
            puntosJugador += 0.5
        else:
            puntosJugador += carta
        print(f"Puntuación total: {puntosJugador}")
        print(Fore.WHITE) #Coloca el color al que esta de base (blanco)
        if puntosJugador > 7.5:
            break
    elif quiereCarta == 2:
        print(Fore.GREEN) #Coloca el color a verde
        print(f"Te has plantado con {puntosJugador} puntos, ahora es turno del CROUPIER.")
        print(Fore.WHITE) #Coloca el color al que esta de base (blanco)
        turnoJugador = False
    else:
        print("Ha de introducir un 1 o un 2.")

if puntosJugador <= 7.5:
    while not turnoJugador:
        if puntosCroupier <= 5.5:
            carta = baraja.pop(0)
            print(f"La carta que le ha salido es {carta}")
            print(Fore.WHITE) #Coloca el color al que esta de base (blanco)
            if carta >=10:
                puntosCroupier += 0.5
            else:
                puntosCroupier += carta
        else:
            print(f"El croupier se planta con {puntosCroupier}. ")
            turnoJugador = True

if puntosJugador > 7.5:
    print(Fore.RED) #Coloca el color a rojo
    print(f"Lo siento {nombre}, has perdido")
    print(Fore.WHITE) #Coloca el color al que esta de base (blanco)
elif puntosCroupier > 7.5:
    print(Fore.GREEN) #Coloca el color a verde
    print(f"Enhorabuena {nombre}, has ganado!!")
    print(Fore.WHITE) #Coloca el color al que esta de base (blanco)
else:
    if puntosJugador <= puntosCroupier:
        print(Fore.RED) #Coloca el color a rojo
        print(f"Lo siento {nombre}, has perdido")
        print(Fore.WHITE) #Coloca el color al que esta de base (blanco)
    else:
        print(f"Enhorabuena {nombre}, has ganado!!")
        print(Fore.WHITE) #Coloca el color al que esta de base (blanco)


#creadores del juego 
######################################
# Nom del programa: 7 i mig          #
# Nom del integrants del grup: 2     #
# Raul Garcia, Sergui y Mireia López #
# Versió del programa: 0.0.0         #
######################################