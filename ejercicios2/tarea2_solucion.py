"""
Ejercicio 2: Crear una lista con 10 números enteros cualquiera.
Indicar cuál es el número mayor y cuál es el número menor.
Si al menos hay 3 números mayores a 100, imprimir esos números,
si no, imprimir los números menores a 50 que formen parte de la lista.
"""

lista_numeros = [1, 34, 67, 99, 105, 125, 97, 44, 10, 147]
lista_numeros.sort()
numero_mayor = lista_numeros[-1]
numero_menor = lista_numeros[0]
print(f"El número mayor de la lista es {numero_mayor}, y el número menor de la lista es {numero_menor}")
mayores_100 = []
for i in lista_numeros:

    if i > 100:
        mayores_100.append(i)
if len(mayores_100) >= 3:
    for numero in mayores_100:
        print(numero)
else:
    for numero in lista_numeros:
        if numero < 50:
            print(numero)