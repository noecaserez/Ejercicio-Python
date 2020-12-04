"""
Crear un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje.
"""

# Solución

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
direccion = input("Ingrese su dirección: ")
tel = input("Ingrese su teléfono: ")

datos_usuario = {}
datos_usuario["Nombre"] = nombre
datos_usuario["Edad"] = edad
datos_usuario["Dirreción"] = direccion
datos_usuario["Teléfono"] = tel

print(datos_usuario)