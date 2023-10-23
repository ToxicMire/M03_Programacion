import random

for i in range(20):
    print('{} -'.format(random.randrange(5)), end=' ') #no sale el ultimo numero 


print()
print('_'*50)
print()
for i in range(20):
    print('{} -'.format(random.randrange(5,10)), end=' ') #no sale el ultimo numero 


print()
print('_'*50)
print()
for i in range(20):
    print('{} -'.format(random.randrange(5,10,2)), end=' ') #no sale el ultimo numero 



print()
print()
print()
print('_'*50)
print()
for i in range(20):
    print('{} -'.format(random.randint(5,10)), end=' ') #salen los numeros 


print()
print()
print()
print('_'*50)
print()
for i in range(5):
    print('{} -'.format(random.random()), end=' ') #salen los numeros decimales entre 1 y 0 
print()
print('_'*50)
print()
for i in range(5):
    print('{} -'.format(100+random.random()*200), end=' ')#salen los numeros decimales entre 100 y 200 


print()
print()
print()
print('_'*50)
print()
for i in range(5):
    print('{} -'.format(random.uniform(100,200)), end=' ')#salen los numeros entre 100 y 200 

print()
print()
print()
print('_'*50)
print()
lista = ['b','d','r','t','q','x']
for i in range(20):
    print('{} -'.format(random.choice(lista)), end=' ')#sale la informacion de la lista 


print()
print()
print()
print('_'*50)
print()
lista = ['b','d','r','t','q','x']
for i in range(2):
    random.shuffle(lista)
    print('{} -'.format(lista))#sale la informacion de la lista desordenada


print()
print()
print()
print('_'*50)
print()
lista = ['b','d','r','t','q','x']
for i in range(2):
    muestra= random.sample(lista,3)
    print('{} -'.format(muestra))#sale la informacion de la lista 

