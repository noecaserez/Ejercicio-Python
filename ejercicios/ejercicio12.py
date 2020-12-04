# Ejercicio 12: Crear un programa que almacene los 
# vectores (1,2,3) y (-1,0,2) en dos listas y 
# muestre por pantalla su producto escalar.

#Ejercicio 12

lista1 = [1,2,3]                    #sumar las listas 3x2, 2x0, 1x-1 = 5
lista2 = [-1, 0, 2]
resultado = []            #El resultado de la suma de las listas colocarlo en una lista vacia, para eso usamos el append


for n in range(3):
    lista_suma = lista1[n] * lista2[n] 
    resultado.append(lista_suma)
    
print(sum(resultado))

