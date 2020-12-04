"""
Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados son todos números,
False si hay al menos uno de los parámetros ingresados que no es un número, y
None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla.
"""

#Ejercicio 5

def num_parametros(*args): #el args es para cuando no se sabe la cantidad de parametros que se necesitaran, es indefinido
    numeros = []
    for arg in args:
        if type(arg) == int or type(arg) == float or type(arg) == complex:
            numeros.append(arg)
    if len(args) == len(numeros):
        return True
    elif len(args) != int:
        return False
    else:
        return None

print(num_parametros(23, "hola"))

print(num_parametros(99, 29))