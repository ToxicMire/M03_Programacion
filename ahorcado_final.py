import time
import os
from tqdm import tqdm #pip install tqdm on cmd

os.system("cls") 
#Vars
vocal = ['A','E','I','O','U']
myword = " "
life = 8
tirada = 0
par = False
cont = False
fallos = 0
si = False
err = 0
usadas = ['']

muerto = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''','''
      +---++
      |  \|
          |
          |
          |
          |
    =========''', '''
      +---+
      |  \|
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |  \|
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |  \|
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |  \|
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |  \|
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |  \|
      X   |
     /|\  |
     / \  |
          |
    =========''']

for _ in tqdm(range(100),
        desc="Cargando scripts",
        ascii=False, ncols=75):
    time.sleep(0.02)
print('Se ha cargado correctamente los scripts')

os.system('cls')
time.sleep(0.5)
ready = False
while ready == False:
    print("**********************************************") 
    print("*                                            *")
    print("*                 Ahorcado                   *")
    print("*                                            *")
    print("*          1. Ganar siemp                    *")
    print("*          2. Perder nunca                   *")
    print("*                                            *")
    print("**********************************************")

    print('¿Estás preparado para jugar? (S/N)')
    sel = input('>> ')
    if sel == 'S' or 's':
        break
    elif sel == 'N' or 'n':
        print('¿Deseas leer otra vez las normas?')
        sel = input('>> ')
        if sel == 'N' or 'n':
            print('Cargando el juego...')
    else:
        print('Por favor ingrese un valor adecuado') 

#Player 1
os.system('cls')
print("**********************************************") 
print("*                                            *")
print("*             Eres el jugador 1              *")
print("*                                            *")
print("**********************************************") 

while si == False:
    print("¿Qué palabra deseas escribir?") #Word var
    word = input(">> ")
    print("¿Esta es la palabra deseas usar?(S/N)")
    sel = input(">> ") #Confirm selection
    if sel == 'S' or 's':
        si = True
    elif sel == 'N' or 'n':
        si = False
        print('Saliendo del juego...')
        time.sleep(0.5)
        os.system('exit')
    word = word.upper() #Min Max Converter

#Player2
os.system('cls')
print("**********************************************") 
print("*                                            *")
print("*             Eres el jugador 2              *")
print("*                                            *")
print("**********************************************") 

for letra in word:
    print(" _ ", end=" ")
    
print("")

i = len(word)

while life > 0:
    tirada += 1

    if tirada % 2 == 0:
        print('\npar')
        par = True
    else:
        print('\nimpar')
        par = False
    
    print("\nLetras usadas: ",usadas)

    if par == False:
        mylet = "A"
        while mylet in vocal:
            mylet = ""
            while mylet in usadas:
            #Define words
                mylet = input("\nIntroduce una letra consonante: ")
                mylet = mylet.upper() #Convert Majus to Min
    if par == True:
        mylet = ""
        while mylet not in vocal:
            while mylet in usadas:
            #Define words
                mylet = input("\nIntroduce una letra vocal: ")
                mylet = mylet.upper() #Convert Majus to Min
    myword += mylet
    usadas.append(mylet)

    for letra in word:
        if letra in myword:
            print(letra, end = " ")
            i -= 1
            
        else:
            print(" _ ", end=" ")

    if mylet not in word:
        life -= 1
        print("\nTe has equivocado")
        print("\nTe quedan ",life," vidas")
        print(muerto[err])
        err += 1
        
    if i == 0: #If we have all words on the secret word program finish
        print(" ")
        os.system('cls')
        print("**********************************************") 
        print("*                                            *")
        print("*                Has ganado                  *")
        print("*                                            *")
        print("**********************************************")
        print(" ")
        break

    if life == 0:
        print("")
        os.system('cls')

        print("**********************************************") 
        print("*                                            *")
        print("*                Has perdido                 *")
        print("*                                            *")
        print("**********************************************")
        print(muerto[7])
        print("\n")
        input("FINAL DEL CODIGO")
        break

input('FINAL DEL CODIGO')