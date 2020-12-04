"""
Ejercicio 9: Crear un diccionario con 10 estudiantes y sus respectivas notas.
Luego crear una función que nos informe
los estudiantes aprobados (nota >= 7),
los estudiantes desaprobados (4 <= nota < 7) y los estudiantes aplazados (0 <= nota < 4).

"""

#Ejercicio 9:

estudiantes = {
    "Noelia" : 9,
    "Andrea" : 10,
    "Patricia" : 9,
    "Luis" : 4,
    "Catalina" : 10,
    "Leonardo" : 8,
    "Raul" : 7,
    "Esteban" : 10,
    "Mauricio" : 2,
    "Bruno" : 7
}

def notas_finales():
    aprobados = {}
    desaprobados = {}
    aplazados = {}
    for n, p in estudiantes.items():
        if p >= 7:
            aprobados[n] = p
        elif 4 <= p < 7:
            desaprobados[n] = p
        elif 0 <= p < 4:
            aplazados[n] = p
    print(f"Alumnos Aprobados: {aprobados}")
    print(f"Alumnos Desaprobados: {desaprobados}")
    print(f"Alumnos Aplazados: {aplazados}")
notas_finales()
