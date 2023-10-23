import random
while True:

    nom = input("Dime tu nombre -> ")

    punthuma = 0
    puntmaqu = 0
    dado1 = 0
    dado2 = 0
    dado3 = 0

    # humano

    if punthuma >= 10000:
        print("Ganaste", nom)


        print("Presione cualquier tecla para empezar", nom)
        input()
        print("Tirada de", nom , "->" )
        dado1 = random.randrange(1, 7)
        dado2 = random.randrange(1, 7)
        dado3 = random.randrange(1, 7)
        print("dado1 =", dado1, "dado2 =", dado2, "dado3 =", dado3, "\n \n")

        punthuma = dado1 + dado2 + dado3

        if dado1 == 1 and dado2 == 1 and  dado3 == 1:
            print("Bonus trio,la tirada vale 1000 puntos")
            punthuma = punthuma + 1000
        elif dado1 == 1 and dado2 == 1 or dado1== 1 and dado3 == 1 or dado2== 1 and dado3 == 1:
            print("Bonus por pareja de 1, 100 puntos ")
            punthuma = punthuma + 100
        elif dado1 == 5 or dado2 == 5  or  dado3 == 5:
            print("Bonus por un numero 5, 50 puntos")
            punthuma = punthuma + 50
        print(punthuma)

    if puntmaqu >= 10000:
        print("Gana el Boot")
        # maquina
        print("Presione el intro para ver la tirada del Boot")
        input()
        print("Tirada del Boot ->")
        dado1 = random.randrange(1, 7)
        dado2 = random.randrange(1, 7)
        dado3 = random.randrange(1, 7)
        print("dado1 =", dado1, "dado2 =", dado2, "dado3 =", dado3)

        if dado1 == 5 and dado2 == 5 and  dado3 == 5:
            print("Bonus trio,la tirada vale 1500 puntos")
            puntmaqu = puntmaqu + 1500
        elif dado1 == 1 and dado2 == 1 or dado1== 1 and dado3 == 1 or dado2== 1 and dado3 == 1:
            print("Bonus por pareja de 1, 100 puntos ")
            puntmaqu = puntmaqu + 100
        elif dado1 == 5 or dado2 == 5  or  dado3 == 5:
            print("Bonus por un numero 5, 50 puntos")
            puntmaqu = puntmaqu + 50
        print(puntmaqu)

    opc = input("Quieres seguir jugando? \n \n  Presiona S = Si quiero seguir jugando \n \n Presiona cualquier tecla menos S para dejar de jugar")
    if opc != "S":
        break