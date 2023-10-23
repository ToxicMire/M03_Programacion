#Comprobante de mails 
cadena = "nombre1;nombre2;nombre3.nombre4.nombre5.nombre6"



#################################################################

inicio=0
final=0
num=2
for i in range(cadena.count(';')):
    if i ==0:
        inicio=0
        final = cadena.index(";")
    else:
        inicio=final+1
        final=cadena.index(";",final+1)
    print("inicio={}, final = {}".format(inicio, final))
    print(cadena[inicio:final])



