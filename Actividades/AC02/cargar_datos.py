from collections import deque
"""
Aquí debes completar las funciones propias de Poblar el Sistema
¡OJO¡: Puedes importar lo que quieras aquí, si lo necesitas
"""


"""
Esta estructura de datos te podría ser útil para el desarollo de la actividad, puedes usarla
si así lo deseas
"""

DICT_PISOS = {
    'Chief Tamburini': 'Piso -4',
    'Jefe': 'Piso -3',
    'Mentor': 'Piso -2',
    'Nuevo': 'Piso -1',
}


def cargar_alumnos(ruta_archivo_alumnos):
    print(f'Cargando datos de {ruta_archivo_alumnos}...')
    with open(ruta_archivo_alumnos, "r", encoding="utf-8") as file:
        datos = file.readlines()
    alumnos = deque()
    for dato in datos:
        alumno = dato[:-1].split(";")
        alumno[1] = set(alumno[1].split(",")) 
        alumnos.append(alumno)
    return alumnos


def cargar_ayudantes(ruta_archivo_ayudantes):
    print(f'Cargando datos de {ruta_archivo_ayudantes}...')
    with open(ruta_archivo_ayudantes, "r", encoding="utf-8") as file:
        datos = file.readlines()
    nuevo = deque()
    mentor = deque()
    jefe = deque()
    chief = deque()
    ayudantes = {"Nuevo": nuevo, "Mentor": mentor, "Jefe": jefe,
                 "Chief Tamburini": chief}
    for dato in datos:
        ayudante = dato[:-1].split(";")
        ayudante[2] = set(ayudante[2].split(","))
        ayudante.append(None)
        ayudantes[ayudante.pop(1)].append(ayudante)
    return ayudantes
