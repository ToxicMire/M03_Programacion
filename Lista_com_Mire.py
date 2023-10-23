# 3 rep Producto > Cantidad> Precio  Enseña lista y añade producto 

#PRIMERO
Titulo = 'Lista de la  compra'.center(38,'*') + '\n' + 'Aritculos'.ljust(13) + 'Cantidad'.rjust(15)+ 'Precio'.rjust(10)+'\n' +'*'*38 + '\n'
Articulo = input('Articulo > ')
Cantidad = input('Cantidad > ')
Precio = input('Precio > ')

Info = Articulo.ljust(13) + Cantidad.rjust(14) + Precio.rjust(10)
print(Titulo,Info)

# SEGUNDO 
Articulo1 = input('Articulo > ')
Cantidad1 = input('Cantidad > ')
Precio1 = input('Precio > ')

Info1 = Articulo1.ljust(13) + Cantidad1.rjust(14) + Precio1.rjust(10)
print(Titulo,Info,Info1)

#TERCERO
Articulo2 = input('Articulo > ')
Cantidad2 = input('Cantidad > ')
Precio2 = input('Precio > ')

Info2 = Articulo2.ljust(13) + Cantidad2.rjust(14) + Precio2.rjust(10)
print(Titulo+'\n'+Info+'\n'+Info1+'\n'+Info2)


########################################################################################################################################################
