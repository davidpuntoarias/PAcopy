from abc import ABC
import control_datos
import carrera
import parametros


class Menu(ABC):
    def __init__(self, opciones, salir):
        self.option = None
        self.options = opciones
        self.exit = salir

    def print(self):
        print_options(self.options)
        print(f"\n[0] {self.exit}")

    def selection(self, game):
        command = False
        while not command:
            self.print()
            command = carrera.check_length("\n")
        if int(command) != 0:
            self.dict[int(command) - 1](game)
            return True
        else:
            return False


class Menu_sesion(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones)
        self.dict = {0: self.new_game, 1: self.load_game}

    def new_game(self, game):
        game.new_game()

    def load_game(self, game):
        game.load_game()


class Menu_principal(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones)
        self.dict = {0: self.start_race, 1: self.save_game, 2: self.buy_car}

    def start_race(self, game):
        game.start_race()

    def save_game(self, game):
        game.save_game()

    def buy_car(self, game):
        game.buy_car()


class Menu_buy(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones)

    def print(self):
        for index, option in zip(range(1, len(self.options) + 1), self.options):
            print(f"[{index}] {option[0]}    -${option[1]}-")
        print(f"\n[0] {self.exit}\n")
        print("Ingresa el numero del vehículo que deseas comprar o 0 para volver al menú:")

    def selection(self, game):
        command = False
        while not command:
            print(f"Dinero usuario: {game.user.money}\nVehículos disponibles para comprar:")
            self.print()
            command = carrera.check_length("\n")
            if command and command != "0" and game.user.money < self.options[int(command) - 1][1]:
                carrera.error(4)
                command = False
        if command != "0":
            self.option = int(command) - 1
            return True
        else:
            return False


class Menu_pits(Menu):
    def __init__(self, options, salir):
        super().__init__(options, salir)

    def print(self):
        for index, piece in zip(range(1, len(self.options) + 1), self.options):
            print("[{:d}] {:^10s} | ${:^5d}".format(index, piece[0], piece[1]))

    def selection(self, game):
        command, cost = False, 0
        while not command:
            print("Partes disponibles para mejorar:")
            self.print()
            command = carrera.check_length("\nIngresa el numero de la parte a mejorar" +
                                           " o 0 para continuar la carrera:\n")
            if command and command != "0" and game.user.money < self.options[int(command) - 1][1]:
                carrera.error(4)
                command = False
        if command != "0":
            self.option = (self.options[int(command) - 1])
            return True
        else:
            return False


class Menu_race_configuration(Menu):
    def __init__(self):
        pass

    def selection(self, game):
        while True:
            print("Elige la pista en la que deseas competir:")
            print_options(game.tracks)
            pista = carrera.check_numeric("\n")
            if pista and 0 <= int(pista) - 1 < len(game.tracks):
                pista = game.tracks[int(pista) - 1]
                break
            else:
                carrera.error(5)
        while True:
            print("Elige el vehículo con el que deseas competir:")
            print_options(game.user_cars)
            vehiculo = carrera.check_numeric("\n")
            if vehiculo and 0 <= int(vehiculo) - 1 < len(game.user_cars):
                game.user.car = game.user_cars[int(vehiculo) - 1]
                break
            else:
                carrera.error(5)
        enemigos = []
        for enemie in game.enemies:
            if enemie.name in pista.enemies:
                enemie.car = carrera.select_car(game.cars, enemie)
                enemigos.append(enemie)
        while len(enemigos) > parametros.NUMERO_CONTRINCANTES:
            enemigos.pop(randint(0, len(enemigos)))
        return carrera.Race(pista, enemigos, game.user)


class Menu_race(Menu):
    def __init__(self, *opciones):
        super().__init__(*opciones)
        self.dict = {0: self.pits}

    def pits(self, game, race):
        return game.pits(race)

    def print(self):
        print(f"[1] {self.options}\n")
        print(f"\n[0] {self.exit}")

    def selection(self, game):
        command = False
        while not command:
            self.print()
            command = carrera.check_length("\n")
        if int(command) != 0:
            self.option = self.dict[int(command) - 1]
            return True
        else:
            return False


def print_options(options):
    for index, option in zip(range(1, len(options) + 1), options):
        print(f"[{index}] {option}\n")
