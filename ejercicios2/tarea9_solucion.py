"""
Ejercicio 9: Pedirle al usuario que ingrese el monto disponible en su tarjeta de crédito.
Evaluar si puede realizar una compra de $2500,
si puede indicar cuánto saldo le queda luego de efectuarla.
Si no puede, indicar cuánto dinero le falta para poder realizarla.
"""

monto_dispo = float(input("Ingrese el monto disponible en su tarjeta de crédito: "))
compra = 2500
if monto_dispo >= compra:
    print("Tiene dinero disponible para realizar la compra.")
    print("Procesando compra...")
    print(f"Su saldo es de {monto_dispo - 2500}")
else:
    print(f"No tiene dinero para realizar la compra, le faltan {compra - monto_dispo}")