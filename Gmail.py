#Comprobante de mails 
mails = [".@asref.com", "asef..asdf@asef.com", ".asf@asdf.com", "asdf..@awe.com", "asdf..@awe.com"
    , "sdfsdf@awe.com.", "sdfsdf@.awe.com", "sdfsdf@awe..com" ,"awer@wer.com","awer@wer.commmm","a@b.com", "a.b@c.com","a.b@c.com","a.b@c.d.es"]


for mail in mails:#coje los mails 1 por 1 y los separa  
    pos_punt = -1
    pos_arrb = -1
    for cnt_lletra in range(0, len(mail)):
        lletra = mail[cnt_lletra]
        if lletra == ".":
            pos_punt = cnt_lletra
        if lletra == "@":
            pos_arrb = cnt_lletra
    usuari = mail[0:pos_arrb] # aqui encontramos el usuario 
    domini = mail[pos_arrb + 1:pos_punt] # aqui encontramos el dominio 
    print(f"{mail} - {usuari} > {domini}")

"""
    if inicio ==0: # mira los mails 1 por 1
        final = mail.index('.')
        for _ in range(count):
            final = mail.index(".", inicio)
            nombre = mail[inicio:final]
            index += 1
            inicio = final + 1
        nombre_separa = mail[inicio:]
        print(nombre_separa)
        input('Presiona cualquier tecla  > ')
        #siguiente separacion del usuario@dominio para poder hacer la compro
        
        
        

        
        index += 1
    else:
        print('Mail incorrecto')
        break
        
ar = 'asref.com'

#######################################################################################################################################################
email = input("Ingresa tu dirección de correo electrónico de Gmail: ")

# Verifica si el correo electrónico cumple con las condiciones
if email.count('@') == 1 and email.count('.') <= 1 and \
   not email.startswith('.') and not email.startswith('@') and \
   email.isalnum() and not email[-1].isdigit() and \
   len(email.split('.')[-1]) <= 3:
    print("La dirección de correo electrónico es válida.")
else:
    print("La dirección de correo electrónico no es válida según los criterios especificados.")
        
"""