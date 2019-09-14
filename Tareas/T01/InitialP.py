import carrera
import control_datos
import menus
import funciones
import parametros
from sys import exit

if __name__ == "__main__":
    juego = carrera.Game()
    menu_s = menus.Menu_sesion(("Nueva partida", "Cargar partida"), "Salir")
    menu_pp = menus.Menu_principal(("Nueva Carrera", "Guardar partida",
                                    "Comprar vehículo"), "Salir")
    menu_dict = {0: menu_s, 1: menu_pp}
    estado = 0
    while True:
        if menu_dict[estado].selection(juego):
            if estado == 0:
                estado += 1
        else:
            exit(0)
