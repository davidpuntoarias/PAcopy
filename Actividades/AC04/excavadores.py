from threading import Thread, Lock
from utils import reloj
import random


class Excavador(Thread):

    def __init__(self, nombre, berlin, tunel):
        super().__init__()
        pass

    def run(self):
        '''
        Funcionalidad de Excavador que crea x metros de tunel cada 10 min,
        cada iteracion chequea si se cumple que hay problema con la picota (10%)
        '''
        self.avanzar(random.randint(50, 100))
        if random.uniform(0, 1) <= 0.1:
            self.problema_picota()

    def problema_picota(self):
        '''
        Probabilida de problema con la picota de 10%
        Se llama a berlin para resolverlo
        '''
        with self.berlin:
            utils.reloj(5)

    def avanzar(self, metros):
        '''
        Usar este método para avanzar en la excavación del túnel
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param metros: int
        '''
        self.tunel.metros_avanzados -= metros
