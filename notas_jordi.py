Nota = input('Dime tu nota y te digo si esta aprvado 1 - 10  \n>')
nota = float(Nota)

if nota <=5:
    print('Tu resultado es Suspenso')
elif  nota < 6:
    print('Tu resultado es Bien')
elif nota < 7:
    print('Tu resultado es Notable')
elif nota <=9:
    print('Tu resultado es Excelente')
elif nota <=10:
    print('Tu resultado es Matricula')
else:
    print('No me has dado una nota correcta')