"""
Ejercicio 10: Crear una función decoradora para una función matemática cualquiera.
"""

def deco(decorada):
    def decoracion(*args):
        print("La siguiente es una función matemática: ")
        decorada(*args)
    return decoracion

@deco

def suma(a, b):
    print(f"Función suma: resultado de la suma entre {a} y {b}")
    print(a + b)

@deco

def resta(a, b):
    print(f"Función resta: resultado de la resta entre {a} y {b}")
    print(a - b)


suma(10, 10)
resta(25, 10)