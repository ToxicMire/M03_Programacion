'''
Partimos de una lista de jugadores, representados por listas. Todos los jugadores empiezan con 100 puntos.
La lista esta siempre ordenada decrecientemente por los puntos de los jugadores
lista_jugadores = [jugador1, jugador2, ...,jugadorN ]
se escogen 2 jugadores de la lista aleatoriamente.
jugador = ["Nombre",[dado1,dado2,dado3],puntos]
atacante tira 5 dados y defensor 3. se guardan los dados ordenados.
atacante aleatorio entre los dos jugadores. El atacante juega sus 3 dados ordenados mayores contra los 3 dados
ordenados del defensor uno a uno y en orden.
el mayor dado del atacante contra el mayor dado del defensor, el segundo mayor del atacante contra el segundo
dado mayor del defensor. Es decir, se sigue la lógica del risk, cada dado mayor del atacante resta un punto al
defensor, en caso contrario se le resta un punto al atacante
'''
import random
lista_jugadores = [["Juan",[],100], ["Rakel",[],100],["Raul",[],100],["Maria Isabel",[],100], ["Constantina",[],100], ["Jose Antonio",[],100]]

dadoata1 = 0 
dadoata2 = 0 
dadoata3 = 0
dadoata4 = 0
dadoata5 = 0

dadodef1 = 0
dadodef2 = 0
dadodef3 = 0 