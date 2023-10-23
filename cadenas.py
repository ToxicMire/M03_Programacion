cadena = 'esto es una cadena'
cadena1 = 'Esto es otra cadena'
print(cadena + cadena1)

print('-'*60)
cadena2 = 'Esto eS uNa caDena'
cadenaminus = cadena2.lower()
cadenamayus = cadena2.upper()
cadenatitu = cadena2.title()
cadenacapi = cadena2.capitalize()
cadenacenter = cadena2.center(80,'-')
cadenafind = cadena2.find('o') #es key sensitive  si ponemos ('n',numero) empieza desde esa posicion , si ponemos ('n',numero,numerp) empieza desde esa posicion  y hasta esa posicion


print(cadena2)
print(cadenaminus)
print(cadenamayus)
print(cadenatitu)
print(cadenacapi)
print(cadenacenter)
print(cadenafind)

print('-'*60)


cadenastart = cadena2.startswith('Es') #saca true o false, si ponemos ('n',1) es por donde empieza la cadena , si ponemos ('n',1,3) es por donde empieza la cadena y por donde acaba
cadenafinal = cadena2.endswith('na') #saca true o false, si ponemos ('n',1) es por donde empieza la cadena , si ponemos ('n',1,3) es por donde empieza la cadena y por donde acaba
cadenacount = cadena2.count('a') #si ponemos ('n',1) es por donde empieza la cadena , si ponemos ('n',1,3) es por donde empieza la cadena y por donde acaba
cadenasplit = cadena2.split('o') 
cadenareplace = cadena2.replace('o','A') 
cadenalstrip = cadena2.strip() #quita los espacios de delante y detras 

print(cadenastart)
print(cadenafinal)
print(cadenacount)
print(cadenasplit)
print(cadenareplace)