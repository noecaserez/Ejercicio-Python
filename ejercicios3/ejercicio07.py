"""
Ejercicio 7: Crear una función que verifique si una palabra es un palíndromo o no.
En caso de que lo sea devolver por pantalla "La palabra es un palíndromo", e
n caso contrario, devolver "La palabra no es un palíndromo".
"""

#Ejercicio 7

def palindromo(texto):
    reverso = texto[::-1]  #El [::-1] para hacer el reverso o invertir la palabra
    if texto == reverso:
        print(f"La palabra ingresada '{reverso}' es un palíndromo")
    else:
        print(f"La palabra ingresada '{reverso[::-1]}' no es palíndromo")

# Ingrese en (" ") su palabra para verificar si es un Palíndromo            
palindromo("neuquen")
palindromo("hola")
palindromo("salchicha")
palindromo("menem")
        



