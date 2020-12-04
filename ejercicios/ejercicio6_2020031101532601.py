"""
Crear un programa que calcule cuánto dinero tendré 
al cabo de un mes si deposito hoy 2000 en el banco 
y el interés mensual es de 5%, y luego devuelva por pantalla ese valor.

"""

monto_inicial = 2000
interes = 0.05
monto_mes = monto_inicial + monto_inicial * 0.05

print(f"Al cabo de un mes tendré {monto_mes:.2f} pesos")