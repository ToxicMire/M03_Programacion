print('Vamos a hacer la lista de clientes ')
cabezera = 'Clientes'.center(41,'*') + '\n' + 'Nombre'.ljust(10) + 'Edad'.rjust(5)+'  '+ 'DNI'.ljust(10)+ 'Telefono'.rjust(14)+'\n' +'*'*41 +'\n'
print(cabezera)

# 1r 
INFO=''
Nombre = input('Nombre > ')
Edad = input('Edad > ')
DNI = input('DNI > ')
Telefono = input('Telefono > ')

INFO = INFO + Nombre.ljust(10) + Edad.rjust(5)+'  '+ DNI.ljust(10)+Telefono.rjust(13)+ '\n'
print(cabezera+INFO)

# 2r 
Nombre = input('Nombre > ')
Edad = input('Edad > ')
DNI = input('DNI > ')
Telefono = input('Telefono > ')

INFO = INFO + Nombre.ljust(10) + Edad.rjust(5)+'  '+ DNI.ljust(10)+Telefono.rjust(13)+ '\n'
print(cabezera+INFO)

#3r
Nombre = input('Nombre > ')
Edad = input('Edad > ')
DNI = input('DNI > ')
Telefono = input('Telefono > ')

INFO = INFO + Nombre.ljust(10) + Edad.rjust(5)+'  '+ DNI.ljust(10)+Telefono.rjust(13)+ '\n'
print(cabezera+INFO)