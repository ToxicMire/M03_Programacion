import random

usuario = ""
puntuacion_usuario = 0
puntuacion_boot = 0
partidas_jugadas = 0
ranking = []
inicio_nombre = 0
fin_nombre = 0
inicio_puntuacion = 0
fin_puntuacion = 0
Cabezera = 'Juego de los dados'


while True:
    print(Cabezera.center(30,'*'))
    print("1.- Jugar partida")
    print("2.- Crear usuario")
    print("3.- Mostrar ranking")
    print("4.- Salir")
    print()
    opc = input("Selecciona una opción \n>  ")

    #OPC de jugar partida 
    if opc == "1":
        #Comprovamos si existe un usuario 
        if usuario == "":
            print("Debes crear un usuario primero (opción 2).")
            print()
        
        #Comienzo de la partida 
        else:
            print("\n¡Comienza la partida, ", usuario, "! Veremos si tienes suerte\n")
            input("Presiona Enter para iniciar la partida...")
            print()

            #Ponemos Reset puntos partida 
            puntuacion_partida = 0 

            #Los 50 Turnos de juego
            for i in range(50):
                input(f"Turno {i + 1}: Presiona Enter para lanzar los dados...")
                
                #Lanzamos dados
                turno_usuario = random.randint(1, 6)
                turno_boot = random.randint(1, 6)

                suma_dados = turno_usuario + turno_boot 

                #Compro que sean pares
                if suma_dados % 2 == 0:
                    puntuacion_usuario += turno_usuario if turno_usuario > turno_boot \
                        else turno_boot
                        
                #Compro que no son pares
                else:
                    puntuacion_usuario -= turno_usuario if turno_usuario < turno_boot \
                        else turno_boot

                puntuacion_boot += turno_usuario if turno_usuario > turno_boot \
                    else turno_boot

                #Enseñamos los resultados 
                print(f"Turno {i + 1}: {usuario} obtiene {turno_usuario} y el boot obtiene {turno_boot}")
                print()
                
                # Sumar la puntuación de la partida actual
                puntuacion_partida += turno_usuario if turno_usuario > turno_boot \
                    else turno_boot 
                    
            #Gestion de los resultados
            if puntuacion_usuario > puntuacion_boot:
                print("\n¡", usuario, " has ganado la partida con", puntuacion_usuario, " puntos!")
                
            elif puntuacion_boot > puntuacion_usuario:
                print("\nEl Boot ha ganado la partida con", puntuacion_boot, "puntos. Casi lo consigues")
                
            else:
                print("\n¡Ha habido un empate! Que mala suerte")

            # Agregar el usuario y su puntuación a la lista de ranking
            ranking.extend((usuario, puntuacion_usuario))

        # Reiniciar las puntuaciones para la próxima partida
        puntuacion_usuario = 0
        puntuacion_boot = 0
        partidas_jugadas += 1

    #OPC de creacion de personaje 
    elif opc == "2":
        usuario = input("Introduce tu nombre de usuario: ")
        print("Bienvenido,", usuario, "! Vamos a jugar una partida ^^")

    #OPC de Ranking
    elif opc == "3":
        print("\n--- Ranking ---")
        
        #Compro que tenemos datos en el Ranking
        if not ranking:
            print("Aún no se han jugado partidas.")
            print()
            
        #Si tenemos datos en el ranking
        else:
             #Entramos en el ranking
            for i in range(len(ranking)): 
                info_cara = ranking[i] 
                
                #Separacion de la lista 
                if info_cara == ":":
                    fin_nombre = i
                    inicio_puntuacion = i + 1
                    
                elif info_cara == ";":
                    fin_puntuacion = i
                    nombre = ranking[inicio_nombre:fin_nombre]
                    puntuacion = ranking[inicio_puntuacion:fin_puntuacion]
                    print("Nombre: {}, Puntuación: {}".format(nombre, puntuacion))
                    inicio_nombre = i + 1
            
                #Presentacion del Ranking 
                nombre = ranking[inicio_nombre:fin_nombre]
                puntuacion = ranking[inicio_puntuacion:fin_puntuacion]
                print("Nombre: {}, Puntuación: {}".format(nombre, puntuacion))
                print()

    #OPC de salir 
    elif opc == "4":
        print("¡Gracias por jugar!")
        print('Nos vemos a la proxima ')
        break

    else:
        print("Opción no válida. Inténtalo de nuevo. Tiene que ser un numero entre el 1 y el 4")