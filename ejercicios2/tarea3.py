""" Ejercicio 3: Pedir al usuario que ingrese por teclado 2 números,
si el primero es menor que el segundo imprimir la resta entre 
el segundo y el primero, si el primero es mayor que el segundo 
imprimir la suma de ambos, y si son iguales imprimir su producto.

"""

#Ejercicio 3

numero1 = int(input("Ingrese un número: "))
numero2 = int(input("Ingrese otro número: "))

if numero1 < numero2:
    print(f"Como el numero 1 es menor que el numero 2 ingresado, restamos el 2 - 1, el resultado sera: {numero2 - numero1}")  
if numero1 > numero2:
    print(f"Como el numero 1 es mayor que el numero 2 los sumaremos, su resultado: {numero1 + numero2}")
if numero1 == numero2:
    print(f"Como ambos numeros son iguales los multiplicamos, el resultado es: {numero1 * numero2}")

 