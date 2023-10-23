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