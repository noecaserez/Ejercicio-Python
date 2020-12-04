"""
Ejercicio 2: Crear una función que devuelva una lista con todos los números pares del 0 al 100 inclusive.
Imprimir esa lista por pantalla.
"""

#Ejercicio 2

def numeros_pares():
    numeros_pares = []
    for i in range(0,101):
        if i%2 == 0:  #para pares
            numeros_pares.append(i)
    return numeros_pares


"""
def numeros_impares():
    numeros_impares = []
    for i in range(0,101):
        if i%2 != 0:
            numeros_impares.append(i)
    return numeros_impares


print(numeros_impares())
"""

print(numeros_pares())