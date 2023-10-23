print("Vamos a dibujar un rectangulo \n")
altura = int(input("Dame el alto del rectangulo -> "))
ancho = int(input("Dame la ancho del rectangulo -> "))
#el 0 o el -1 se refiere a la posicion del range  

for i in range(altura):
    for j in range(ancho):
        #Parte exterior
        if i == 0 or  i == altura - 1 or j == 0 or j == ancho-1:
            if (i == 0 and j == 0) or (i == 0 and j == ancho-1) or \
                    (i == altura-1 and j ==0) or ( i== altura-1 and j == ancho -1):
                    print("x",end="")
            else:
             print("-",end="")
        #Cuadrado
        elif i == 1 or i == altura -2 or j == 1 or j == ancho-2:
            print("x",end="")
        else:
             print("-",end="")
    print()
  