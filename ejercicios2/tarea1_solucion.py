"""
Ejercicio 1: Pedir al usuario que ingrese un mensaje cualquiera,
si el mensaje tiene más de 100 caracteres imprimirlo por teclado,
si tiene entre 50 y 100 caracteres imprimirlo al revés,
si no se cumple ninguna de las opciones anteriores,
por pantalla devolver un mensaje que diga "su mensaje es demasiado corto".
"""

mensaje = input("Ingrese un mensaje cualquiera: ")

if len(mensaje) >= 100:
    print(mensaje)
elif 50 <= len(mensaje) < 100:
    print(mensaje[::-1])
else:
    print("Su mensaje es demasiado corto.")


# slicing

# listas, tuplas y strings --> objetos iterables

# mensaje[start:stop:step]







