import random
'''
#eje 1
def cuadrado (c , d):
    resultado = c **d
    return resultado

c = int(input('Dime el valor que quieres dividir al n²  -> '))
d = 2

print(cuadrado(c,d))



#eje 2
def imprimiraste (a , b):
    imprimir = a * b 
    return imprimir

a = '*'
b = int(input('Dime el valor de * que quieres imprimir -> '))

print(imprimiraste(a,b))


#eje 3
e = int(input('Dime el numero a dividir -> '))
i = 1
def divisors (e , i):
    while i <= e :
        if e%i == 0:
            print(i) 
        i = i+1
divisors(e,i)


#eje4

lista1 = [1,2,3,4]
lista2= [4,5,6,7]

def iguales (lista1 , lista2):
    print(lista1)
    print(lista2)

    for i in lista1:
        for j in lista2:
            if(i==j):
                print('True')
                break
        else:
            print('False')

iguales(lista1, lista2)


#eje5
lista3 = []


for i in range(3):
    lista3.append(random.randint(1, 15))
  

print(lista3)
input()


def procediment(lista3):
    for x in lista3:
        print('*'*x,end='\n')

procediment(lista3)


#eje6
numx = int(input('Dime un numero y yo imprimo las x correspondientes -> '))

def generar_n_caracters(numx):
    print('X'* numx)


generar_n_caracters(numx)


#eje7
lista_1 = []

for i in range(3):
    lista_1.append(random.randint(1, 15))

print(lista_1)

print('*'*35)

def suma(lista_1):

    resultado= 0 
    for x in range(len(lista_1)): #revisar 
        resultado += lista_1[x]
        print(resultado)

suma(lista_1)

print('*'*35)


def multi(lista_1):
    resultado1= 0 
    for x in range(len(lista_1)):
        resultado1 += lista_1[x]
        print(resultado1)

multi(lista_1)
'''