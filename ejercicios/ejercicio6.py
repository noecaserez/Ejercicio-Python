""" Ejercicio 6: Crear un programa que calcule 
cuánto dinero tendré al cabo de un mes si 
deposito hoy 2000 en el banco y el interés 
mensual es de 5%, y luego devuelva por pantalla ese valor.

""" 

#Ejercicio 6


deposito = int(input("Monto dinero que quiere depositar: "))


print(f"Valor de interés al cabo de un mes {deposito * 1.05}")


#Colocar {deposito * 1.05} me ahorra el paso de colocar {deposito * 0.05 + deposito}
# De ese modo no tengo que sacar el porcentaje y sumarlo luego, si no que se suma solo.
