"""
Ejercicio 5: Crear un diccionario con los meses del año de la forma { 1: "enero"}.
Desafío: lograr cambiar las claves.
Pista: si imprimen ítems del diccionario les crea una lista.
Una vez que lo logren, imprimir el diccionario modificado.
"""

# Solución

meses = {
    1: "enero",
    2: "febrero",
    3: "marzo",
    4: "abril",
    5: "mayo",
    6: "junio",
    7: "julio",
    8: "agosto",
    9: "septiembre",
    10: "octubre",
    11: "noviembre",
    12: "diciembre"
}

lista_meses = list(meses.values())
lista_nums = list(meses.keys())
meses.clear()

meses = dict(zip(lista_meses, lista_nums))

print(meses)




