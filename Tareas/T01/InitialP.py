from abc import ABC, abstractmethod
from random import random, randint as random, randint
import parametros
tipo_a_parametro = {"Automovil": parametros.AUTOMOVIL, "Bicicleta": parametros.BICICLETA,
                    "Troncomovil": parametros.TRONCOMOVIL, "Motocicleta": parametros.MOTOCICLETA}


class Menu(ABC):
    def __init__(self, opciones):
        self.options = opciones

    def print(self):
        for index, option in enumerate(self.options):
            print(f"[{index}] {option}")


class Menu_sesion(Menu):
    def __init__(self, options):
        super().__init__()

    def new_game():
        new_game()

    def load_game():
        load_game()



class Menu_principal(Menu):
    def __init__(self, options):
        super().__init__()

    def start_game():
        start_game()

    def save_game():
        save_game()

    def buy_car():
        pass

    def exit():
        pass


class Menu_buy():
    def __init__(self, options):
        super().__init__()

    def back():
        pass

    def print():
        for index, option in enumerate(self.options):
            print(f"[{index}] {option}")


class Menu_pits(Menu):
    def __init__(self, options):
        super().__init__()

    def buy():
        pass

    def print():
        for index, option in enumerate(self.options):
            print(f"[{index}] {option}")


class Menu_carrera(Menu):
    def __init__(self, options):
        super().__init__()


class Racers():
    def __init__(self, npc, cuerpo, balance, personalidad, equipo):
        if not npc:
            self.experience = 0
        self.team = equipo
        self.personality = personalidad
        self.body = cuerpo
        self.balance = balance


class Cars():
    def __init__(self, tipo, chasis, carroceria, peso, ruedas, zapatillas, motor):
        self.type = tipo
        self.dict = tipo_a_parametro[self.type]
        self.chassis = chasis
        self.body = carroceria
        self.weight = peso
        self.wheels = ruedas
        self.shoes = zapatillas
        self.motor = motor

    def __str__(self):
        return(f"Chasis: {self.chassis}\nCarroceria: {self.body}\nPeso: {self.weight}" +
               f"\nRuedas: {self.wheels}\nZapatillas: {self.shoes}\nMotor: {self.motor}")


class Game():
    def __init__(self, usuario, vehiculo_actual, corredores):
        self.user = usuario
        self.actual_car = vehiculo_actual
        self.dinero = 0
        self.racers = corredores

    def save_game(self):
        pass

    def start_game(self):
        pass


def new_car(tipo):
    max_min = tipo_a_parametro[tipo]
    chasis = randint(max_min["CHASIS"]["MIN"], max_min["CHASIS"]["MAX"])
    carroceria = randint(max_min["CARROCERIA"]["MIN"], max_min["CARROCERIA"]["MAX"])
    peso = randint(max_min["PESO"]["MIN"], max_min["PESO"]["MAX"])
    ruedas = randint(max_min["RUEDAS"]["MIN"], max_min["RUEDAS"]["MAX"])
    zapatillas = randint(max_min["ZAPATILLAS"]["MIN"], max_min["ZAPATILLAS"]["MAX"])
    motor = randint(max_min["MOTOR"]["MIN"], max_min["MOTOR"]["MAX"])
    return Cars(tipo, *(chasis, carroceria, peso, ruedas, zapatillas, motor))


def new_game():
    pass


def start_game():
    pass


def load_game():
    pass


def print_options(options):
    for index, option in zip(range(len(options)), options):
        print(f"[{index}] {option}")


def new_game():
    name = input("Selecciona un nombre de usuario:\n")
    if "".join(filter(lambda character: character != " ", name)).isalpha():
        print("Selecciona uno de los siguientes equipos disponibles:\n")
        print_options(("Tareos", "Hibridos", "Docencios"))
        comand = input()
        if comand.isnumeric():
            Game(Racers(False, comand,)


tocomocho = new_car("Automovil")
print(tocomocho)
