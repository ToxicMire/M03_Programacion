num= int(input('Dime un numero y te digo si es primo > '))
primo = True

for i in range(2,num):
    if num%i == 0:
        primo= False
        break
if primo:
    print('Numero primo')
else: 
    print('Numero No primo')

