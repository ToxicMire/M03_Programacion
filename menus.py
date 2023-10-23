menu00 = "\n \n "+"-"*10+ "Menu00"+ "-"*10+ "\n 1.- Menu01 \n 2.- Menu02 \n 3.- Exit\n"
menu01 = "\n \n "+"-"*10+ "Menu01"+ "-"*10+ "\n 1.- Menu11 \n 2.- Menu12 \n 3.- Back\n"
menu02 = "\n \n "+"-"*10+ "Menu02"+ "-"*10+ "\n 1.- Menu21 \n 2.- Menu22 \n 3.- Back\n"
# print(menu00)
# print(menu01)
# print(menu02)

#semaforos
flg_00 = True
flg_01 = False
flg_02 = False
flg_12 = False
flg_11 = False
flg_21 = False
flg_22 = False

while True:
    print("while principal")
    while flg_00:
        print(menu00)
        opc = input("Opcion -> ")
        if not opc.isdigit():
            print("Opcion Incorrecta")
        elif int(opc) <1 or int(opc) >3:
            print("Opcion Incorrecta")
        opc = int(opc)

        if opc ==1:
            flg_00 = False
            flg_01 = True

        if opc ==2:
            flg_00 = False
            flg_02 = True

        if opc ==3:
            flg_00 = False


    while flg_01:
        print(menu01)
        opc = input("Opcion -> ")
        if not opc.isdigit():
            print("Opcion Incorrecta")
        elif int(opc) <1 or int(opc) >3:
            print("Opcion Incorrecta")
        opc = int(opc)

        if opc ==1:
            flg_01 = False
            flg_011 = True

        if opc ==2:
            flg_01 = False
            flg_012 = True

        if opc ==3:
            flg_00 = True
            flg_01 = False



    while flg_02:
        print(menu02)
        opc = input("Opcion -> ")
        if not opc.isdigit():
            print("Opcion Incorrecta")
        elif int(opc) <1 or int(opc) >3:
            print("Opcion Incorrecta")
        opc = int(opc)

        if opc ==1:
            flg_02 = False
            flg_021 = True

        if opc ==2:
            flg_02 = False
            flg_021 = True

        if opc ==3:
            flg_00 = True
            flg_02 = False

    if not flg_00 and not flg_01 and flg_02\
    and  not flg_012 and  not flg_011 and  not flg_021 \
    and not flg_02:
    break