"""
Crear un programa que almacene el diccionario con los créditos de las asignaturas de un curso
{'Matemáticas': 6, 'Física': 4, 'Química': 5}
y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos,
donde <asignatura> es cada una de las asignaturas del curso,
y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.
"""

# Solución

creditos = {
    "Matemáticas" : 6,
    "Física" : 4,
    "Química" : 5
}

total_creditos = 0

nota_mate = creditos["Matemáticas"]
print(f"La nota de matemática es {nota_mate}")

"""
for materia, nota in creditos.items():
    print(f"La materia {materia} tiene {nota} créditos")
    print(f"La nota de {materia} es {nota}")
    total_creditos += nota

print(f"El total de créditos es {total_creditos}")


"""
var = 9

lista = [1, 2, 3, var]
string = f"Tengo str{var} casas (mentira eh)"
gato = f"Mi gato tiene {var} años"
gato1 = "Mi gato tiene " + str(var) + " años"
print(gato)
print(gato1)







