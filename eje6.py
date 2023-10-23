print('='* 30)
print('= 1.- Euros a Dolares')
print('= 2.- Euros a Dolares')
print('= 3.- Dolares a Euros')
print('= 4.- Dolares a Yenes')
print('= 5.- Yenes a Euros')
print('= 6.- Yenes a Dolares')
print('='* 30)
print('= Tria una opc de conversion =')
print('='* 30)

opc = int(input('Dime que opc quieres usar \n> '))
euro_yen = 115.998
euro_dolar = 1.11894
Euro = 0
Dolar = 0
Yen  = 0
cantida = 0 
paso = 0

if opc == 1:
    cantida = int(input('Dime la cantidad de dinero > '))
    paso = cantida * euro_dolar
    print('Paso Euros a dolares = ',paso)
    
elif opc == 2:
    print('opc2')
    cantida = int(input('Dime la cantidad de dinero > '))
    paso = cantida * euro_yen
    print('Paso Euros a Yenes = ',paso)
    
elif opc == 3:
    print('opc3')
    cantida = int(input('Dime la cantidad de dinero > '))
    paso = cantida / euro_dolar
    print('Paso Dolares a Euros = ',paso)
    
elif opc == 4:
    print('opc4')
    cantida = int(input('Dime la cantidad de dinero > '))
    paso = cantida / euro_dolar
    paso1 = paso * euro_yen
    print('Paso Dolares a Yenes = ',paso1)

elif opc == 5:
    print('opc5')
    cantida = int(input('Dime la cantidad de dinero > '))
    paso = cantida / euro_yen
    print('Paso Yenes a Euros = ',paso)
    
elif opc == 6:
    print('opc6')
    cantida = int(input('Dime la cantidad de dinero > '))
    paso = cantida / euro_yen
    paso1 = paso * euro_dolar
    print('Paso Yenes a Dolares = ',paso1)
else:
    print('Eso no es una opcion correcta')