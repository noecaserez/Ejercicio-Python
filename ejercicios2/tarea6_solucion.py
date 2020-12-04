"""
Ejercicio 6: Escribir un programa que seleccione una operación de cuatro operaciones numéricas disponibles,
una vez seleccionada la operación, introducir dos números y ejecutar la operación
"""

opcion = int(input("""
    Seleccionar la operación que desea realizar:
    1 - Suma
    2 - Resta
    3 - Producto
    4 - División
    """))

if 0 < opcion <= 4:
    print("Ingrese dos números: ")
    num1 = int(input())
    num2 = int(input())
    if opcion == 1:
        print(num1 + num2)
    elif opcion == 2:
        print(num1 - num2)
    elif opcion == 3:
        print(num1 * num2)
    else:
        print(num1 / num2)
else:
    print("No ingresó ninguna opción correcta.")
