num = 10 

'''
print(num > 0)
input()
while num > 0:
    print(num > 0)
    print('num =', num)
    num -= 2
    input()'''
    
cont = 1
'''
while cont <= 10:
    print('contador = ', cont)
    cont += 1 
    if cont== 5:
        break

while True:
    print('contador = ', cont)
    cont += 1 
    if cont== 5:
        break
'''

for i in range(20):
    print('i =',i)
print('-'*50)
print(range(5,10))
print('-'*50)

for i in range(5,10): #empieza en el numero y termina en uno menos del final
    print('i =',i)

print('-'*50)
for i in ['Pedro','Pablo','Justino']:
    print('i = ' , i )

print('-'*50)

for i in range(5,10): #empieza en el numero y termina en uno menos del final
    print('i =',i)
    i = i-1
    print('i2 =',i) # se itera sobre lo de arriba pero este no afectaprint('-'*50)


print('-'*50)

for i in range(5,10,2): #empieza en el numero y termina en uno menos del final y suma de 2 en 2
    print('i =',i)

print('-'*50)

for i in range(10): #empieza en el numero y termina en uno menos del final y suma de 2 en 2
    for j in range(10):
        print('i = ',i )
        print('j = ',j )
        print('*'*10)

print('-'*50)
for i in range(10): #empieza en el numero y termina en uno menos del final y suma de 2 en 2
    for j in range(10):
        print('i = ',i )
        print('j = ',j )
        if j == 5: 
            break