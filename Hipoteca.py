importepres = int(input("Cual es el importe para el prestamo? \n ->"))
ingresos = int(input("Cuales son tus ingrasos anuales ? \n ->"))
coste = int(input("Dime el coste de la tassa del piso"))
termini = int(input("dime el terminio de pagos al año \n ->"))


hipote = False
recimen = importepres*2/(termini*12)

if importepres< coste*80/100:
 if recimen < (ingresos/12)*50/100:
  hipote = True

if hipote:
 print("se a cocedido la hipoteca")
 print("El importe mensual sera", recimen)
else:
 print("No se ha concedido la hipoteca")

