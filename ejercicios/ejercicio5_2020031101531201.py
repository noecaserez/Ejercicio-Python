"""

Crear un programa que pida al usuario ingresar 2 números por teclado
y devuelva por pantalla la suma de ellos en un renglón,
la resta en otro, el producto en otros y la división en otro.

"""

num = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
print("\n")
print(f"La suma de {num} y {num2} es {num + num2}")
print(f"La resta entre {num} y {num2} da {num - num2}")
print(f"El producto entre {num} y {num2} es {num * num2}")
print(f"La división entre {num} y {num2} da {num / num2}")

