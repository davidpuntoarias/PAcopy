def velocidad_real(car, racer, track):
    max(parametros.VELOCIDAD_MINIMA, velocidad_intencional(car, racer, track) +
        hipotermia(racer, track) + dificultad_control(car, racer))


def dificultad_control(car, racer):
    if car.type in ("Troncomovil", "Automovil"):
        return 0
    else:
        if racer.personality == "precavido":
            balance_multiplier = parametros.EQUILIBRIO_PRECAVIDO
        else:
            balance_multiplier = 1
        return min(0, racer.balance * balance_multiplier -
                   (parametros.PESO_MEDIO/car.weigth)//1)


def velocidad_intencional(car, racer, track):
    if racer.personality == "precavido":
        speed_multiplier = parametros.EFECTO_PRECAVIDO
    else:
        speed_multiplier = parametros.EFECTO_OSADO
    return velocidad_multiplier * velocidad_recomendada(racer, car, track)


def velocidad_recomendada(car, racer, track):
    return car.motor + (car.ruedas - track.ice) * parametros.POND_EFECT_HIELO +\
           (car.chasis - track.rocks) * parametros.POND_EFECT_ROCAS +\
           (racer.exp - track.level) * parametros.POND_EFECT_DIFICULTAD


def hipotermia(racer, track):
    return min(0, juego.lap * (racer.body - track.ice))


def car_damage(car, track):
    return max(0, track.rocks - car.carroseria)


def pits_time(car):
    return parametros.TIEMPO_MINIMO_PITS + (car.damage) * parametros.VELOCIDAD_PITS


def money_per_lap(track):
    return juego.lap * track.level


def lap_time(car, racer, track):
    return ceil(track.lenght/velocidad_real(car, racer, track))


def accident(car, racer, track):
    speed_recommended = velocidad_recomendada(car, racer, track)
    speed_real = velocidad_real(car, racer, track)
    return min(1, max(0, (speed_real - speed_recommended)/speed_recommended) +
               (car.damage/car.chasis)//1)


def winer_price(track):
    return juego.laps * (track.level + track.ice - track.rocks)


def winer_exp(racer, track, last_racer):
    if racer.personality == "precavido":
        exp_multiplier = parametros.BONIFICACION_PRECAVIDO
    else:
        exp_multiplier = parametros.BONIFICACION_OSADO
    return (track.level + advantage_last_place(racer, last_racer)) * exp_multiplier


def advantage_last_place(racer, last_place):
    return racer.time - last_place.time


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


def load_enemies():
    with open(parametros.PATHS["CONTRINCANTES"], "r", encoding="utf-8") as file:
        racers = file.readlines()
    list_enemies = []
    for line in racers[1:]:
        racer = line[:-1].split(",")
        list_racers.append(Racers(racer[0], racer[1], racer[2], racer[3],
                                  racer[4], racer[5], racer[6]))
    return list_enemies


def load_cars():
    with open(parametros.PATHS["VEHICULOS"], "r", encoding="utf-8") as file:
        racers = file.readlines()
    list_cars = []
    for line in racers[1:]:
        racer = line[:-1].split(",")
        list_cars.append(Cars(racer[0], racer[1], racer[2], racer[3],
                         racer[4], racer[5], racer[6]))
    return list_cars


def load_tracks():
    with open(parametros.PATHS["PISTAS"], "r", encoding="utf-8") as file:
        tracks = file.readlines()
    list_tracks = []
    for line in tracks[1:]:
        track = line[:-1].split(",")
        list_tracks.append(Tracks(tracks[0], track[1], track[2], track[3], track[4],
                           track[5].split(";"), track[6], track[7]))


def load_racers():
    with open(parametros.PATHS["PILOTOS"], "r", encoding="utf-8") as file:
        racers = file.readlines()
    list_racers = []
    for line in racers[1:]:
        racer = line[:-1].split(",")
        list_racers.append(Racers(racer[0], racer[1], racer[2], racer[3],
                                  racer[4], racer[5], racer[6]))
    return list_racers
