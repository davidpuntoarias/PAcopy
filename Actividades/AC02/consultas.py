"""
Aquí debes completar las funciones de las consultas
"""


def resumen_actual(ayudantes, alumnos):
    ayudantes1 = len(ayudantes["Nuevo"])
    ayudantes2 = len(ayudantes["Jefe"])
    ayudantes3 = len(ayudantes["Mentor"])
    ayudantes4 = len(ayudantes["Chief Tamburini"])
    nayudantes = ayudantes1 + ayudantes2 + ayudantes3 + ayudantes4
    print("--- ---")
    print(f" Alumnos restantes: {len(alumnos)}\nAyudantes restates: " +
          f"{nayudantes}\nAyudantes Piso -1: {ayudantes1}\nAyudantes " +
          f"Piso -2: {ayudantes2}\nAyudantes Piso -3: {ayudantes3}\n" +
          f"Ayudantes Piso -4: {ayudantes4}\n --- ---")


def stock_comida(alumnos):
    comidas = set()
    ncomidas = []
    for alumno in alumnos:
        comidas = comidas | alumno[1]
    comidas = list(comidas)
    for comida in range(len(comidas)):
        cantidad = 0
        for alumno in alumnos:
            if comidas[comida] in alumno[1]:
                cantidad += 1
        comidas[comida] = (comidas[comida], cantidad)
    return comidas
