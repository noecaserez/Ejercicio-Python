"""
Ejercicio 10: Crear una función decoradora para una función matemática cualquiera.
"""

#Ejercicio 10:

def funcion_deco(funcion_interna):
    def funcion_mate(*args):
        print("Realizando calculo...\n")
        funcion_interna(*args)
  
    return funcion_mate 

@funcion_deco

def suma(a, b, c):
    print(f"El resultado de la suma es: {a + b + c}")

suma(100, 100, 0)

def resta(a, b):
    print(f"El resultado de la Resta es: {a - b}")

resta(100, 20)

def multiplicacion(a,b):
    print(f"El resultado de la multiplicación es: {a * b}")

multiplicacion(2, 5)

print("\nCalculo terminado.")