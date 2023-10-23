# Mirar compro hacer en bucle 
#infromacion e imports
from colorama import init, Fore, Back, Style #Cambia el color del texto 
Menu01 = ('1.- Crear usuario \n2.- Listar usuarios \n3.- Buscar \n4.- Salir')
Menu011 = ('Vamos a crear un usuario')
Menu03 = ('1.- Buscar por nombre \n2.- Buscar por DNI \n3.- Buscar por Telefono \n4.- Salir')
max_len = 100
Flag_menu00= True

usuarios = [ 
("Mario Gonzalez Perez", "55555555E" , "Calle Canada 27,1 2", "+0034654321234" ),
("Pedro Gutierrez Lopez", "44444444E" , "Calle Balmes 26,4 1",
"+0034654321234" ),("Anabel Lorca Suarez", "522222222" , "Calle Vesubio 27,7 1",
"+0034654321234")
]
Usuarios = ('')

dicc = []
letra_dni=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
cabezera =  '*'*max_len +'\nNombre'.ljust(27) + 'DNI'.ljust(26) + 'Direccion'.ljust(20) + 'Tfn\n'.rjust(10) + '*'*max_len

#Programa

#Menu inicial
while Flag_menu00 != False:
    print(Fore.BLUE)
    print('*'*max_len)
    print('Gestion de Usuarios'.center(max_len,'*'))
    print('*'*max_len)
    print()
    print(Menu01)
    print(Fore.GREEN)
    opc = input('Dime la opcion que quieres \n>')
    if not opc.isdigit():
        print("La opcion ha de ser numérica")
        input("Pulse una tecla para continuar...\n")
    else:
        opc = int(opc)
        if opc > 4 or opc < 0:
            print("La opción ha de estar entre 1 y 4")
            input("Pulse una tecla para continuar...\n")
            
            
    if opc == 1:
        print(Fore.BLUE)
        print('*'*max_len)
        print(Menu011.center(50))
        print('*'*max_len)
        print(Fore.GREEN)
        # Nombre , Dni compro , Telefono compro
        Nom_Usu = input('Nombre del nuevo usuario ? \n>')
        
        Dni_Usu = input('DNI del usuario \n>') 
        if len(Dni_Usu) != 9 or not Dni_Usu[0:8].isdigit():
            print(Fore.RED)
            print('Formato incorrecto')
            print(Fore.GREEN)
            Dni_Usu = input('DNI del usuario \n>')
        elif letra_dni[int(Dni_Usu[0:8])%23].lower() != Dni_Usu[8].lower():
            print(Fore.RED)
            print('La letra del dni es incorrecta ')
            print(Fore.GREEN)
            Dni_Usu = input('DNI del usuario \n>')
            
        else:
            print('DNI correcto ')
            
        Tel_Usu = input('Telefono del nuevo usuario \n>')
        # primero un + 14 numeros  del segundo digito al final sea digit 
        if len(Tel_Usu) != 14 or not Tel_Usu[1:].isdigit():
            print(Fore.RED)
            print('Formato incorrecto')
            print(Fore.GREEN)
            Tel_Usu = input('Telefono del nuevo usuario \n>')
        if Tel_Usu[0] != '+':
            print(Fore.RED)
            print('Formato incorrecto')
            print(Fore.GREEN)
            Tel_Usu = input('Telefono del nuevo usuario \n>')
        else:
            print('Telefono correcto ')
        
        Direcc_Usu = input('Direccion del nuevo usuario \n>')
        
        nuevo_usuario = (Nom_Usu,Dni_Usu,Direcc_Usu,Tel_Usu)
        usuarios.append(nuevo_usuario)
        print(cabezera)
        for i in range(len(usuarios)):
            for j in range(len(usuarios[i])):                   
                print(usuarios[i][j].ljust(25),end = ' ')
            print('')
        print(Fore.BLUE)
        print('Nuevo usuario creado correctamente')
        
        
        
    
        
    if opc == 2:
        print('Menu 2 Listar usu')
        print(cabezera)
        for i in range(len(usuarios)):
            for j in range(len(usuarios[i])):                   
                print(usuarios[i][j].ljust(25),end = ' ')
            print('')
    if opc == 3:
        print('Menu 3 Buscar usuarios')
        print(Menu03)    
        opc1 = int(input('Dime la opcion que quieres \n>'))
        
        #listar el usuario 
        # for i in range(len(usuarios)):
        #     for j in range(len(usuarios[i])):                   
        #         print(usuarios[i][j].ljust(25),end = ' ') 
            
        print('')
        
        
    if opc == 4:
        print('Saliendo del programa ^-^')
        print('Gracias por usar la app <3')
        Flag_menu00 = False
    
    
    
    
    
#Apuntes extra o informacion extra 
'''
    Comprobacion del dni 
    dni = input("DNI del nuevo usuario: \n")
                if len(dni) != 9 or not dni[0:8].isdigit():
                    print("Formato del DNI incorrecto")
                elif lista[int(dni[0:8])%23].lower() != dni[8].lower():
                    print("La letra del DNI es incorrecta")
                else:
                    print("Bien, has introducido un DNI correcto")
                   
       
'''