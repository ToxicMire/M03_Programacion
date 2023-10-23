nombre_usuario = "jose"
puntos_usuario = 50
datos_rank = ["antonio:100"]

if len(datos_rank) == 0:
    datos_rank = nombre_usuario +":"+ str(puntos_usuario)+";"
else:
    for i in range(0,datos_rank):
        if ";" == 0:
            inicio = 0
            final = datos_rank.index(";")

        else:
            inicio = final + 1
            final = datos_rank.index(";", final +1)

        if int(datos_rank[inicio:final][datos_rank[inicio:final].index(":") +1:]) < puntos_usuario:
            datos_rank = datos_rank[:inicio] + nombre_usuario + ":" + str(puntos_usuario) + ";" + datos_rank[inicio:]

        if i == datos_rank.count(";") -1 and not int(datos_rank[inicio:final][datos_rank[inicio:final].index(":") +1:]) < puntos_usuario:


print(datos_rank)