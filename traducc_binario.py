#Bin a Hexa

cadena=1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"
resultado=0

bin=input("Dame la ip a traducir:")

listabin=bin.split(":")
print(listabin)

for i in listabin:
    for j in range(len(i)):
            resultado += int(i[j]) * 2 ** (len(i)-1-j)

    print(resultado)
# for i in range(2):
#     cadena= str(resultado %16 ) +  cadena
#     cadena = cadena + ":"
#     cadena = cadena[:-1]
# 10110100:10110110:01110110:11100011:11001111:11001101

