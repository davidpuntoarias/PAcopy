from abc import ABC, abstractmethod
from random import random, randint as random, randint
from os import path
import parametros
number_team = {0: "Tareos", 1: "Hibridos", 2: "Docencios"}
number_car = {0: "Automovil", 1: "Troncomovil", 2: "Motocicleta", 3: "Bicicleta"}
car_parametros = {"Automovil": parametros.AUTOMOVIL, "Bicicleta": parametros.BICICLETA,
                  "Troncomovil": parametros.TRONCOMOVIL, "Motocicleta": parametros.MOTOCICLETA}
racer_parametros = {"Tareos": parametros.EQUIPOS["TAREOS"],
                    "Docencios": parametros.EQUIPOS["DOCENCIOS"],
                    "Hibridos": parametros.EQUIPOS["HIBRIDOS"]}
path_racers = parametros.PATHS["CONTRINCANTES"]
path_cars = parametros.PATHS["VEHICULOS"]


class Menu(ABC):
    def __init__(self, opciones, salir, funciones):
        self.options = opciones
        self.dict = dict(zip(range(1, len(opciones) + 1), opciones))

    def print(self):
        for index, option in zip(range(1, len(self.options + 1)), self.options):
            print(f"[{index}] {option}")
        print(f"[0] {self.salir}")

    def selection(self):
        self.print()
        comand = None
        while not comand.isnumeric() and len(comand) > 1:
            command = input("\n")
            if not comand.isnumeric():
                error(1)
            elif len(comand) > 1:
                error(2)
        if int(comand) in self.dict.keys():
            self.dict(int(comand))()
        else:
            exit()


class Menu_sesion(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones, (juego.new_game, juego.load_game))


class Menu_principal(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones, (juego.start_race, juego.save_game, juego.buy_car))


class Menu_buy():
    def __init__(self, options):
        super().__init__(options)


class Menu_pits(Menu):
    def __init__(self, options):
        super().__init__(options)


class Menu_carrera(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones, (juego.continue_race))


class Racers():
    def __init__(self, name, money, personalidad, cuerpo, balance,
                 exp, equipo):
        self.experience = exp
        self.name = name
        self.money = money
        self.team = equipo
        self.personality = personalidad
        self.body = cuerpo
        self.balance = balance

    def __repr__(self):
        return self.name


class Cars():
    def __init__(self, name, dueno, tipo, chasis, carroceria, ruedas, aceleracion, peso):
        self.name = name
        self.owner = dueno
        self.type = tipo
        self.chassis = chasis
        self.body = carroceria
        self.weight = peso
        self.wheels = ruedas
        self.motor = aceleracion

    def __repr__(self):
        return self.name


class Game():
    def __init__(self):
        self.user = None
        self.actual_car = None
        self.user_cars = []
        self.dinero = 0
        self.racers = load_racers()
        self.cars = load_cars()

    def new_game(self):
        name, team, car, carname = None, None, None, None
        while not "".join(filter(lambda character: character != " ", name)).isalpha():
            name = input("Selecciona un nombre de usuario:\n")
            if not "".join(filter(lambda character: character != " ", name)).isalpha():
                error(0)
        while not team.isnumeric():
            print("Selecciona uno de los siguientes equipos",
                  "disponibles:\n")
            print_options(("Tareos", "Hibridos", "Docencios"))
            team = input()
            if team.isnumeric():
                self.user = new_racer(name, number_team[int(team)])
                with open(path_racers, "a", encoding="utf-8") as file:
                    file.write(f"{name},{self.user.money},{self.user.personality}," +
                               f"{self.user.body},{self.user.balance},{self.user.exp}" +
                               f",{self.user.team}")
            else:
                error(1)
        while not "".join(filter(lambda character: character != " ", carname)).isalpha():
            print("Selecciona el tipo de tu primer vehículos:\n")
            print_options(("Automovil", "Troncomovil", "Motocicleta", "Bicicleta"))
            if car is None:
                while not "".join(filter(lambda character: character != " ", car)).isalpha():
                    car = input()()
                    if not "".join(filter(lambda character: character != " ", car)).isalpha():
                        error(1)
            carname = input("Selecciona un nombre para tu vehiculo:\n")
            if "".join(filter(lambda character: character != " ", carname)).isalpha() \
               and carname not in self.user_cars:
                self.user_cars.append(self.actual_car)
                with open(path_cars, "a", encoding="utf-8") as file:
                    file.write(f"{carname},{name},{self.actual_car.type}," +
                               f"{self.actual_car.chassis},{self.actual_car.body}," +
                               f"{self.actual_car.wheels}, {self.actual_car.motor}" +
                               f",{self.actual_car.shoes},{self.actual_car.weight}")
            else:
                error(0)

    def save_game(self):
        pass

    def load_game(self):
        pass

    def start_race(self):
        pass

    def buy_car(self):
        pass

    def continue_race(self):
        pass


def new_car(nombre, tipo):
    max_min = car_parametros[tipo]
    chasis = randint(max_min["CHASIS"]["MIN"], max_min["CHASIS"]["MAX"])
    carroceria = randint(max_min["CARROCERIA"]["MIN"], max_min["CARROCERIA"]["MAX"])
    peso = randint(max_min["PESO"]["MIN"], max_min["PESO"]["MAX"])
    ruedas = randint(max_min["RUEDAS"]["MIN"], max_min["RUEDAS"]["MAX"])
    zapatillas = randint(max_min["ZAPATILLAS"]["MIN"], max_min["ZAPATILLAS"]["MAX"])
    motor = randint(max_min["MOTOR"]["MIN"], max_min["MOTOR"]["MAX"])
    return Cars(nombre, tipo, chasis, carroceria, peso, ruedas, zapatillas, motor)


def new_racer(name, equipo):
    max_min = racer_parametros[equipo]
    contextura = randint(max_min["CONTEXTURA"]["MIN"], max_min["CONTEXTURA"]["MAX"])
    equilibrio = randint(max_min["EQUILIBRIO"]["MIN"], max_min["EQUILIBRIO"]["MAX"])
    personalidad = max_min["PERSONALIDAD"]
    return Racers(name, 0, contextura, equilibrio, personalidad, 0, equipo)


def load_racers():
    with open(path_racers, "r", encoding="utf-8") as file:
        racers = file.readlines()
    list_racers = []
    for line in racers[1:]:
        racer = line[:-1].split(",")
        list_racers.append(Racers(racer[0], racer[1], racer[2], racer[3],
                                  racer[4], racer[5], racer[6]))
    return list_racers


def load_cars():
    with open(path_cars, "r", encoding="utf-8") as file:
        racers = file.readlines()
    list_cars = []
    for line in racers[1:]:
        racer = line[:-1].split(",")
        list_cars.append(Racers(racer[0], racer[1], racer[2], racer[3],
                         racer[4], racer[5], racer[6]))
    return list_cars


def print_options(options):
    for index, option in zip(range(len(options)), options):
        print(f"[{index}] {option}\n")


def error(option):
    option1 = "El valor ingresado no contiene solo espacios y letras"
    option2 = "El valor ingresado no contiene solo numeros"
    option3 = "El nombre elegido ya lo posee otro de tus vehiculos"
    option4 = "El comando posee una longitud erronea"
    options = {0: option1, 1: option2, 2: option3, 3: option4}
    print(f"\n --Error-- {options[option]}\n")

juego = Game()
menu_s = Menu_sesion(("Nueva partida", "Cargar partida") ,"Salir")
menu_pp = Menu_principal(("Nueva Carrera", "Guardar partida", "Comprar vehículo"), "Salir")
menu_c = Menu_carrera("Ir a los pits", "Continuar la carrera")
#menu_pt = Menu_pits(())
if __name__ == "__main__":
    tocomocho = new_car("test", "Automovil")
    print(tocomocho)
    print(tocomocho.motor)
