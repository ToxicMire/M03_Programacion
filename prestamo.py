# if prestec  = costetaxa 80% 
# ingresos mes = prestect mes no mas del 50% 

prestec = int(input('Dime la cantidad del prestamo > '))
ingresos  =  int(input('Cual es la cantidad de ingresos mensuales tiene > '))
Costetaxa = int(input('Dime la tasa del prestamo > '))
Termino_de_pago  =  int(input('Dime el termino de pago en años > '))
#Calculos
importemensual = (prestec *2) / (Termino_de_pago * 12)
condicio1 = Costetaxa * 0.80
condicio2 = importemensual *0.50


if prestec > condicio1: 
    print('No puedes acceder al prestamo por que se pasa del 80%')

elif condicio2 >= importemensual:
    print('No cumples la segunda condicion')
else :
    print('Tienes acceso al prestamo, tu importe mensual sera de {}'.format(importemensual))

    