"""
Ejercicio 8: Crear una función que calcule cuántos litros de nafta gasta un auto que consume 2 litros x 100km,
en un viaje ida y vuelta MdP-Bue si la distancia es de 400km.
Luego crear una función que, a partir de esos datos,
devuelva cuánto significa eso en pesos si el litro de nafta está 60$.
"""

#Ejercicio 8

def kilometros():
    litros_100km = 2 
    km = 100
    distancia_a_destino = 400
    litros_consumidos = litros_100km * distancia_a_destino / km
    return litros_consumidos

def costo(consumo):
    litro_nafta = 60
    gasto_total = litro_nafta * consumo
    print(f"Se gastaran  ${gasto_total}")

print("Litros consumidos por km indicados...")
print(kilometros())
print("\nDinero total gastado...")
costo(kilometros())

