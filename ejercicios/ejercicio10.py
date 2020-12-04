# Ejercicio 10: Escribir un programa que almacene 
# todas las letras del abecedario y luego elimine 
# las vocales y nos devuelva una lista sin las vocales, sin modificar la original.

#Ejercicio 10

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


abecedario.remove('a')
abecedario.remove('e')
abecedario.remove('i')
abecedario.remove('o')
abecedario.remove('u')

print(abecedario)


"""
for i in abecedario:
    vocales = ['a', 'e', 'i', 'o', 'u']
    for vocal in vocales:
        if i == vocal:
            abecedario.remove(vocal)

print(abecedario)

"""

# con .remove() solo puedo quitar un argumento por vez

