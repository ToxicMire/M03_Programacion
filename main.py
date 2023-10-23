mails = ["@@asref.com", "asef..asdf@asef.com", ".asf@asdf.com", "asdf..@awe.com", "asdf..@awe.com"
    , "sdfsdf@awe.com.", "sdfsdf@.awe.com", "sdfsdf@awe..com" ,"awer@wer.com","awer@wer.commmm","a@b.com", "a.b@c.com","a.b@c.com","a.b@c.d.es"]

usuario = ''
dominio = ''
inicio = 0 
final = 0 
cantAt = 0
count = mails.count(".")
index = 0

if ("a" > "z"):
    print("")

"f" >= "a" "f" <= "z"

for mail in mails:
    for c in mail:
        print(c)
        if (c == "@"):
            cantAt += 1
            if (cantAt > 1):
                print("FALLIDO: Doble @")
                break
            print("-> @ <-")
        if (mail[0] == "."):
            print("FALLIDO: Empieza por punto inicio")
            break
        if (len(mail) >= 2):
            if (mail[len(mail)-1] == "." and mail[len(mail)] == "."):
                print("FALLIDO: Dos puntos !")
                
    print("\n")
    cantAt = 0
    usuario = ""
    
    break
            