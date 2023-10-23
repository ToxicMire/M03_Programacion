print('Hola mundo')

#print('\n \n \n')

'''
    \t es una tabulacion  \' imprime las comillas 
'''

print(' Hola mundo 1\n Hola mundo 2\n Hola mundo 3')

print('\n \n \n')
print('Variables')
#True = 1 bolean
var = True 
#string
var2 = 'True'
#numero
var3 = 5 
# False = 0
var4 = False

print(var + var)
print(var2 + var2) #concatena los strings 
print(var3 + var3)

print('\n')

print(type(var))
print(type(var2))
print(type(var3))

print('\n')

print(var * var)
print(var*var3)
print(var2*var3)
print(var*var2)
print(var4*var2) #como es un 0 no imprime nada
#print(var2*var2) no se puede multiplicar los strings con strings 
print('\n \n \n')

print('Operaciones enteras')

'''
+
-
*
/
** elevado a 
%  da la resta de la division 
// de la division se queda con un numero entero 
'''

num = 28
num1 = 5

print(num + num1)
print(num - num1)
print(num / num1)
print(num * num1)
print(num // num1)
print(num % num1)


print('\n')

print('Operaciones Logicas')

'''
and = evaluar mas de dos condiciones 
or =  evaluar una o otra condicion
not = niega la condicion

'''
print('*'*10)
print('\n')
print('AND')
print('\n')

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print('*'*10)
print('\n')
print('OR')
print('\n')

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('*'*10)
print('\n')
print('NOT')
print('\n')

print(not True)
print( not False)

print('*'*10)
print('\n')
print('NOT AND')
print('\n')
print('*'*10)
# print(not(True and True)) composicion 

condicion1 = True
condicion2 = False

#negamos toda la expresion 

print(not (condicion1 and condicion1 ))
print(not (condicion1 and condicion2 ))
print(not (condicion2 and condicion1 ))
print(not (condicion2 and condicion2 ))

#negamos la primera expresion 

print('*'*10)

print(not condicion1 and condicion1 )
print(not condicion1 and condicion2 )
print(not condicion2 and condicion1 )
print(not condicion2 and condicion2 )

#negamos las dos expresiones 

print('*'*10)

print(not condicion1 and not condicion1 )
print(not condicion1 and not condicion2 )
print(not condicion2 and not condicion1 )
print(not condicion2 and not condicion2 )


print('\n \n \n')
print('Operadores logicos 2')

print('\n')
'''
== 
!=
<
>
<=
>=

'''
num2 = 6
num3 = 5

print( num2 == num2)
print( num2 != num3)
print( num3 < num2)
print( num3 > num3)
print( num3 >= num3)
print( num3 >= num3)

print('*'*10)

print(num2 == 5 and num3 == 9)
print(not(num2 == 5 or num3 == 9 ))

print('*'*10)

print(num2 != 5 and num3 != 9)
print(not(num2 != 5 or num3 != 9 ))

#ejemplos

print('\n \n \n')
print('Ejemplos')
print('\n')

print(7>6 and 8<3 or 2<5)

#primer operador logico que el programa hace es el and 

print(5 + 6 * 10 - 6 * 3) #sin parantesis

#primero que se ejecuta es la multiplicacion despues division suma  y resta (* / + -)

print((((5 + 6) * 10 )- 6) * 3) # con parentesis 

# calcular la suma de 5+7 el resultado multiplicado por 10 a todo lo anterior lo restamos multiplicamos por 5 y luego restamos a este resultado porcial 10 

print(((5+7)* 10 ) - ((10 * 5)-10 )) 

print(((5+7)* 10 ) - ((10 * 5)-10 ) + ((8+5)*7)  ) 


print('\n \n \n')
print('Operadores Asignados ')

print('\n')
'''
operadores asignados
'''

nume1 = ((5+7)*10)
nume2 = ((10*5)-10)
nume3 = ((8+5)*7)
nume4 = (6+(5*4))
nume5 = nume1 - nume2

print(nume1 + nume2 + nume3 - nume4)

print(nume5 + nume3 - nume4)

print('\n')

ue1 = 0
ue1 +=1
print(ue1)
ue1 = ue1 + 1
print(ue1)

print('*'*10)

ue12 = 1
ue12 *=2 
print(ue12)
ue12 = ue12 * 2
print(ue12)

print('*'*10)


ue13 = 1000
ue13 /=10
print(ue13)
ue13 = ue13 / 10
print(ue13)

print('*'*10)

ue14 = 1000
ue14 -=10
print(ue14)
ue14 = ue14 - 10
print(ue14)

print('*'*10)


ue2 = 1000
ue21= ue2
ue21 = ue21  + 5000
print(ue2)
print(ue21)

