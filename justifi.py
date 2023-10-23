'''
print("Titulo".center(60,"="))
print("Id".ljust(10),"Nombre".ljust(15),"Apellido".ljust(35))
print("=",60)

id = "1"
nombre = "Pablo"
apellido = "Adolfo"
print("{}{}{}".format(str(id).ljust(10),str(nombre).rjust(15),str(apellido).rjust(35)))

id = "2"
nombre = "Juan"
apellido = "No se"
print("{}{}{}".format(str(id).ljust(10),str(nombre).rjust(15),str(apellido).rjust(35)))

id = "3"
nombre = "Tony"
apellido = "Gomez"
print("{}{}{}".format(str(id).ljust(10),str(nombre).rjust(15),str(apellido).rjust(35)))


id = "PR1"
nombre = "Pau"
apellidos = "Rius Noriega"
print("Titulo".center(60,"=") + "\n" + "ID".ljust(10) + "Nombre".ljust(15) + "Apellidos".ljust(35) + "\n" + ""60)
print(("{}{}{}").format(id.ljust(10),nombre.ljust(15),apellidos))
id = "PM1"
nombre ="Paulo"
apellidos = "Maestre Fernandez"
print(("{}{}{}").format(id.ljust(10),nombre.ljust(15),apellidos))
id = "PM2"
nombre = "Paula"
apellidos = "Naharro Ureña"
print(("{}{}{}").format(id.ljust(10),nombre.ljust(15),apellidos))



print('\n \n')

print("Titulo".center(65,"="))
print("Id".ljust(15)+" "*5+"Nombre".ljust(10)+" "*5+"Apellido".ljust(30))
print(65*"=")
texto = '{}'+ ' '*5 + '{}'+ ' '*5 + '{}' 

id = 1
nombre = "Pablo"
apellido = "Adolfo"
print(texto.format(str(id).rjust(15),str(nombre).ljust(10),str(apellido).ljust(30)))

id = 2
nombre = "Juan"
apellido = "No se"
print(texto.format(str(id).rjust(15),str(nombre).ljust(10),str(apellido).ljust(30)))

id = 3
nombre = "Tony"
apellido = "Gomez"
print(texto.format(str(id).rjust(15),str(nombre).ljust(10),str(apellido).ljust(30)))





print('Nuevo producto')
id = input('ID > ')
stock = int(input('Dime el numero del stock > '))
Descri = input('Descripcion del producto \n>')

print('\n')

print('Nuevo producto')
id2 = input('ID > ')
stock2 = int(input('Dime el numero del stock > '))
Descri2 = input('Descripcion del producto \n>')

print('\n')

print('Nuevo producto')
id3 = input('ID > ')
stock3 = int(input('Dime el numero del stock > '))
Descri3 = input('Descripcion del producto \n>')

print('\n')

print("Almacen".center(65,"="))
print("Id".ljust(15)+" "*5+"Stock".ljust(10)+" "*5+"Desc.Pedido".ljust(50))
print(65*"=")
texto = '{}'+ ' '*5 + '{}'+ ' '*5 + '{}' 
print(texto.format(str(id).ljust(15),str(stock).rjust(10),str(Descri).ljust(50)))
print(texto.format(str(id2).ljust(15),str(stock2).rjust(10),str(Descri2).ljust(50)))
print(texto.format(str(id3).ljust(15),str(stock3).rjust(10),str(Descri3).ljust(50)))
'''





print('Nuevo producto')
id = input('ID > ')
stock = int(input('Dime el numero del stock > '))
Descri = input('Descripcion del producto \n>')

prductos= ''

texto = '{}'+ ' '*5 + '{}'+ ' '*5 + '{}' 
prductos += texto.format(str(id).ljust(15),str(stock).rjust(10),str(Descri).ljust(50))

print('\n')


cabezera = "Almacen".center(65,"=")+ '\n'  +65*"="  + '\n' + "Id".ljust(15)+" "*5+"Stock".ljust(10)+" "*5+"Desc.Pedido".ljust(50)  +'\n' +65*"=" +'\n'

print(cabezera + prductos)

print('Nuevo producto')
id = input('ID > ')
stock = int(input('Dime el numero del stock > '))
Descri = input('Descripcion del producto \n>')

prductos += texto.format(str(id).ljust(15),str(stock).rjust(10),str(Descri).ljust(50))

print(cabezera + prductos)
