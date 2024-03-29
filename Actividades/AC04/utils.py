from time import sleep
from threading import Event, Lock


def reloj(minutos):
    """
    Simulación: 1 hora virtual equivale a 1 segundo real
    :param minutos: tiempo en segundos virtuales
    """
    # print(f"{minutos} SLEEP")
    sleep(minutos / 60)


class Tunel:

    def __init__(self):
        self.metros_avanzados = 0
        self.largo = 6000
        self.tunel_listo = Event()
        self.usar_tunel = Lock()


class BolsaDinero:

    def __init__(self):
        self.dinero_acumulado = 0
        self.meta_dinero = 10000000
        self.usar_bolsa = Lock()
        self.dinero_listo = Event()
