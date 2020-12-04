"""
Crear un programa que almacene los vectores (1,2,3) y (-1,0,2)
en dos listas y muestre por pantalla su producto escalar.
"""

vector_1 = [1, 2, 3]
vector_2 = [-1, 0, 2]
vector_prod_escalar = []

for i in range(3):  # (0, 1, 2)
    elemento = vector_1[i] * vector_2[i]
    vector_prod_escalar.append(elemento)

print(sum(vector_prod_escalar))








