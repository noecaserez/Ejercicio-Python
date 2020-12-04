"""
Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo o no.
En caso de que lo sea devolver por pantalla "La palabra es un palíndromo", e
n caso contrario, devolver "La palabra no es un palíndromo".
"""

def palindromo(palabra):
    palabra_reverse = palabra[::-1]
    if palabra == palabra_reverse:
        print("La palabra es un palíndromo")
    else:
        print("La palabra no es un palíndromo")

palindromo("maría")