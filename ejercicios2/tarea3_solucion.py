"""
Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números,
si el primero es menor que el segundo imprimir la resta
entre el segundo y el primero, si el primero es mayor que el segundo imprimir la suma de ambos,
y si son iguales imprimir su producto.
"""

numero_1 = int(input("Ingrese el primer número: "))
numero_2 = int(input("Ingrese el segundo número: "))

if numero_1 < numero_2:
    print(numero_2 - numero_1)
elif numero_1 > numero_2:
    print(numero_1 + numero_2)
else:
    print(numero_1 * numero_2)

