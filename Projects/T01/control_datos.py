import carrera
import parametros


def load_enemies():
    with open(parametros.PATHS["CONTRINCANTES"], "r", encoding="utf-8") as file:
        racers = file.readlines()
    list_racers = []
    for line in racers[1:]:
        racer = line[:-1].split(",")
        list_racers.append(carrera.Racers(racer[0], racer[1], racer[2], racer[3],
                                          racer[4], racer[5], racer[6]))
    return list_racers


def load_cars():
    with open(parametros.PATHS["VEHICULOS"], "r", encoding="utf-8") as file:
        racers = file.readlines()
    list_cars = []
    for line in racers[1:]:
        car = line[:-1].split(",")
        list_cars.append(carrera.Cars(car[0], car[1], car[2], car[3],
                                      car[4], car[5], car[6], car[7]))
    return list_cars


def save_cars(cars):
    with open(parametros.PATHS["VEHICULOS"], "w", encoding="utf-8") as file:
        file.write("Nombre,Dueño,Categoría,Chasis,Carrocería,Ruedas,Motor o Zapatillas,Peso\n")
        for car in cars:
            file.write(f"{car.name},{car.owner},{car.type},{car.chassis},{car.body}" +
                       f",{car.wheels},{car.motor},{car.weight}\n")


def load_tracks():
    with open(parametros.PATHS["PISTAS"], "r", encoding="utf-8") as file:
        tracks = file.readlines()
    list_tracks = []
    for line in tracks[1:]:
        track = line[:-1].split(",")
        list_tracks.append(carrera.Tracks(track[0], track[1], track[2], track[3], track[4],
                                          track[5], track[6].split(";"), track[7]))
    return list_tracks


def load_racers():
    with open(parametros.PATHS["PILOTOS"], "r", encoding="utf-8") as file:
        racers = file.readlines()
    list_racers = []
    for line in racers[1:]:
        racer = line[:-1].split(",")
        list_racers.append(carrera.Racers(racer[0], racer[1], racer[2], racer[3],
                                          racer[4], racer[5], racer[6]))
    return list_racers


def save_racers(racers):
    with open(parametros.PATHS["PILOTOS"], "w", encoding="utf-8") as file:
        file.write("Nombre,Dinero,Personalidad,Contextura,Equilibrio,Experiencia,Equipo\n")
        for racer in racers:
            file.write(f"{racer.name},{racer.money},{racer.personality},{racer.body}" +
                       f",{racer.balance},{racer.experience},{racer.team}\n")
