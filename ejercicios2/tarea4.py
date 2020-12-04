""" Ejercicio 4: Ingresar 6 números por teclado, preferentemente enteros, 
ordenarlos de manera creciente e imprimirlos por pantalla.

"""

#Ejercicio 4:

numeros_ordenados = []
for i in range(6):
    numeros = int(input("Ingrese 6 numeros: "))
    numeros_ordenados.append(numeros)
    numeros_ordenados.sort()

print(f"Números ingresados impresos por pantalla en orden: {numeros_ordenados}")