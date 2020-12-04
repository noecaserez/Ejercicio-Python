"""
Escribir un programa que almacene todas las letras del abecedario
y luego elimine las vocales
y nos devuelva una lista sin las vocales, sin modificar la original.
"""

# Solución
"""
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x", "y", "z"]
abecedario2 = abecedario.copy()


for i in abecedario2:
    vocales = ["a", "e", "i", "o", "u"]
    for vocal in vocales:
        if i == vocal:
            abecedario2.remove(i)
print(abecedario)
print(abecedario2)
"""

from string import ascii_lowercase

print(ascii_lowercase)
lista_abc = list(ascii_lowercase)
print(lista_abc)

