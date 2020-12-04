"""
Crear un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.)
que se le pida al usuario.
Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
"""

# Solución

datos_usuario = {}
rta = "s"

while rta == "s":
    key = input("¿Qué dato vas a introducir? ")
    value = input(f"{key} : ")
    datos_usuario[key] = value
    print(datos_usuario)
    rta = input("¿Desea introducir más información? Presione s por sí y n por no: ").lower()



