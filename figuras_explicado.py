alt = int(input("Dime la altura: "))
anc = int(input("Dime la anchura: "))

for altura in range(alt):
    for anchura in range(anc):
        print("(I = {}, J = {}) ".format(altura,anchura),end="")
    print()