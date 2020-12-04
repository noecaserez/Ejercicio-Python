# Ejercicio 14: Crear un programa que pregunte al usuario su nombre, 
# edad, dirección y teléfono y lo guarde en un diccionario. 
# Después debe mostrar por pantalla el mensaje.

# Ejercicio 14

datos = {

}


nombre = str(input("¿Cuál es su nombre?"))
edad = int(input("¿Cuál es su edad?"))
direccion = str(input("¿Cual es su dirección?"))
telefono = int(input("¿Cual es su telefono?"))
datos.update(dict(nombre=nombre, edad=edad, direccion=direccion, telefono=telefono))

print(datos)