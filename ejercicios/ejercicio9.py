"""Ejercicio 9: Crear un programa que pregunte 
al usuario 5 números enteros y devuelva una lista con ellos

"""

#Ejercicio 9

numeros_5 = []

for i in range(5):
    numeros = int(input("ingrese 1 numero entero: "))
    numeros_5.append(numeros)

print(numeros_5) 

# Creo una lista vacia llamada "numeros_5" 
#creamos otra variable for que nos permita poner un limite de 5 numeros,
# el .append() nos permite rellenar la lista, agrega los numeros al final de la misma en 
# caso de que ya tenga informacion adentro.
#  