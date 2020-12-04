""" Ejercicio 8: Pedirle al usuario que ingrese por teclado  
3 números binarios de 8 bits, para cada uno imprimir su 
siguiente (número + 1) pero en sistema decimal. Recuerden 
que los números binarios están compuestos por 1 y 0.
"""

#Ejercicio 8.

numero_decimal = 0

for i in range(3):
    numeros_binarios = input("Ingrese por teclado 1 numero binario de 8 bits: ")
    for num in numeros_binarios:
        numero_decimal = numero_decimal + int(num)
        print(numero_decimal + 1)




