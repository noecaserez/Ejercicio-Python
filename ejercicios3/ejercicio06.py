"""
Ejercicio 6: Crear una función que devuelva por pantalla un mensaje ingresado por parámetro pero en modo Title.
Si el mensaje ya está en modo title, que devuelva por pantalla "El mensaje ya está en modo title: {mensaje}"
"""

#Ejercicio 6:

def mensaje(msj): 
    if msj.istitle():
        print(f"El mensaje ya esta en modo title:  {msj} ")
    else:
        print(f"Este mensaje fue convertido en title: {msj.title()}")

mensaje("Las Funciones Si Que Me Estan Costando")

mensaje("este mensaje no estaba en modo title")

#Si el mensaje no esta puesto en modo tittle, aunque le haya colocado el ".title" no me lo comvierne.


#mensaje es la funcion, y no esta definida, tengo que colocarla al final, 
# en este caso tengo que colocar el mensaje que quiero que se modifique al final del codigo

#msj es lo que usare para darle forma a la funcion, tengo que mencionarlo dentro 
# de este y al final solo iria "mensaje" que es lo que se llama, lo principal
