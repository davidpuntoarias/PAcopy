from abc import ABC, abstractmethod
from random import random, randint as random, randint
from math import ceil as ceil
from os import path
import parametros
import funciones
import sys.exit
number_team = {0: "Tareos", 1: "Hibridos", 2: "Docencios"}
number_car = {0: "automóvil", 1: "troncomóvil", 2: "motocicleta", 3: "bicicleta"}
car_parametros = {"automóvil": parametros.AUTOMOVIL, "bicicleta": parametros.BICICLETA,
                  "troncomóvil": parametros.TRONCOMOVIL, "motocicleta": parametros.MOTOCICLETA}
racer_parametros = {"Tareos": parametros.EQUIPOS["TAREOS"],
                    "Docencios": parametros.EQUIPOS["DOCENCIOS"],
                    "Hibridos": parametros.EQUIPOS["HIBRIDOS"]}


class Menu(ABC):
    def __init__(self, opciones, salir, funciones):
        self.options = opciones
        self.option = None
        self.dict = dict(zip(range(1, len(opciones) + 1), opciones))

    def print(self):
        print_options(self.options)
        print(f"\n[0] {self.salir}")

    def selection(self):
        command = " "
        while not command.isnumeric() and len(command) == 1:
            self.print()
            command = input("\n")
            if not command.isnumeric():
                error(1)
            elif len(command) > 1:
                error(2)
        if int(command) in self.dict.keys():
            self.option = self.dict(int(command))
            return True
        else:
            return False


class Menu_sesion(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones, (juego.new_game, juego.load_game))


class Menu_principal(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones, (juego.start_race, juego.save_game, juego.buy_car))


class Menu_buy():
    def __init__(self, options):
        super().__init__(*opciones, ("automóvil", "troncomóvil",
                         "motocicleta", "bicicleta"))

    def print(self):
        for index, option in zip(range(1, len(self.options + 1)), self.options):
            print(f"[{index}] {option[0]}    -${option[1]}-")
        print(f"\n[0] {self.salir}")

    def selection(self):
        command, cost = " ", 0
        while not (command.isnumeric() and juego.money >= self.options[int(comand)][1]):
            print("Vehículos disponibles para comprar:")
            self.print()
            command = input("\n")
            if not command.isnumeric():
                error(1)
            elif len(command) > 1:
                error(2)
            elif int(command) < self.options[int(command)][1]:
                error(4)
                comand = " "
        if command in self.dict.keys():
            self.option = (self.dict[int(command)], self.options[int(command)][1])
            return True
        else:
            return False


class Menu_pits(Menu):
    def __init__(self, options):
        super().__init__(options)


class Menu_race_configuration(Menu):
    def __init__(self):
        pass

    def selection(self):
        while True:
            print("Elige la pista en la que deseas competir:")
            print_options(juego.tracks)
            pista = check_numeric()
            if pista and 0 < pista < len(juego.tracks) + 1:
                juego.actual_track = juego.tracks[pista - 1]
                break
            else:
                error(5)
        while True:
            print("Elige el vehículo con el que deseas competir:")
            print_options(juego.user_cars)
            vehiculo = check_numeric()
            if pista and 0 < pista < len(juego.tracks) + 1:
                juego.actual_car = juego.user_cars[pista - 1]
                break
            else:
                error(5)


class Menu_race(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones, (juego.continue_race))


class Racers():
    def __init__(self, name, money, personalidad, cuerpo, balance,
                 exp, equipo):
        self.experience = int(exp)
        self.name = name
        self.money = int(money)
        self.team = equipo
        self.personality = personalidad
        self.body = int(cuerpo)
        self.balance = int(balance)

    def __repr__(self):
        return self.name


class Cars():
    def __init__(self, name, dueno, tipo, chasis, carroceria, ruedas, aceleracion, peso):
        self.name = name
        self.owner = dueno
        self.type = tipo
        self.chassis = int(chasis)
        self.chassis_buff = 0
        self.body = int(carroceria)
        self.body_buff = 0
        self.weight = int(peso)
        self.weight_buff = 0
        self.wheels = int(ruedas)
        self.wheels_buff = 0
        self.engine = int(aceleracion)
        self.engine_buff = 0
        self.damage = 0

    @property
    def chasis(self):
        return self.chassis + self.chassis_buff * parametros.MEJORAS["CHASIS"]

    @chasis.setter
    def chasis(self, x):
        self.chassis_buff += x

    @property
    def carroceria(self):
        return self.body + self.body_buff * parametros.MEJORAS["CARROSERIA"]

    @carroceria.setter
    def carroceria(self, x):
        self.body_buff += x

    @property
    def peso(self):
        return self.weight + self.weight_buff * parametros.MEJORAS["PESO"]

    @peso.setter
    def peso(self, x):
        self.weight_buff += x

    @property
    def ruedas(self):
        return self.wheels + self.wheels_buff * parametros.MEJORAS["RUEDAS"]

    @ruedas.setter
    def ruedas(self, x):
        self.wheels_buff += x

    @property
    def motor(self):
        if self.type in ("automóvil", "troncomóvil"):
            return self.engine + self.engine_buff * parametros.MEJORAS["MOTOR"]
        else:
            return self.engine + self.engine_buff * parametros.MEJORAS["ZAPATILLAS"]

    @motor.setter
    def motor(self, x):
        self.motor_buff += x

    def __repr__(self):
        return self.name


class Tracks():
    def __init__(self, name, tipo, hielo, rocas, dificultad, rivales, vueltas, largo):
        self.name = name
        self.type = tipo
        self.ice = int(hielo)
        self.rocks = int(rocas)
        self.level = int(dificultad)
        self.enemies = rivales
        self.laps = int(vueltas)
        self.length = int(largo)

    def __repr__(self):
        return self.name


class Game():
    def __init__(self):
        self.user = None
        self.actual_car = None
        self.actual_track = None
        self.user_cars = []
        self.money = 0
        self.users = funciones.load_pilotos()
        self.enemies = funciones.load_enemies()
        self.cars = funciones.load_cars()
        self.tracks = funciones.load_tracks()
        self.lap = 0

    def new_game(self):
        del self.pilotos
        name, team, car, carname, isalpha = "", "", False, "", False
        while True:
            name = check_alpha("Selecciona un nombre de usuario:\n")
            if name:
                if name in self.pilotos:
                    error(6)
                else:
                    break
        while True:
            print("Selecciona uno de los siguientes equipos",
                  "disponibles:\n")
            print_options(("Tareos", "Hibridos", "Docencios"))
            team = check_numeric(input())
            if team:
                if int(team) in (1, 2, 3):
                    self.user = funciones.new_racer(name, number_team[int(team)])
                    with open(parametros.PATHS["PILOTOS"], "a", encoding="utf-8") as file:
                        file.write(f"{name},{self.user.money},{self.user.personality}," +
                                   f"{self.user.body},{self.user.balance},{self.user.exp}" +
                                   f",{self.user.team}")
                    break
                else:
                    error(5)
        while True:
            print("Selecciona el tipo de tu primer vehículos:\n")
            print_options(("Automovil", "Troncomovil", "Motocicleta", "Bicicleta"))
            if car is False:
                while car:
                    car = check_numeric()
            carname = check_alpha("Selecciona un nombre para tu vehiculo:\n")
            if carname and carname not in self.user_cars:
                self.user_cars.append(funciones.new_car(carname, number_car[car]))
                with open(path_cars, "a", encoding="utf-8") as file:
                    file.write(f"{carname},{name},{self.actual_car.type}," +
                               f"{self.actual_car.chassis},{self.actual_car.body}," +
                               f"{self.actual_car.wheels}, {self.actual_car.motor}" +
                               f",{self.actual_car.shoes},{self.actual_car.weight}")
                break
            elif carname in self.user_cars:
                error(6)

    def save_game(self):
        pass

    def load_game(self):
        pass

    def start_race(self):
        menu_rc.selection()
        while True:
            menu_r.selection()

    def buy_car(self):
        while True:
            if menu_b.selection():
                while True:
                    name = check_alpha()
                    if name in self.user_cars:
                        error(6)
                    elif name:
                        break
                funciones.new_car(name, menu_b.option[0])
                self.money -= menu_b.option[1]
            else:
                break

    def continue_race(self):
        pass


def print_options(options):
    for index, option in zip(range(1, len(options + 1)), options):
            print(f"[{index}] {option[0]}\n")


def check_alpha(mensaje):
    command = input(mensaje).strip(" ")
    if not "".join(filter(lambda character: character != " ", command)).isalpha():
        error(0)
        return False
    else:
        return command


def check_numeric(mensaje):
    command = input(mensaje).strip(" ")
    if not "".join(filter(lambda character: character != " ", command)).isnumeric():
        error(1)
        return False
    else:
        return command


def error(option):
    option1 = "El valor ingresado no contiene solo espacios y letras"
    option2 = "El valor ingresado no contiene solo numeros"
    option3 = "El nombre elegido ya lo posee otro de tus vehiculos"
    option4 = "El comando posee una longitud erronea"
    option5 = "No posees el dinero necesario para realizar esa compra"
    option6 = "El valor ingresado es mayor o menor a los valores posibles"
    option7 = "Este nombre ya lo posee otro piloto"
    options = {0: option1, 1: option2, 2: option3, 3: option4, 4: option5,
               5: option6, 6: option7}
    print(f"\n --Error-- {options[option]}\n")


if __name__ == "__main__":
    juego = Game()
    menu_s = Menu_sesion(("Nueva partida", "Cargar partida"), "Salir")
    menu_pp = Menu_principal(("Nueva Carrera", "Guardar partida", "Comprar vehículo"), "Salir")
    menu_b = Menu_buy(("Automóvil", 500), ("Troncomóvil", 900),
                      ("Motocicleta", 370), ("Bicicleta", 1050), "Volver al menú principal")
    menu_r = Menu_race("Ir a los pits", "Continuar la carrera")
    menu_rs = Menu_race_configuration()
    menu_dict = {0: menu_s, 1: menu_pp}
    estado = 0
    while True:
        if menu_dict[estado].selection():
            menu_dict[estado].option()
            if estado == 0:
                estado += 1
        else:
            sys.exit(0)
