""" Ejercicio 2: Crear una lista con 10 números enteros cualquiera. 
Indicar cuál es el número mayor y cuál es el número menor. 
Si al menos hay 3 números mayores a 100, imprimir esos números, 
si no, imprimir los números menores a 50 que formen parte de la lista.
"""

# Ejercicio 2

numeros = [5, 10, 20, 50, 100, 222, 56, 333, 444, 555, 666, 231]

numeros.sort()

mayor = max(numeros)
menor = min(numeros)

print(f"En la lista 'numeros' el N° menor es {menor} y el N° mayor es {mayor} ")

numeros_mayores_100 = []

for i in numeros:
    if i > 100:
        numeros_mayores_100.append(i)            

if len(numeros_mayores_100) >= 3:
    print(f"Hay al menos 3 numeros mayores a 100 y son: {numeros_mayores_100} ")
else:
    for menor in numeros:
        if menor < 50:
            print(f"numeros menores a 50 : {menor} ")




# Con funcion, que embole :/

"""
def es_mayor(n):
    if n >= 100:
        return True

def es_menor(n):
    if n <= 50:
        return True

filtrado = list(filter(es_mayor, numeros))

if len(filtrado) >= 3:
    print(filtrado)

else:
    filtrado = list(filter(es_menor, numeros))
    print(filtrado)

"""







"""
for numero in numeros:
    if numero >= 100:     
        if len(numeros) >= 3:
            print(f"Hay al menos 3 numeros mayores a 100 y son: {numero} ")
        else:
            for numero in numeros:
                if numero < 50:
                    print(f"numeros menores a 50 : {numero} ")

"""

    