"""
Ejercicio 7: Crear un diccionario con 5 estudiantes y sus respectivas notas.
Imprimir por pantalla los alumnos que aprobaron y su nota (no en forma de diccionario, sino con nombre : nota).
Tener en cuenta que para aprobar el alumno debe sacarse una nota mayor o igual a 7 y menor o igual a 10.
"""

notas = {
    "María Perez": 8,
    "Juan Lopez": 10,
    "Ana García": 7,
    "Lucas Gomez": 5,
    "Lucía Fernandez": 6
}

for nombre, nota in notas.items():
    if nota >= 7:
        print(f"{nombre} : {nota}")

