"""
Ejercicio 2: Crear una función que devuelva una lista con todos los números pares del 0 al 100 inclusive.
Imprimir esa lista por pantalla.
"""

# Solución

def pares_100():
    lista_pares100 = []
    for i in range(101):
        if i % 2 == 0:
            lista_pares100.append(i)
    return lista_pares100

print(pares_100())
