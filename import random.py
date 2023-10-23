import random
# alto = int(input("Dame el alto del rectangulo -> "))
# ancho = int(input("Dame la ancho del rectangulo -> "))
#
# for i in range(alto):
#     for j in range(ancho):
#         if (i ==0 or j==0 or i== alto-1 or j== ancho-1):
#             print("*",end="")
#         else :
#             print(" ", end="")
#     print()
#
# alto1 = int(input("Dame el alto del rectangulo -> "))
# ancho1 = int(input("Dame la ancho del rectangulo -> "))
#
# for i in range(alto1):
#
#     for j in range(ancho1):
#         if (i ==0 or j==0 or i== alto1-1 or j== ancho1-1):
#             print("*",end="")
#         else :
#             print(" ", end="")
#     print("i = ", i)
#     print("j = ", j)
#     print()
#
# print("Dime tu fehca de nacimiento en este orden dia mes año para saber tu numero de la suerte")
# dia = int(input("Primer dijito del dia -> "))
# dia1 = int(input("Segundo dijito del dia -> "))
# mes = int(input("Primer dijito del mes  -> "))
# mes1 = int(input("Segundo dijito del mes  -> "))
# año = int(input("Primer dijito del año -> "))
# año1 = int(input("Segundo dijito del año -> "))
# año2 = int(input("Tercer dijito del año -> "))
# año3 = int(input("Cuarto dijito del año -> "))
# result = 0
# while result <10:
#     result = dia + dia1 + mes + mes1 + año + año1 + año2 + año3
# print(result)

#
# print("Eje 3 \n ")
# numbacterias = 1
# veces = 0
# timpoMin = 0
# while numbacterias < 10000000:
#     timpoMin = timpoMin +3
#     numbacterias = numbacterias * 2
#     print("El numero de minutos es ", timpoMin  )


# valores = 0
# print("Cuantos valores vas a intoducir ? \n")
# valores = int(input("Dime el numero de valores que vas a introducir ->  "))
# while valores <0:
#     print("Dame un valor positivo")
#     valores = int(input("Dime el numero de valores que vas a introducir "))
#
# num1 = int(input("Escibe un numero ->"))
# num2 =  int(input("Escribe un numero diferente a " , num1 ":", num2 <> num1 ))
# while num2 < > num1
#     print("Otro numero porfavor")
#     num2 = int(input("Escribe un numero diferente a ", num1 ":", num2 <> num1 ))
#
# dado1 = 0
# dado2 = 0
# puntuacion1 = 0
# puntuacion2 = 0
#
# while   (puntuacion1 < 10 and puntuacion2 < 10):
#     print("Tu tirada")
#     dado1 = random.randrange(1,7)
#     dado2 = random.randrange(1, 7)
#     tirada1 = dado1 +   dado2
#     print("Tirada" , tirada1)
#     print("Tirada de la maquina")
#     dado1 = random.randrange(1, 7)
#     dado2 = random.randrange(1, 7)
#     tirada2= dado1 + dado2
#     print("Tirada", tirada2)
#     if tirada1 > tirada2:
#         puntuacion1 = +1
#     elif tirada2 > tirada1:
#         puntuacion2 = +1
#     print("puntuacion actual")
#     print( " Tu puntuacion" , tirada1)
#     print(" Tu puntuacion", tirada2)
# if puntuacion1 > puntuacion2:
#     print("Eres el ganador")
# else:
#     print("Ganador la maquina")


for i in range(20):
     print(random.randint(10,20)) #salen numeros aleatorios del 10 al 20 con ellos incluidos
#
lista = ["A", "B","C","D"]
# for 1 in range(20):
#     print(random.choice(lista)) #salen numeros aleatorios de la lista
#

print(lista)
random.shuffle(lista) #se desordena la lista aleatoriamente
print(lista)