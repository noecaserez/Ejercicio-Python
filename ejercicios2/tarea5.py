""" Ejercicio 5: Crear un diccionario con los meses del 
año de la forma { 1: "enero"}. Desafío: lograr cambiar 
las claves. Pista: si imprimen ítems del diccionario
 les crea una lista. Una vez que lo logren, imprimir el diccionario modificado.

 """
#con cambiar las claves se refiere al orden, invertirlas.

 #Ejercicio 5:

meses_año = {
    1 : "Enero",
    2 : "Febrero",
    3 : "Marzo",
    4 : "Abril",
    5 : "Mayo",
    6 : "Junio",
    7 : "Julio",
    8 : "Agosto",
    9 : "Septiembre",
    10 : "Octubre",
    11 : "Noviembre",
    12 : "Diciembre" 
}

lista_numeros = list(meses_año.keys()) 
lista_meses = list(meses_año.values())
meses_año.clear() #para limpiar la lista si no saldra por duplicado

meses_año = dict(zip(lista_meses, lista_numeros)) 

"""imprimo meses_año pero esta vez ya esta previamente convertido
en lista y luego esta misma lista se convierte en diccionario con "dict" se los une con "zip"
"""

print(meses_año)

    