# Ejercicio 16: Crear un programa que cree un diccionario 
# vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que 
# se le pida al usuario. Cada vez que se añada un nuevo dato debe
#  imprimirse el contenido del diccionario.



#Ejercicio 16

informacion_personal = {}

continuar = "s"

while continuar == "s":
    key = input("Dato a ingresar: ")
    value = input(f"valor del dato {key} :  ")
    informacion_personal[key] = value
    print(informacion_personal)
    continuar = input("si desea continuar agregando datos oprima 's', caso contrario oprima 'n' : ").lower()

