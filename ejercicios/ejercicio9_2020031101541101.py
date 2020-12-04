"""
Crear un programa que pregunte al usuario 5 números enteros
y devuelva una lista con ellos.
"""

# Solución

n = 0
lista = []
"""
while n < 5:
    numero = int(input("Ingrese un número: "))
    lista.append(numero)
    n += 1

print(lista)
"""
for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

print(lista)



