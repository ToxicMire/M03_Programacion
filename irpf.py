dinero_bruto = int(input('Dime cuanto cobras de forma bruta al año \n> '))
irpf = 0 
total_irpf = 0
total = 0

if dinero_bruto < 12450:
    irpf = 19
    total = (dinero_bruto * irpf) / 100 
    total_irpf = total
elif dinero_bruto < 20200:
    irpf = 24
    total = ((dinero_bruto * irpf) / 100 ) + (dinero_bruto - 12450 )
    total_irpf =+ total
elif dinero_bruto < 35200:
    irpf = 30
    total = (dinero_bruto * irpf) / 100 - ((dinero_bruto * 24)/100)
    total_irpf =+ total
elif dinero_bruto < 60000:
    irpf = 37
    total = (dinero_bruto * irpf) / 100
    total_irpf =+ total
elif dinero_bruto < 300000:
    irpf = 45
    total = (dinero_bruto * irpf) / 100 
    total_irpf =+ total
else:
    irpf = 47
    total = (dinero_bruto * irpf) / 100
    total_irpf =+ total
    
print('Lo que tienes que pagar por el IRPF es {}€'.format(total_irpf))