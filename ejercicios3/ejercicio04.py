"""
Ejercicio 4: Crear una función que, a partir de 4 números,
devuelva el mayor producto de dos de ellos. Imprimir resultado por pantalla.
"""

#ejercicio 4
def producto():
    producto_numeros = []
    for i in range(4):
        numero = int(input("Ingrese un número: "))
        producto_numeros.append(numero)
    producto_numeros.sort()
    for num in producto_numeros:
        if num == 0:
            producto_numeros.pop(num)
            producto_mayor = producto_numeros[-2] * producto_numeros[-1]
        else:
            producto_mayor = producto_numeros[-2] * producto_numeros[-1] #si le quito el else la funcion da error, porque?
    print(producto_mayor)

producto()

"""
esta funcion te pide 4 numeros, los ordena en una nueva lista de menor a mayor y los dos ultimos
osea los dos mayores son multiplicados

en una lista
[-2] siendo el -2 el ante ultimo
[-1] siendo -1 el índice del último elemento
"""