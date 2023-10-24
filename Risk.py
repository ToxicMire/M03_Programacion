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

# ramdom quien empieza 
ini = random.randrange(1,2)

# guardar los datos
for i in range(4):
    dado = random.randint(1,6)
    if i == 0:
        lista_jugadores[1][1].append(dado) 
                      
    for j in range(len(lista_jugadores[1][1])):
        if dado > lista_jugadores[1][1][j]:
            lista_jugadores[1][1].insert(j,dado)
            break
        if j == len(lista_jugadores[1][1])-1 and dado<= lista_jugadores[1][1][j]:
            lista_jugadores[1][1].append(dado)
            
print(lista_jugadores)

#dados 



# se comparan los dados de mayo a menor solo los 3 de cada uno



# se ordenan los usuarios por los puntos 

# se suman o restan putos por cada dado que pierdan o ganen 