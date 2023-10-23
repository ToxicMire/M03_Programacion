import re
#usuario
nombre_usuario = input("Ingresa un nombre de usuario: ")
if 6 <= len(nombre_usuario) <= 12 and nombre_usuario.isalnum():
    print("El nombre de usuario es válido.")
else:
    print("El nombre de usuario debe tener entre 6 y 12 caracteres y ser alfanumérico.")

#Contraseña 
contraseña = input("Ingresa tu contraseña: ")
if len(contraseña) < 8:
    print("La contraseña debe tener al menos 8 caracteres.")
elif len(re.findall(r'[a-z]', contraseña)) < 3:
    print("La contraseña debe contener al menos 3 letras minúsculas.")
elif len(re.findall(r'[A-Z]', contraseña)) < 3:
    print("La contraseña debe contener al menos 3 letras mayúsculas.")
elif len(re.findall(r'\d', contraseña)) < 1:
    print("La contraseña debe contener al menos 1 dígito.")
elif len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', contraseña)) < 1:
    print("La contraseña debe contener al menos 1 carácter no alfanumérico.")
else:
    print("La contraseña es válida.")


#############################################################################################
passwo = ''
pass_valido = True

if len(passwo)<8:
    pass_valido = False
    print('menos de 8 caracteres')
if ' ' in passwo:
    pass_valido = False
    print('Tiene espacios en blanco')
if passwo.isalnum():
    pass_valido = False
    print('Tiene espacios en blanco')
if passwo.upper() == passwo:
    pass_valido = False
    print('No tiene minusculas ')
if passwo.lower() == passwo:
    pass_valido = False
    print('No tiene mayusculas ')

contiene_num = False
for letras in passwo:
    if letras.isdigit():
        contiene_num = True
        break
    if not contiene_num:
        contiene_num = False
        print('No tiene numeros')

if pass_valido:
    print('Password valido')
    
else:
    print('Passqord invalido')