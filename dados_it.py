import random
menu="1)new game\n2)new player\n3)show ranking\n4)exit"

jugador=""
bot="bot"
puntosjug=0
puntosbot=0

ranking="'"*10+"raking"+"'"*10+"\n"+"name".ljust(13)+"point".rjust(13)+"\n"+"*"*26
        #"\n"+str(jugador).ljust(13)+str(puntosjug).rjust(13)
datos_ranking=""


menu_actual = 0
while menu_actual >= 0:

    while menu_actual == 0:
    # Obtener opción correcta
        opcion_ok = False
        while not opcion_ok:
            print(menu)
            opc = input(">Opcion: ")
            if not opc.isdigit():
                print("La opcion ha de ser numérica")
                input("Pulse una tecla para continuar...\n")
            else:
                opc = int(opc)
                if opc > 5 or opc < 0:
                    print("La opción ha de estar entre 1 y 4")
                    input("Pulse una tecla para continuar...\n")
                else:
                    opcion_ok = True
        # Tratar opción
        if opc == 1:
            menu_actual = 1
        elif opc == 2:
            menu_actual = 2
        elif opc==3:
            menu_actual=3
        elif opc==4:
            print("Adios")
            break

    while menu_actual == 1:
        ganador = ""
        if jugador=="":
            print("Tienes que introducir tu nombre primero, ve a la >Opcion: 2")
            print(menu)
            opc = input(">Opcion: ")
            #opc = int(opc)
            if not opc.isdigit() or int(opc) not in range(1, 5):
                print("== Opcion Incorrecta!!! ===")
                print(menu)
                opc = input(">Opcion: ")
                if opc == 1:
                    menu_actual = 1
                elif opc == 2:
                    menu_actual = 2
                elif opc == 3:
                    menu_actual = 3
                elif opc == 4:
                    menu_actual = 0
            else:
                opc = int(opc)
                if opc == 1:
                    menu_actual = 1
                elif opc == 2:
                    menu_actual = 2
                elif opc == 3:
                    menu_actual = 3
                elif opc == 4:
                    menu_actual = 0
        else:
            turno = random.randint(0, 1)
            for i in range(10):

                dadosjug = 0
                dadosbot = 0
                dado1jug = 0
                dado2jug = 0
                dado1bot = 0
                dado2bot = 0
                dado1jug += random.randint(1, 6)
                dado2jug += random.randint(1, 6)
                dado1bot += random.randint(1, 6)
                dado2bot += random.randint(1, 6)
                dadosjug += dado1jug + dado2jug
                dadosbot += dado1bot + dado2bot
                tirada = "Tirada {}".format(i)
                turno += 1
                print(tirada)
                if turno%2==0:
                    print("turno de {}".format(jugador))
                    print("dado1 = {} , dado2 = {}. sum = {}".format(dado1jug, dado2jug, dadosjug))
                    if dadosjug%2==0:
                        if dado1jug>dado2jug:
                            print("Bien!! {} gana {} puntos".format(jugador, dado1jug))
                            puntosjug= puntosjug + dado1jug
                            print("{}: {} puntos".format(jugador,puntosjug))
                            print("{}: {} puntos".format(bot,puntosbot))
                        elif dado2jug>dado1jug:
                            print("Bien!! {} gana {} puntos".format(jugador, dado2jug))
                            puntosjug= puntosjug + dado2jug
                            print("{}: {} puntos".format(jugador, puntosjug))
                            print("{}: {} puntos".format(bot, puntosbot))
                    elif dadosjug%2!=0:
                        if dado1jug>dado2jug:
                            print("Mala suerte!! {} pierde {} puntos".format(jugador, dado2jug))
                            puntosjug = puntosjug - dado2jug
                            print("{}: {} puntos".format(jugador, puntosjug))
                            print("{}: {} puntos".format(bot, puntosbot))
                        elif dado2jug>dado1jug:
                            print("Mala suerte!! {} pierde {} puntos".format(jugador, dado1jug))
                            puntosjug =puntosjug- dado1jug
                            print("{} tiene {} puntos".format(jugador, puntosjug))
                            print("{} tiene {} puntos".format(bot, puntosbot))

                    input(print("Presiona para lanzar los dados..."))

                elif turno%2!=0:
                    print("turno de {}".format(bot))
                    print("dado1 = {} , dado2 = {}. sum = {}".format(dado1bot, dado2bot, dadosbot))
                    if dadosbot%2==0:
                        if dado1bot>dado2bot:
                            print("Bien!! {} gana {} puntos".format(bot, dado1bot))
                            puntosbot =puntosbot + dado1bot
                            print("{}: {} puntos".format(bot, puntosbot))
                            print("{}: {} puntos".format(jugador, puntosjug))
                        elif dado2jug>dado1jug:
                            print("Bien!! {} gana {} puntos".format(bot, dado2bot))
                            puntosjug =puntosbot+ dado2jug
                            print("{}: {} puntos".format(bot, puntosbot))
                            print("{}: {} puntos".format(jugador, puntosjug))
                    elif dadosbot%2!=0:
                        if dado1bot>dado2bot:
                            print("Mala suerte!! {} pierde {} puntos".format(bot, dado1bot))
                            puntosbot =puntosbot- dado1bot
                            print("{}: {} puntos".format(bot, puntosbot))
                            print("{}: {} puntos".format(jugador, puntosjug))
                        elif dado2jug>dado1jug:
                            print("Mala suerte!! {} pierde {} puntos".format(bot, dado2bot))
                            puntosbot =puntosbot- dado2bot
                            print("{}: {} puntos".format(bot, puntosbot))
                            print("{}: {} puntos".format(jugador, puntosjug))

                    input("Presiona para lanzar los dados...")

            if puntosjug>puntosbot:
                print("ha ganado {}".format(jugador))
                ganador+=jugador
                datos_ranking+=str(jugador).ljust(13)+":"+str(puntosjug).rjust(13)+";"
            elif puntosbot>puntosjug:
                print("ha ganado {}".format(bot))
            elif puntosbot==puntosjug:
                print("empate!!")


                print("puntos jug = {} \npuntos bot = {}".format(puntosjug, puntosbot))
                input("Enter para continuar")

            print(menu)
            opc = input(">Opcion: ")
            # Validación alternativa del valor introducido:
            # Funciona bien porque, normalmente, al evaluar un OR
            # la 2a condición solo se evalúa si la primera es falsa
            # (Si la primera es cierta ya se sabe que el OR es cierto y no se sigue evaluando)
            # Inconveniente: el mensaje no distingue no numérico de valor fuera de rango.
            if not opc.isdigit() or int(opc) not in range(1, 5):
                print("== Opcion Incorrecta!!! ===")
                print(menu)
                opc = input(">Opcion: ")
                opc = int(opc)
                if opc == 1:
                    menu_actual = 1
                elif opc == 2:
                    menu_actual = 2
                elif opc == 3:
                    menu_actual = 3
                elif opc == 4:
                    menu_actual = 0
            else:
                opc = int(opc)
                if opc == 1:
                    menu_actual = 1
                elif opc == 2:
                    menu_actual = 2
                elif opc == 3:
                    menu_actual = 3
                elif opc == 4:
                    menu_actual = 0

    while menu_actual == 2:
        jugador=input("Dame tu nombre: ")
        while jugador=="":
            if jugador =="" or jugador==" ":
                print("vuelve a introducir tu nombre.")
                jugador = input("Dame tu nombre: ")
                print("Hola {}, vamos a jugar".format(jugador))
            else:
                print("Hola {}, vamos a jugar".format(jugador))

        print(menu)
        opc = input(">Opcion: ")
        # Validación alternativa del valor introducido:
        # Funciona bien porque, normalmente, al evaluar un OR
        # la 2a condición solo se evalúa si la primera es falsa
        # (Si la primera es cierta ya se sabe que el OR es cierto y no se sigue evaluando)
        # Inconveniente: el mensaje no distingue no numérico de valor fuera de rango.
        if not opc.isdigit() or int(opc) not in range(1,5):
            print("== Opcion Incorrecta!!! ===")
            print(menu)
            opc = input(">Opcion: ")
            opc = int(opc)
            if opc == 1:
                menu_actual = 1
            elif opc == 2:
                menu_actual = 2
            elif opc == 3:
                menu_actual = 3
            elif opc == 4:
                menu_actual = 0
        else:
            opc = int(opc)
            if opc == 1:
                menu_actual = 1
            elif opc == 2:
                menu_actual = 2
            elif opc == 3:
                menu_actual = 3
            elif opc==4:
                menu_actual=0

    while menu_actual == 3:
        if ganador==jugador:
            print(ranking+"\n"+datos_ranking)
        else:
            print(ranking)
        print(menu)
        opc = input("\n"+">Opcion: ")
        if not opc.isdigit() or int(opc) not in range(1,5):
            print("== Opcion Incorrecta!!! ===")
            print(menu)
            opc = input(">Opcion: ")
            opc = int(opc)
            if opc == 1:
                menu_actual = 1
            elif opc == 2:
                menu_actual = 2
            elif opc == 3:
                menu_actual = 3
            elif opc == 4:
                menu_actual = 0
        else:
            opc = int(opc)
            if opc == 1:
                menu_actual=1
            elif opc == 2:
                menu_actual=2
            elif opc == 3:
                menu_actual = 3
            elif opc==4:
                menu_actual=0