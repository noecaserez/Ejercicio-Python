"""
Ejercicio 6: Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title.
Si el mensaje ya está en modo title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"
"""

def modo_title(mensaje):
    if mensaje.istitle():
        print(f"El mensaje ya está en modo title: {mensaje}")
    else:
        mensaje.title()
        print(mensaje)

modo_title("Hola Qué Tal")