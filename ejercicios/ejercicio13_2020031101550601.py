"""
Crear un programa que guarde en una variable
el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
pregunte al usuario por una divisa
y muestre su símbolo o un mensaje de aviso
si la divisa no está en el diccionario.
"""

divisas = {
    "Euro" : "€",
    "Dollar" : "u$s",
    "Yen" : "¥"
}

divisa = input("""
Elija una divisa:
    - presione E o e para Euro
    - presione D o d para Dollar
    - presione Y o y para Yen
""")

if divisa.lower() == "e":
    print(divisas["Euro"])
elif divisa.lower() == "d":
    print(divisas["Dollar"])
elif divisa.lower() == "y":
    print(divisas["Yen"])
else:
    print("No seleccionó ninguna de las opciones propuestas.")


# Otra solución

divisas = {
    'Euro':'€',
    'Dollar':'$',
    'Yen':'¥'
}
divisa = input('Ingrese una divisa: ')

if divisa in divisas:
    print(divisas[divisa])
else:
    print('Esta divisa no está en el diccionario')