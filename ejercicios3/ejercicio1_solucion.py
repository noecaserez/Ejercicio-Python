"""
Ejercicio 1: Crear una función que, a partir de un dato de entrada que sea en horas,
nos informe cuántos minutos y cuántos segundos serían esas horas. Imprimir por pantalla dichos valores.
"""

# Solución

def min_seg(horas):
    minutos = horas * 60
    seg = horas * 3600
    print(f"{horas} horas son {minutos} minutos y {seg} segundos.")

min_seg(10)
min_seg(24)

