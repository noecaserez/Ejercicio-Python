# Ejercicio 15: Crear un programa que almacene el diccionario
#  con los créditos de las asignaturas de un 
# curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y
#  después muestre por pantalla los créditos de cada asignatura 
# en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es 
# cada una de las asignaturas del curso, y <créditos> son sus créditos. 
# Al final debe mostrar también el número total de créditos del curso.


#Ejercicio 15

creditos_asignaturas = {
    "Matematicas" : 6,
    "Fisica" : 4,
    "Quimica" : 5
}

creditos_totales = [6, 4, 5]

for asignatura, creditos in creditos_asignaturas.items(): #asignatura, creditos (se toma en orden: clave, valor dentro del diccionario y teniendo en cuenta los items dentro de este)
    print(f"la asignatura {asignatura} tiene {creditos} creditos")

print(f"\nEl número total de creditos en el curso es de {sum(creditos_totales)}")



"""
mate = creditos_asignaturas[Matematicas]
fis = creditos_asignatura[Fisica]
quim = creditos_asignatura[Quimica]
print(f"la nota de Matematicas {mate} creditos")

"""