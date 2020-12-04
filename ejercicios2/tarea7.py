""" Ejercicio 7: Crear un diccionario con 5 estudiantes y
 sus respectivas notas. Imprimir por pantalla los alumnos 
 que aprobaron y su nota (no en forma de diccionario, si no 
 con nombre : nota). Tener en cuenta que para aprobar el alumno
  debe sacarse una nota mayor o igual a 7 y menor o igual a 10.
  """

  #Ejercicio 7:

estudiantes = {
    "Noelia" : 9,
    "Angelica" : 10,
    "Patricia" : 9,
    "Evelyn" : 8,
    "Lais" : 4,
    "Larisa" : 7
}
"""
aprobados = {}

for n, p in estudiantes.items():
    notas = p
    estudiante = n
    if 7 <= notas <= 10:
        aprobados.update({n:p})
        print(f"Alumnos aprobados con nota mayor o igual a 7: {aprobados}")  
        
#imprime por pantalla la lista correcta pero cada resultado lo hace en una linea diferente y se acumula
"""

for nombre, nota in estudiantes.items():  #separo el nombre y la nota,luego formateo el dicccionario ()
    if 7 <= nota <= 10:
        print(f"Aprobado con nota mayor o igual a 7: \n {nombre} : {nota}")

