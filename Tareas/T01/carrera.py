from random import random, randint, uniform
import control_datos
import menus
import funciones
import parametros

racer_parametros = {"Tareos": parametros.EQUIPOS["TAREOS"],
                    "Docencios": parametros.EQUIPOS["DOCENCIOS"],
                    "Hibridos": parametros.EQUIPOS["HIBRIDOS"]}
car_parametros = {"automóvil": parametros.AUTOMOVIL, "bicicleta": parametros.BICICLETA,
                  "troncomóvil": parametros.TRONCOMOVIL, "motocicleta": parametros.MOTOCICLETA}
number_team = {0: "Tareos", 1: "Hibridos", 2: "Docencios"}
number_car = {0: "automóvil", 1: "troncomóvil", 2: "motocicleta", 3: "bicicleta"}


class Racers():
    def __init__(self, name, moneyorlevel, personalidad, cuerpo, balance,
                 exp, equipo):
        if moneyorlevel.isalpha():
            self.level = moneyorlevel
        else:
            self.money = int(moneyorlevel)
        self.experience = int(exp)
        self.name = name
        self.team = equipo
        self.personality = personalidad
        self.body = int(cuerpo)
        self.balance = int(balance)
        self.car = None
        self.time_lap = 0
        self.time_race = 0

    def __repr__(self):
        return self.name


class Cars():
    def __init__(self, name, dueno, tipo, chasis, carroceria, ruedas, aceleracion, peso):
        self.name = name
        self.owner = dueno
        self.type = tipo
        self.chassis = int(chasis)
        self.chassis_damage = 0
        self.body = int(carroceria)
        self.weight = int(peso)
        self.wheels = int(ruedas)
        self.engine = int(aceleracion)
        self.damage = 0

    @property
    def chasis(self):
        return self.chassis - self.chassis_damage

    @chasis.setter
    def chasis(self, x):
        self.chassis = self.chassis * (parametros.MEJORAS["CHASIS"]) * x

    @property
    def carroceria(self):
        return self.body

    @carroceria.setter
    def carroceria(self, x):
        self.body = self.body * (parametros.MEJORAS["CARROCERIA"]) * x

    @property
    def ruedas(self):
        return self.wheels

    @ruedas.setter
    def ruedas(self, x):
        self.wheels = self.wheels * (parametros.MEJORAS["RUEDAS"]) * x

    @property
    def motor(self):
        return self.engine

    @motor.setter
    def motor(self, x):
        if self.type in ("automóvil", "troncomóvil"):
            return self.engine * parametros.MEJORAS["MOTOR"] * x
        else:
            return self.engine * parametros.MEJORAS["ZAPATILLAS"] * x

    def __repr__(self):
        return self.name


class Tracks():
    def __init__(self, name, tipo, hielo, rocas, dificultad, vueltas, rivales, largo):
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


class Race():
    def __init__(self, pista, corredores, user):
        self.track = pista
        self.user_car = user
        self.racers = corredores + [user]
        self.losers = []
        self.laps = 0

    def continue_race(self, game, is_user):
        for index, racer in zip(range(len(self.racers)), self.racers):
            racer.car.chassis_damage = funciones.car_damage(racer.car, self.track)
            if uniform(0, 1) <= funciones.accident(racer.car, racer, self.track, self):
                racer.car.chassis_damage = racer.car.chassis
            racer.time_race += funciones.lap_time(racer.car, racer, self.track, self)
            if racer.car.chasis == 0:
                self.losers.append(self.racers.pop(index))
                if racer.name == game.user.name:
                    while self.laps != self.track.laps:
                        return continue_race(self, game, False)
        self.laps += 1
        if self.laps == self.track.laps:
            return self.end_race(game)
        if is_user:
            self.racers.sort(key=racer_place)
            if game.user.name == self.racers[0].name:
                self.racers[0].money += funciones.money_per_lap(self, self.track)
            print(f"\nVuelta: {self.laps} / {self.track.laps}\nPosiciones de los corredores:")
            if funciones.velocidad_intencional(racer.car, racer, self.track) !=\
               funciones.velocidad_real(racer.car, racer, self.track, self):
                print("Tu velocidad ha sido afectada durante esta vuelta")
            else:
                print("Tu velocidad no ha sido afectada durante esta vuelta")
            print_places(self.racers)
            if self.losers != []:
                print("Competidores descalificados:")
                for racer in self.losers:
                    print(f" - {racer.name}")

    def end_race(self, game):
        self.racers.sort(key=racer_place)
        print_places(self.racers)
        if game.user == self.racers[0]:
            money = funciones.winner_price(self.track)
            exp = funciones.winner_exp(self.racer[0], self.track,
                                       self.racer[len(racer) - 1])
            print("\nFelicidades has sido el ganador de la carrera\n",
                  f"Has consegido ${money} y {exp} puntos de experiencia")
            self.racers[0].money += money
            self.racer[0].exp += exp
        else:
            print("\nNos has sido el ganador, pero has ganado en diversión\n")
        for racer in self.losers:
            racer.time_race = 0
            racer.car.chassis_damage = 0
        for racer in self.racers:
            racer.time_race = 0
            racer.car.chassis_damage = 0
        return True


class Game():
    def __init__(self):
        self.user = None
        self.user_cars = []
        self.users = control_datos.load_racers()
        self.enemies = control_datos.load_enemies()
        self.cars = control_datos.load_cars()
        self.tracks = control_datos.load_tracks()

    def new_game(self):
        name, team, car, carname, isalpha = False, False, False, "", False
        while not name:
            name = check_alpha("Selecciona un nombre de usuario solo con letras y espacios:\n")
            if name:
                is_in = False
                for user in self.users:
                    if name == user.name:
                        is_in = True
                        break
                if is_in:
                    error(6)
                    name = False
        while not team:
            print("Selecciona uno de los siguientes equipos",
                  "disponibles:\n")
            menus.print_options(("Tareos", "Hibridos", "Docencios"))
            team = check_numeric("\n")
            if team:
                if int(team) in (1, 2, 3):
                    self.user = new_racer(name, number_team[int(team) - 1])
                    with open(parametros.PATHS["PILOTOS"], "a", encoding="utf-8") as file:
                        file.write(f"{name},{self.user.money},{self.user.personality}," +
                                   f"{self.user.body},{self.user.balance}," +
                                   f"{self.user.experience},{self.user.team}\n")
                else:
                    error(5)
                    team = False
        while not car:
            print("Selecciona el tipo de tu primer vehículos:\n")
            menus.print_options(("Automovil", "Troncomovil", "Motocicleta", "Bicicleta"))
            car = check_length("\n")
        while not carname:
            carname = check_alpha("Selecciona un nombre para tu vehiculo:\n")
            if carname:
                if carname in self.user_cars:
                    error(6)
                else:
                    self.user_cars.append(new_car(carname, number_car[int(car) - 1], self.user))
                    with open(parametros.PATHS["VEHICULOS"], "a", encoding="utf-8") as file:
                        file.write(f"{carname},{name},{self.user_cars[0].type}," +
                                   f"{self.user_cars[0].chassis},{self.user_cars[0].body}," +
                                   f"{self.user_cars[0].wheels},{self.user_cars[0].motor}" +
                                   f",{self.user_cars[0].weight}\n")
        del self.users

    def save_game(self):
        racers = control_datos.load_racers()
        for index, racer in zip(range(len(racers)), racers):
            if self.user.name == racer.name:
                racers.pop(index)
        control_datos.save_racers(racers + [self.user])
        control_datos.save_cars(self.cars + self.user_cars)

    def load_game(self):
        name = False
        while not name:
            name = check_alpha("Escribe el nombre de usuario que deseas cargar:\n")
            if name:
                is_in = False
                for user in self.users:
                    if name == user.name:
                        is_in = True
                        break
                if not is_in:
                    error(7)
                    name = False
        for usuario in self.users:
            if name == usuario.name:
                self.user = usuario
        del(self.users)
        for index, vehiculo in zip(range(len(self.cars)), self.cars):
            if name == vehiculo.owner:
                self.user_cars.append(self.cars.pop(index))

    def start_race(self):
        menu_rc = menus.Menu_race_configuration()
        menu_r = menus.Menu_race("Ir a los pits", "Continuar la carrera")
        race = menu_rc.selection(self)
        while True:
            if menu_r.selection(self):
                if menu_r.option(self, race):
                    break
            else:
                if race.continue_race(self, True):
                    break

    def buy_car(self):
        menu_b = menus.Menu_buy([("Automóvil", 500), ("Troncomóvil", 900),
                                ("Motocicleta", 370), ("Bicicleta", 1050)],
                                "Volver al menú principal")
        while True:
            if menu_b.selection(self):
                while True:
                    name = check_alpha("Selecciona un nombre para tu vehiculo:\n")
                    if name and name in self.user_cars:
                        error(6)
                    elif name:
                        break
                new_car(name, self.user, number_car[menu_b.option])
                self.user.money -= menu_b.options[menu_b.option][1]
            else:
                break

    def pits(self, race):
        car_part = {"Chasis": self.user.car.chasis, "Carrocería": self.user.car.carroceria,
                    "Ruedas": self.user.car.ruedas, "Zapatillas": self.user.car.motor,
                    "Motor": self.user.car.motor}
        if self.user.car.chassis != self.user.car.carroceria:
            funciones.pits_time(self.user.car)
            self.user.car.chassis_damage = 0
        if self.user.car.type in ("automóvil", "motocicleta"):
            motor = ("Motor", parametros.MEJORAS["MOTOR"]["COSTO"])
        else:
            motor = ("Zapatillas", parametros.MEJORAS["ZAPATILLAS"]["COSTO"])
        menu_pt = menus.Menu_pits((("Chasis", parametros.MEJORAS["CHASIS"]["COSTO"]),
                                   ("Carrocería", parametros.MEJORAS["CARROCERIA"]["COSTO"]),
                                   ("Ruedas", parametros.MEJORAS["RUEDAS"]["COSTO"]),
                                   motor), "Continuar la carrera")
        while True:
            print(f"Dinero del usuario: {self.user.money}")
            if menu_pt.selection(self):
                car_part[menu_pt.option[0]] = 1
                self.user.money -= menu_pt.option[1]
                return race.continue_race(self, True)
            else:
                return race.continue_race(self, True)


def new_car(nombre, tipo, user):
    max_min = car_parametros[tipo]
    chasis = randint(max_min["CHASIS"]["MIN"], max_min["CHASIS"]["MAX"])
    carroceria = randint(max_min["CARROCERIA"]["MIN"], max_min["CARROCERIA"]["MAX"])
    peso = randint(max_min["PESO"]["MIN"], max_min["PESO"]["MAX"])
    ruedas = randint(max_min["RUEDAS"]["MIN"], max_min["RUEDAS"]["MAX"])
    if tipo in ("troncomóvil", "bicicleta"):
        motor = randint(max_min["ZAPATILLAS"]["MIN"], max_min["ZAPATILLAS"]["MAX"])
    else:
        motor = randint(max_min["MOTOR"]["MIN"], max_min["MOTOR"]["MAX"])
    return Cars(nombre, user.name, tipo, chasis, carroceria, ruedas, motor, peso)


def new_racer(name, equipo):
    max_min = racer_parametros[equipo]
    contextura = randint(max_min["CONTEXTURA"]["MIN"], max_min["CONTEXTURA"]["MAX"])
    equilibrio = randint(max_min["EQUILIBRIO"]["MIN"], max_min["EQUILIBRIO"]["MAX"])
    personalidad = max_min["PERSONALIDAD"]
    return Racers(name, "0", personalidad, contextura, equilibrio, 0, equipo)


def select_car(all_cars, enemie):
    cars = []
    for car in all_cars:
        if car.owner == enemie.name:
            cars.append(car)
    if len(cars) != 1:
        selection = randint(0, len(cars) - 1)
    else:
        selection = 0
    return cars[selection]


def print_places(racers):
    print("{:>8s}| {:^20s}| {:>6s}| {:>6s}".format("Posición", "Corredor",
          "Tiempo vuelta", "Tiempo total"))
    for index, racer in zip(range(1, len(racers) + 1), racers):
        print("{:>8d}°| {:^20s}| {:>6d} seg| {:>6d} seg".format(index,
              racer.name, racer.time_lap, racer.time_race))


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
    return command


def check_length(mensaje):
    command = check_numeric(mensaje)
    if command and len(command) != 1:
        error(2)
        return False
    return command


def racer_place(racer):
    return racer.time_race


def error(option):
    option1 = "El valor ingresado no contiene solo espacios y letras"
    option2 = "El valor ingresado no contiene solo numeros"
    option3 = "El nombre elegido ya lo posee otro de tus vehiculos"
    option4 = "El comando posee una longitud erronea"
    option5 = "No posees el dinero necesario para realizar esa compra"
    option6 = "El valor ingresado es mayor o menor a los valores posibles"
    option7 = "Este nombre ya lo posee otro piloto o no es válido"
    option8 = "El nombre ingresado no existe, por favor intente nuevamente"
    options = {0: option1, 1: option2, 2: option3, 3: option4, 4: option5,
               5: option6, 6: option7, 7: option8}
    print(f"\n --Error-- {options[option]}\n")
