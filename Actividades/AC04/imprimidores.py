from threading import Thread, Lock
from utils import reloj
import random


class Imprimidor(Thread):

    def __init__(self, nombre, berlin, bolsa_dinero):
        super().__init__()
        self.name = nombre
        self.berlin = berlin
        self.bolsa_dinero = bolsa_dinero
        self.usar_bolsa = Lock()

    def run(self):
        '''
        Funcionalidad de iMPRIMIDOR que imprime dinero cada 5 minutos, cada
        iteracion chequea si se cumple que hay problema con el dinero (20%)
        '''
        while self.bolsa_dinero.dinero_acumulado < self.bolsa_dinero.meta_dinero:
            self.imprimir_dinero(random.randint(100000, 500000))
            reloj(10)
            if random.uniform(0, 1) <= 0.2:
                self.problema_papel()
            if self.bolsa_dinero.dinero_acumulado >= self.bolsa_dinero.meta_dinero:
                self.bolsa_dinero.dinero_listo.set()

    def imprimir_dinero(self, dinero):
        '''
        Llamar a este método para imprimir dinero.
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param dinero:
        :return:
        '''
        print(f"{self.name}: Imprimiendo {dinero} euros")
        with self.bolsa_dinero.usar_bolsa:
            self.bolsa_dinero.dinero_acumulado += dinero

    def problema_papel(self):
        '''
        Probabilidad de problema con el papel de 20%
        '''
        print(f"{self.name}: Tengo un problema con el papel")
        with self.berlin:
            reloj(10)
