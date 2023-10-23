# los < de 18  *1.1
# ingresos menos de (nemher * 5700) +500  no va , si son += NO , si son mas de 4 her + 150€
# beca = 4000 (((numher * 5700)+ 500 -ingresos) / ((numher * 5700)+500))

edad = int(input('Dime tu edad > '))
ingresos = int(input('Dime los ingresos > '))
numher = int(input('Dime el numero de hermanos que tienes > '))
beca = 4000 * (((numher * 5700)+ 500 -ingresos) / ((numher * 5700)+500))


if ingresos <= ((numher * 5700) + 500):
    print('La beca no puede ser superior ')
if numher > 4:
    print('Tienes la beca por ser mas de 4 hermanos')
else:
    print('No puedes acceder a la beca ')
    
if edad < 18:
    beca = beca *1.1