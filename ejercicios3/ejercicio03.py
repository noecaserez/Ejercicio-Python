"""
Ejercicio 3: Crear una función que, a partir de un mensaje,
nos devuelva una lista con todos los números, si los hay, que aparecen en dicho mensaje.
"""

#Ejercicio 3

def mensaje(msj):
    numeros = []
    for caracter in msj:
        if caracter.isdigit():   #este es para num, y para caracteres alfabeticos .isalpha 
            numeros.append(caracter)
    print(numeros)  #por una mala identacion no me reconocia print(numeros) y daba error

mensaje("La hora es 23:00 y este ejercicio me costo caso 1 hora")


