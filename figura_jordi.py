print("Vamos a dibujar un rectangulo \n")
alto = int(input("Dame el alto del rectangulo -> "))
ancho = int(input("Dame la ancho del rectangulo -> "))
#el 0 o el -1 se refiere a la posicion del range  

for i in range(alto):
    for j in range(ancho):
        if (i ==j) or (i+j==ancho-1) :
            print("*",end="")
        else :
            print("-", end="")
    print()