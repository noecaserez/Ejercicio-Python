"""
Ejercicio 5: Crear una función que devuelva True si los parámetros ingresados son todos números,
False si hay al menos uno de los parámetros ingresados que no es un número, y
None si ninguno de los parámetros ingresados es un número. Imprimir resultado por pantalla.
"""

# Solución

def comparacion(*args):
    cant_args_num = []
    for arg in args:
        if type(arg) == int or type(arg) == float or type(arg) == complex:
            cant_args_num.append(arg)
    if len(args) == len(cant_args_num):
        return True
    elif len(cant_args_num) != 0:
        return False
    else:
        return None


print((comparacion(1, 25)))