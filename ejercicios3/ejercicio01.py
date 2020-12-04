"""
Ejercicio 1: Crear una función que, a partir de un dato de entrada
que sea en horas, nos informe cuántos minutos y 
cuántos segundos serían esas horas. Imprimir por 
pantalla dichos valores.
"""

#Ejercicio 1

def horas_ingresadas(horas):
    minutos = horas * 60
    segundos = horas * 3600
    print(f"Las horas ingresadas '{horas}' son '{minutos}' minutos y '{segundos}' segundos")

horas_ingresadas(1)
horas_ingresadas(24)