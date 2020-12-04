# Ejercicio 13: Crear un programa que guarde en una 
# variable el diccionario
#  {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario
#  por una divisa y muestre su símbolo o un mensaje de aviso si 
# la divisa no está en el diccionario.

#Ejercicio 13

diccionario = {
    'Euro' : '€',
    'Dollar' : '$', 
    'Yen' : '¥'
}

moneda = input("Ingrese una divisa:\n Euro: \n Dollar: \n Yen:\n ").capitalize()
if moneda in diccionario:
    print(diccionario[moneda])
else:
    print("Esta divisa no se encuentra en el diccionario")




"""
Hola = input("Ingrese una divisa para saber su símbolo:\n euro: \n dollar: \n yen: \n ")
if Hola.lower() == 'euro':
    print(diccionario['Euro'])
elif Hola.lower() == 'dollar':
    print(diccionario['Dollar'])
elif Hola.lower() == 'yen':
    print(diccionario['Yen'])
else:
    print("La divisa no se encuentra en el diccionario")

"""


