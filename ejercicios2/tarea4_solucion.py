"""
Ejercicio 4: Ingresar 6 números por teclado,
preferentemente enteros, ordenarlos de manera creciente e imprimirlos por pantalla.
"""

# solución

lista_numeros = []
for i in range(6):
   num = int(input("Ingrese un número: "))
   lista_numeros.append(num)
lista_numeros.sort()

for numeros in lista_numeros:
    print(numeros)
