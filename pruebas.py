Datos = 'Juan:150;Pepe:125;'
datos_dict = {}  # Crear un diccionario para almacenar los datos

inicio_nombre = 0
fin_nombre = 0
inicio_puntuacion = 0
fin_puntuacion = 0

for i in range(len(Datos)):
    caracter = Datos[i]
    if caracter == ":":
        fin_nombre = i
        inicio_puntuacion = i + 1
    elif caracter == ";":
        fin_puntuacion = i
        nombre = Datos[inicio_nombre:fin_nombre]
        puntuacion = int(Datos[inicio_puntuacion:fin_puntuacion])  # Convertir la puntuación a entero
        datos_dict[nombre] = puntuacion  # Almacenar en el diccionario
        inicio_nombre = i + 1

# Mover la siguiente parte del código al final del bucle for
nombre = Datos[inicio_nombre:fin_nombre]
puntuacion = int(Datos[inicio_puntuacion:fin_puntuacion])  # Convertir la puntuación a entero
datos_dict[nombre] = puntuacion  # Almacenar en el diccionario

# Imprimir el diccionario
for nombre, puntuacion in datos_dict.items():
    print("Nombre: {}, Puntuación: {}".format(nombre, puntuacion))
    
################################################################################################################################
Datos = 'Juan:150;Pepe:125;'
inicio_nombre = 0
fin_nombre = 0
inicio_puntuacion = 0
fin_puntuacion = 0

for i in range(len(Datos)):
    caracter = Datos[i]
    if caracter == ":":
        fin_nombre = i
        inicio_puntuacion = i + 1
    elif caracter == ";":
        fin_puntuacion = i
        nombre = Datos[inicio_nombre:fin_nombre]
        puntuacion = Datos[inicio_puntuacion:fin_puntuacion]
        print("Nombre: {}, Puntuación: {}".format(nombre, puntuacion))
        inicio_nombre = i + 1

nombre = Datos[inicio_nombre:fin_nombre]
puntuacion = Datos[inicio_puntuacion:fin_puntuacion]
print("Nombre: {}, Puntuación: {}".format(nombre, puntuacion))






