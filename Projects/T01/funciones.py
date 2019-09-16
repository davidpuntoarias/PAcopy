from math import ceil
import parametros


def velocidad_real(car, racer, track, race):
    return max(parametros.VELOCIDAD_MINIMA, velocidad_intencional(car, racer, track) +
               hipotermia(race, racer, track) + dificultad_control(car, racer))


def dificultad_control(car, racer):
    if car.type in ("Troncomovil", "Automovil"):
        return 0
    else:
        if racer.personality == "precavido":
            balance_multiplier = parametros.EQUILIBRIO_PRECAVIDO
        else:
            balance_multiplier = 1
        return min(0, racer.balance * balance_multiplier -
                   (parametros.PESO_MEDIO/car.weight)//1)


def velocidad_intencional(car, racer, track):
    if racer.personality == "precavido":
        speed_multiplier = parametros.EFECTO_PRECAVIDO
    else:
        speed_multiplier = parametros.EFECTO_OSADO
    return speed_multiplier * velocidad_recomendada(car, racer, track)


def velocidad_recomendada(car, racer, track):
    return (car.motor + (car.ruedas - track.ice) * parametros.POND_EFECT_HIELO +
            (car.chasis - track.rocks) * parametros.POND_EFECT_ROCAS +
            (racer.experience - track.level) * parametros.POND_EFECT_DIFICULTAD)


def hipotermia(race, racer, track):
    return min(0, race.laps * (racer.body - track.ice))


def car_damage(car, track):
    return max(0, track.rocks - car.carroceria)


def pits_time(car):
    return parametros.TIEMPO_MINIMO_PITS + (car.chassis_damage) * parametros.VELOCIDAD_PITS


def money_per_lap(race, track):
    return race.laps * track.level


def lap_time(car, racer, track, race):
    return ceil(track.length/velocidad_real(car, racer, track, race))


def accident(car, racer, track, race):
    speed_recommended = velocidad_recomendada(car, racer, track)
    speed_real = velocidad_real(car, racer, track, race)
    return min(1, max(0, (speed_real - speed_recommended)/speed_recommended) +
               ((car.chassis_damage)/car.chassis)//1)


def winner_price(track):
    return track.laps * (track.level + track.ice + track.rocks)


def winner_exp(racer, track, last_racer):
    if racer.personality == "precavido":
        exp_multiplier = parametros.BONIFICACION_PRECAVIDO
    else:
        exp_multiplier = parametros.BONIFICACION_OSADO
    return (track.level + advantage_last_place(racer, last_racer)) * exp_multiplier


def advantage_last_place(racer, last_place):
    return last_place.time_race - racer.time_race
