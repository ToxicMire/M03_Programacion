print('Hello')
def funcionA(a,b): #excepcion de un objeto 
    print('la division entre a y b es: ', a/b)
    #ZeroDyvisionError: division by zero

def funcionb(cadena):
    assert_cadena!='casa', 'no me puedes pasar casa'
    print(cadena)
    #AssertionError 

def funcionc(a,b)
    try:
        opcion = int(input('Dame una opcion numerica'))
        print('a')
        assert a > 0, 'a no puede ser segativo'
        print('la division entre a y b es: ', a/b)
        print('b')
        #Son especificaciones 
    except ZeroDivisionError:  #error de 0 
        print('estas intentando dividit por cero') 
    except AssertionError: #error de numero negarivo
        print('estas pasando un numero negativo ')
    except ValueError: #error de numero si pones una letra
        print('No es un numero')
    except: #error comun poner al fianl de toda la lista 
        print('error desconocido')
        

#funcionA(4,0)
#funcionb('dfkslfkas<<jifsjk')
#funcionb('casa')
funcionc(2,2)


def funciond(iterable):
    try: 
        if type(iterable) not in  (list, dict, tuple , str) #si es diferente a una lista diccionario tupla y str 
            raise TypeError ('no me estas pasando un elemento iterable')
        for i in range iterable:
            print('i')
        except TypeError:
            print('Deberias pasar un elemento iterable')
        finally:
            print('Final de programa...')

funciond(['a', 'b']) #dicionarios listas tupla
