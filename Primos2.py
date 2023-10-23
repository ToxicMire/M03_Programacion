num= int(input('Dime un numero y te digo si es primo > '))

for i in range(2,num):
    primo: True
    for j in range(2,i):
                if j%i == 0:
                    primo = False
                    break
    if primo:
            print(i)

   