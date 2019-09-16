import carrera
import control_datos
import menus
import funciones
import parametros
from sys import exit


def mensaje_principal():
    msj1 = ("Elige una opción para comenzar a participar en" +
            " emocionantes carreras a toda velocidad:\n",
            "Hola bienvenido a InitialP")
    print("--||{:^25}||--\n {:<}".format(msj1[1], msj1[0]))


def mensaje_menu(name):
    print("--|| Bienvenido {:^21} ||--\n¿Qué deseas hacer?\n".format(name))

if __name__ == "__main__":
    juego = carrera.Game()
    menu_s = menus.Menu_sesion(("Nueva partida", "Cargar partida"), "Salir")
    menu_pp = menus.Menu_principal(("Nueva Carrera", "Guardar partida",
                                    "Comprar vehículo"), "Salir")
    menu_dict = {0: menu_s, 1: menu_pp}
    estado = 0
    while True:
        if estado == 0:
            mensaje_principal()
        else:
            mensaje_menu(juego.user.name)
        if menu_dict[estado].selection(juego):
            if estado == 0:
                estado += 1
        else:
            exit(0)
