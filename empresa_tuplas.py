#Aplicacion de empresa
mario =("mario gonzalez perez", "555555555E", "calle canada 12 3º 4º", "+0034566232216")
pedro =("pedro gutierresz lopez", "666666666A", "calle balmes 22 1º 3º", "+00341212314")
anabel =("anabel lorca suarez", "251244515Y", "calle vasubio 7 8º 1º", "+0034562123123")

#lista de usuarios
usuarios = [mario,pedro,anabel]
#usuarios de la empresa


#para calcular las letras del dni

letrasDNI = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

while True:
    print("************Gestoria Gutierrez*************")
    print("1) Nuevo usuario \n 2) Lista de usuarios \n 3)Buscar \n 4)Salir")
    opc = input("Opcion: \n")
    if not opc.isdigit(): #se comprueba si es un digito
        print("opcion incorrecta")
    elif int(opc)<1 or int(opc) > 4: #se comprueba si es un numero de 1 a 4
        print("Opcion incorrecta")
    else:
        opc = int(opc)
        if opc == 1:
            # encuesta del nuevo osuario
                print("nuevo usuario: \n")

                nombre = input("nombre del nuevo usuario: \n")
                direccion = input("direccion del nuevo usuario: \n")
                # bucle del dni
                while True:
                    dni = input("Dni del nuevo usuario: \n")
                    if len(dni) != 9 or not dni[0:8].isdigit():  # 9 caracters y 8 son dijitos
                        print("Formato del DNI incorrecto")
                    elif letrasDNI[int(dni[0:8]) % 23].lower() != dni[
                        8].lower():  # pasamos el numero 23 en digito para poder calcular, comprobamos si esta en la posicion 8 y lo ponemos en minus
                        print("la letra del dni es incorecta")
                    else:
                        print("bien has introduciodo un dni correcto")
                        break  # salimos del bucle del dni

                    # bucle telefono
                while True:
                    tfn = input("telefono del nuevo usuario: \n")
                    if len(tfn) != 14 or not tfn[1:].isdigit():  # se comprueba si es de 14 dijitos y que los 13 sean numeros
                        print("Formato del telefono incorrecto")
                    elif tfn[0] != "+":
                        print("Formato del telefono incorrecto")
                    else:
                        print("bien has introduciodo un telefono correcto")
                        break  # salimos del bucle del dni

                    # añadimos el nuevo usuario
                    nuevoUsu = (nombre, dni, direccion, tfn)
                    usuarios.append(nuevoUsu)

        if opc == 2:
            for u in usuarios: #listar los usuarios en 1 en 1
                str = "Nombre:".ljust(15)+u[0]+"\n"+"DNI:".ljust(15)+u[1]+"\n"+"Direccion:".ljust(15)+u[2]+"\n"+"Telefono:".ljust(15)+u[3]
                print(str)
                input()

        if opc == 3: #menu de busqueda
            while True:
                print("Menu de busqueda")
                print("1)Por nombre\n 2) Por Dni \n 3) Por telefono \n 4) Salir")
                opc = input("Opcion:\n")
                if not opc.isdigit():  # se comprueba si es un digito
                    print("opcion incorrecta")
                elif int(opc) < 1 or int(opc) > 4:  # se comprueba si es un numero de 1 a 4
                    print("Opcion incorrecta")
                else:
                    opc = int(opc)
                    if opc ==1 :
                        busqueda = input("Nombre a buscar:\n ")
                        str = "Nombre".ljust(25)+"DNI".ljust(15)+"Direccion".ljust(25)+"Telefono".ljust(15)+"\n"+"*"*70+"\n"

                        for u in usuarios:
                            if busqueda.lower() in u[0].lower():
                                str = 'Nombre'.ljust(25) + 'DNI'.ljust(15) + 'Direccion'.ljust(25) + 'Telefono'.ljust(
                                    15) + '\n' + '*' * 75 + '\n'


                        print(str)
                        input()

                    if opc== 2:
                        busqueda = input("DNI a buscar:\n ")
                        str = 'Nombre'.ljust(25) + 'DNI'.ljust(15) + 'Direccion'.ljust(25) + 'Telefono'.ljust(
                            15) + '\n' + '*' * 75 + '\n'
                        "\n"

                        for u in usuarios:
                            if busqueda.lower() in u[1].lower():
                                str = str + u[0].ljust(25) + u[1].ljust(15) + u[2].ljust(25) + u[3].ljust(15) + "\n"

                        print(str)
                        input()

                    if opc == 3:
                        busqueda = input("Telefono a buscar:\n ")
                        str = 'Nombre'.ljust(25) + 'DNI'.ljust(15) + 'Direccion'.ljust(25) + 'Telefono'.ljust(
                            15) + '\n' + '*' * 75 + '\n'

                        for u in usuarios:
                            if busqueda.lower() in u[3].lower():
                                str = str + u[0].ljust(25) + u[1].ljust(15) + u[2].ljust(25) + u[3].ljust(15) + "\n"

                        print(str)
                        input()
                    if opc == 4:
                        opc = 0
                        break


        if opc ==4:
            break