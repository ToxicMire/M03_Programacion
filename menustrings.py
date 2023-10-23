menu00 = 'Menu00'
Menu00 = '1.- Menu01 \n2.- Menu02 \n3.- Exit'
Primertitu= menu00.center(80,'-')  

menu01 = 'Menu01'
Menu01 = '1.- Menu011 \n2.- Menu012 \n3.- Exit'
Primertitu1= menu01.center(80,'-')  

menu011 = 'Menu011'
Menu011 = '1.- Menu0111 \n2.- Menu0112 \n3.- Exit '
Primertitu2= menu011.center(80,'-') 

menu012 = 'Menu012'
Menu012 = '1.- Menu0121 \n2.- Menu0122 \n3.- Exit '
Primertitu3= menu012.center(80,'-') 

menu02 = 'Menu02'
Menu02 = '1.- Menu021 \n2.- Menu022 \n3.- Exit '
Primertitu4= menu02.center(80,'-') 

menu021 = 'Menu021'
Menu021 = '1.- Menu0211 \n2.- Menu0212 \n3.- Exit '
Primertitu5= menu021.center(80,'-') 

menu022 = 'Menu022'
Menu022 = '1.- Menu0221 \n2.- Menu0222 \n3.- Exit '
Primertitu6= menu022.center(80,'-') 


#Menu00
flg_00 = True
#Menu01
flg_01 = False
#Menu02
flg_02 = False
#Menu012
flg_012 = False
#Menu011
flg_011 = False
#Menu21
flg_021 = False
#Menu22
flg_022 = False



while True:

    while flg_00:
        print(Primertitu)
        print(Menu00)
        opc= int(input('>'))
        if opc <1 or opc>3:
            print('Opcion incorrecta')
        
        if opc == 1:
            flg_00 = False
            flg_01 = True

        if opc == 2:
            flg_00 = False
            flg_02 = True

        if opc == 3:
            flg_00 = False
            
    while flg_01:
        print(Primertitu1)
        print(Menu01)
        opc= int(input('>'))
        if opc <1 or opc>3:
            print('Opcion incorrecta')

        if opc == 1:
            flg_01 = False
            flg_011 = True
            
        
        if opc == 2:
            flg_01 = False
            flg_012 = True
            print(Primertitu3)
            print(Menu012)

        if opc == 3:
            flg_01 = False
            flg_00 = True
            
    while flg_02:

        print(Primertitu4)
        print(Menu02)
        opc= int(input('>'))
        if opc <1 or opc>3:
            print('Opcion incorrecta')

        if opc == 1:
            flg_02 = False
            flg_021 = True
            print(Primertitu5)
            print(Menu021)
        
        if opc == 2:
            flg_02 = False
            flg_022 = True
            print(Primertitu6)
            print(Menu022)

        if opc == 3:
            flg_02 = False
            flg_00 = True
    
    while flg_011:
            print(Primertitu2)
            print(Menu011)
            opc= int(input('>'))
            if opc <1 or opc>3:
                print('Opcion incorrecta')
            
            if opc == 1:
                print('Has elegido el Menu0111')
            if opc == 2:
                print('Has elegido el Menu0112')
            if opc == 3:
                flg_01 = True
                flg_011 = False
    
    while flg_012:
            print(Primertitu3)
            print(Menu012)
            opc= int(input('>'))
            if opc <1 or opc>3:
                print('Opcion incorrecta')
            
            if opc == 1:
                print('Has elegido el Menu0121')
            if opc == 2:
                print('Has elegido el Menu0122')
            if opc == 3:
                flg_01 = True
                flg_012 = False
    
    while flg_021:
            print(Primertitu5)
            print(Menu021)
            opc= int(input('>'))
            if opc <1 or opc>3:
                print('Opcion incorrecta')
            
            if opc == 1:
                print('Has elegido el Menu0211')
            if opc == 2:
                print('Has elegido el Menu0212')
            if opc == 3:
                flg_02 = True
                flg_021 = False

    while flg_022:
            print(Primertitu6)
            print(Menu022)
            opc= int(input('>'))
            if opc <1 or opc>3:
                print('Opcion incorrecta')
            
            if opc == 1:
                print('Has elegido el Menu0221')
            if opc == 2:
                print('Has elegido el Menu0222')
            if opc == 3:
                flg_02 = True
                flg_022 = False

    if (not flg_00) and (not flg_01) and (not flg_011) and (not flg_012) and (not flg_02) and (not flg_021) and (not flg_022):
        break
