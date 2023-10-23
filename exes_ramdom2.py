#ejer 2 
import random

numeroia =  random.randint(1,100)
print('Adivina que numero! Es un numero entre 1 y 100 pero tienes 5 intentos')
numeropersona = int(input('Dime el numero > ' ))
intentos = 5

while True:    
    if numeropersona == numeroia:
        print('Has gadano el numero es ese',numeroia)
        break
    else:
        print('Ese no es el numero')
        numeropersona = int(input('Dime el numero > ' ))
        intentos-=1
        print('Te quedan',intentos)
        if intentos == 0:
            print('Has perdido no tienes vidas')
            break
            
