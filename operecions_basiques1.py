
def sum (a , b ):
    resultadoab = a+b
    return resultadoab

print('Suma')
print(sum(10, 100))

def resta (c,d):
    resultadocd = c-d
    return resultadocd

print('Resta')
print(resta(90, 30))

def multi(e,f):
    resultadoef = e*f
    return resultadoef

print('Multi')
print(multi(2,6))

def divi(g,h):
    try:
        resultadogh = g/h
        return resultadogh
    except ZeroDivisionError:  # error de 0
        print('estas intentando dividit por cero')

print(divi(50,10))
