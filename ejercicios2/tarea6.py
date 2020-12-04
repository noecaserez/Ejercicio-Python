""" Ejercicio 6: Escribir un programa que seleccione una 
operación de cuatro operaciones numéricas disponibles, 
una vez seleccionada la operación, introducir dos números y ejecutar la operación.
"""

#Ejercicio 6:


operaciones = int(input("""Escriba que operacion matemática desea hacer
Suma:1 
Resta:2 
Multiplicación:3 
Division:4
"""))

if operaciones == 1:
    num1 = int(input("Ingrese un numero: "))
    num2 = int(input("Ingrese un numero: "))
    print(f"La suma entre ambos numeros es: {num1+num2}")
elif operaciones == 2:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese un numero: "))
    print(f"La Resta entre ambos números es: {num1-num2}")
elif operaciones == 3:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese un numero: "))
    print(f"La Multiplicación entre ambos números es: {num1*num2}")
elif operaciones == 4:
    num1 = int(input("Ingrese un número: "))
    num2 = int(input("Ingrese un numero: "))
    print(f"La División entre ambos números es: {num1/num2}")
else:
    print("La opción elegida no es correcta")



"""

if 0 < operaciones <= 4:  #no comprendo esta parte, porque operaciones se ejecuta bien si 0 es < a operaciones
    print("Ingrese un número: ")
    num1 = int(input())
    print("Ingrese un número: ")
    num2 = int(input())
    if operaciones == 1:
        print(f"La suma entre ambos numeros es: {num1+num2}")
    elif operaciones == 2:
        print(f"La Resta entre ambos números es: {num1-num2}")
    elif operaciones == 3:
        print(f"La Multiplicación entre ambos números es: {num1*num2}")
    elif operaciones == 4:
        print(f"La División entre ambos números es: {num1/num2}")
    else:
        print("El número elegido no es correcto")

"""
