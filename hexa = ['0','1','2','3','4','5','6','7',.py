hexa = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
menu00 = "Tipo de conversion:\n1) Hexadecimal Binaria\n2) Binaria Hexadecimal\n3) Salir"
menu01 = "#" * 5 + " Hexadecimal a Binario " + "#" * 5
menu02 = "#" * 5 + " Binario a Hexadecimal " + "#" * 5
cadena = ""
listaMac = []
while True:
    print(menu00)
    opcion = input("Opcion >> ")
    if not opcion.isdigit():
        print("No has introducido un numero")
    elif int(opcion) < 1 or int(opcion) > 3:
        print("El numero no es correcto")
    else:
        if int(opcion) == 1:
            while True:
                macaux = ""
                cadena = ""
                print(menu01)
                mac = input("Dime tu direccion MAC: ")
                for i in mac:
                    # DC:DC:FD -> [DC,DC,FD]
                    if not i == ":":
                        macaux = macaux + i
                    if len(macaux) == 2:
                        listaMac.append(macaux)
                        macaux = ""
                if len(listaMac) != 6:
                    print("Mac no valida")
                else:
                    break
            for dupla in listaMac:
                result = 0
                for i in range(len(dupla)): # i = 0, primer valor; i = 1, segundo valor (Dupla)
                    result = result + hexa.index(dupla[i]) * 16 ** (len(dupla) - 1 - i) # A -> index = 10, 10 * 16 elevado a len(dupla) -1-i
                binOcteto = ""
                for j in range(8): # 8 porque cada octeto tiene 8
                    binOcteto = str(result % 2) + binOcteto # Coger resto -> 0 or 1
                    result = result // 2 # Division entera para seguir
                cadena = cadena + binOcteto + ":"
            cadena = cadena[:-1] # DC:DC:FD:DC:DC:FD: -> DC:DC:FD:DC:DC:FD
            print("Numero en binario {}".format(cadena))

        if int(opcion) == 2:
            print(menu02)
            while True:
                numBin = input("Numero en binario: ")
                if len(numBin) != 53:
                    print("Numero no valido")
                else:
                    break
            binariNum = numBin.split(":")
            for item in binariNum:
                result = 0
                for i in range(len(item)):
                    result += int(item[i]) * 2 ** int(len(item) - 1 - i) # 1 * 10 elevado a index -> 0,1,2,4,8,16,32
                    cadenaaux = ''
                for j in range(2):
                    cadenaaux = str(hexa[result % 16]) + cadenaaux
                    result = result // 16
                cadena = cadena + cadenaaux
                cadena = cadena + ':'
            cadena = cadena[:-1]
            print("La direccion mac en hexadecimal es {}".format(cadena))
        if int(opcion) == 3:
            print("Saliendo del programa ^.^ ")
            break
