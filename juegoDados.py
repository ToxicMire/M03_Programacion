import random

nombreJugador = input('Dmie tu nombre: ')
nombreMaquina = 'Matrix'

puntuacionJugador = 0
puntuacionMaquina = 0

turno = 0

d0 = random.randint(0,1)
if d0 == 0:
    turno = 0
else:
    turno = 1

d1 = 0
d2 = 0

while puntuacionJugador < 100 and puntuacionMaquina < 100:
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    print('Tirada = {}'.format(d1+d2))
    if (d1 + d2)%2 == 0:
        if turno%2 == 0:
            print('{} No suma puntos'.format(nombreMaquina))
        else:
            print('{} No suma puntos'.format(nombreJugador))
    if (d1 + d2)%2 != 0:
        if turno%2 == 0:
            print('{} Suma puntos'.format(nombreMaquina))
            puntuacionMaquina += (d1+d2)
        else:
            print('{} Suma puntos'.format(nombreJugador))
            puntuacionJugador += (d1 + d2)
    turno += 1
    print('Puntos {} = {}, puntos {} = {}'.format(nombreJugador, puntuacionJugador, \
                                                  nombreMaquina, puntuacionMaquina))
    if (puntuacionJugador >= 100):
        print('Ha ganado {}'.format(nombreJugador))
    if (puntuacionJugador >= 100):
        print('Ha ganado {}'.format(nombreMaquina))
        print()
    input()
