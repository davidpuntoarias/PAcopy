
"""
ANTES DE EMPEZAR A PROGRAMAR LA ACTIVIDAD, TE RECOMENDAMOS FUERTEMENTE LEER EL ENUNCIADO Y
ENTENDER BIEN LO QUE DEBE HACER TU PROGRAMA
"""

"""
Aquí debes importar las librerias que vayas a utilizar durante la actividad
"""
import os
from random import randint
from collections import deque
from cargar_datos import cargar_alumnos, cargar_ayudantes
from consultas import resumen_actual, stock_comida



"""
Esta estructura de datos se utilizará en la simulación, para avanzar piso por piso
"""
PISOS = deque(['Nuevo', 'Mentor', 'Jefe', 'Chief Tamburini'])


"""
Aquí debes completar las funciones propias de Acciones en DCCampal
"""


def distraer(alumno, ayudante):
    comidacompartida = list(alumno[1] & ayudante[1])
    indice = randint(0, len(comidacompartida))
    if comidacompartida != [] and len(alumno[1]) != 0:
        alumno.remove(comidacompartida[indice])
        ayudante[2] = comidacompartida[indice]
        return True
    return False


def simular_batalla(alumnos, ayudantes):
    """
    El malvado PhD. Pinto ha borrado todo el código de esta función,
    pero ha decidido dejar unas cuantas línea de la simulación
    """
    stock = stock_comida(alumnos)
    print('Les tengo información importante antes de empezar la batalla, '
          'aquí va el catastro de las de las habilidades de los alumnos:')
    print(stock)

    resumen_actual(ayudantes, alumnos)

    while PISOS and alumnos:
        # Mientras queden pisos y alumnos para distraer
        piso_actual = PISOS[0]
        ayudantes_del_piso = ayudantes[piso_actual]  # Debes obtener los ayudantes del piso
        while ayudantes_del_piso:
            # Mientras hayan ayudantes en el piso
            ayudante_defensor = ayudantes_del_piso[0] # Debes obtener el ayudante que le toca defender
            alumno_atacante = alumnos[-1] # Debes obtener el alumno que le toca distraer
            while not distraer(alumno_atacante, ayudante_defensor):
                if alumnos:
                    alumnos.pop()
                    break
                # Si no se logró distraer el ayudante con el alumno actual,
                # se debe mandar a la casa al alumno
                # Si quedan alumnos, intentamos con otro alumno,
                # si no, no po
            # O se acabaron los alumnos, o se logró distraer al ayudante
            if not alumnos:
                # Si no quedan alumnos, no podemos distraer ayudantes
                break
            elif ayudante_defensor[2] != None:
                ayudantes_del_piso.popleft()
        if not ayudantes_del_piso:
            # Si no quedan ayudantes, avanzamos de piso
            PISOS.popleft()
        resumen_actual(ayudantes, alumnos)

    if not PISOS:
        print('¡Los alumnos lograron derrotar al Chief!')
    else:
        print('No se logró derrotar al Chief :`(')

    stock = stock_comida(alumnos)
    print('Tras  la batalla, aquí va el catastro de las de las habilidades de los alumnos:')
    print(stock)


if __name__ == '__main__':
    alumnos = cargar_alumnos(os.path.join('bases_datos', 'alumnos.csv'))
    ayudantes = cargar_ayudantes(os.path.join('bases_datos', 'ayudantes.csv'))
    simular_batalla(alumnos, ayudantes)
