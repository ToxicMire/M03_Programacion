print( "|" , "*"*23 , "|" , "*"*11, "|"  )
print("|" , "NUM. DE KILOS COMPRADOS".ljust(23) ,"|".ljust(1),  "% DESCOMPTE".ljust(10) , "|")
print( "|" , "*"*23 , "|" , "*"*11, "|"  )
print("|" , " -> 0 - 2".ljust(23), "|", "0%".rjust(6), "|".rjust(6))
print( "|" , "_"*23 , "|" , "_"*11, "|"  )
print("|" , " -> 2.01 - 5".ljust(23), "|", "10%".rjust(6), "|".rjust(6))
print( "|" , "_"*23 , "|" , "_"*11, "|"  )
print("|" , " -> 5.01 - 10".ljust(23), "|", "15%".rjust(6), "|".rjust(6))
print( "|" , "_"*23 , "|" , "_"*11, "|"  )
print("|" , " -> 10.01 - 20".ljust(23), "|", "20%".rjust(6), "|".rjust(6))
print("\n")
print("Final del ejer 6 \n")


print("introduce un numero para saber si es par o impar")
resultado = int(input("Introduce el numero: \n \n -> "))
if resultado >=0 and  resultado <=5:
    print("El numero esta entre 0 y 5")
elif resultado >5 and resultado <=10:
   print("El numero esta entre 6 y 10 ")
elif resultado >10 and resultado <=15:
   print("El numero esta entre 10 y 15 ")
else:
    print("El nnumero es mayor que quinze ")




num = True if resultado%2==0 else False
print("mi variable=",num)

resul = int(input("Introduce el numero: \n \n -> "))
if resul < 0:
    print("el valor absoluto es:",resul)





edad = int(input("Introzuce tu edad"))
ingresos = int(input("Introduce tus ingresos familiares"))
numherma = int(input("Cuantos hermanos tienes ?"))


if ingresos > (numherma * 5700)+500:
    if numherma > 4:
        beca = 150
    else:
        beca = 0
else:
    beca = (400* (numherma * 5700) + 500 - ingresos) / ((numherma * 5700) +500)

if edad < 18:
    beca = beca + beca*10/100
print("El importe es", beca)



numero = 10
while numero > 0:
    print("numero", num)
    numero = numero - 1