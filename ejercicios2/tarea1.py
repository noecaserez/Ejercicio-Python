""" Ejercicio 1: Pedir al usuario que ingrese un 
mensaje cualquiera, si el mensaje tiene más de 100 
caracteres imprimirlo por pantalla, si tiene 
entre 50 y 100 caracteres imprimirlo al revés, 
si no se cumple ninguna de las opciones anteriores, 
por pantalla devolver un mensaje que diga "su mensaje es demasiado corto".
"""

# Ejercicio 1

mensaje = str(input("Ingrese un mensaje: "))

if len(mensaje) > 100:
    print(mensaje)
if len(mensaje) >= 50 <= 100:
    print(mensaje[::-1])
else:
    print("Su mensaje es muy corto")