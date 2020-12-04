""" Ejercicio 9: Pedirle al usuario que ingrese el monto 
disponible en su tarjeta de crédito. Evaluar si puede 
realizar una compra de $2500, si puede indicar cuánto saldo 
le queda luego de efectuarla. Si no puede, indicar cuánto
 dinero le falta para poder realizarla.
 """

 #Ejercicio 9

dinero = int(input("Ingrese el monto disponible en su tarjeta de credito: "))

compra = 2500
monto_restante = 0 

if dinero >= 2500:
    print(f"Usted posee monto suficiente para realizar la compra.\nEl monto restante luego de la misma seria de: {dinero-compra}")
else:
    print(f"Necesita ${compra-dinero} par poder efectuar la compra")


