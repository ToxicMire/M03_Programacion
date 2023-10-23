salir = ''
print(salir!='S')
while salir!='S':
    print('Hola')
   
    salir = input('Quieres salir del programa ?? S\ N  \n> ')
    
    
i = 0 
 
while i <= 100:
    print('I =', i)
    i+= 1
    break # salir del bucle actual 

input()
for variable in (23,36,56):
    print(variable)
input()



for variable in [23,36,56]:
    print(variable)
input()

  
for variable in range(23): # el ultimo no sale (start,stop,salto)
    print(variable)
input()
    
for variable in range(10,20):
    print(variable)
    variable = 50
input()


for variable in range(10,20):
    print(variable)
    if variable == 14:
        break
input()


for variable in range(10,20): 
    if variable == 14:
        continue
    print(variable)
    
input()


for variable in range(10,15): 
    for j in range(10,15): 
        print('I = {} , J = {}'.format(variable,j))
        if j ==11: #aqui solo rompemos el bucle de j 
            break
        