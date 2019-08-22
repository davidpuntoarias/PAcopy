from entidades_banco import Cliente, BancoDCC
from os import path
'''
Deberas completar las clases ClienteSeguro, BancoSeguroDCC y  sus metodos
'''


class ClienteSeguro(Cliente):
    def __init__(self, id_cliente, nombre, contrasena):
        super().__init__(self, id_cliente, nombre, contrasena)
        self.tiene_fraude = False

    @property
    def saldo_actual(self):
        return self.saldo

    @saldo_actual.setter
    def saldo_actual(self, nuevo_saldo):
        if nuevo_saldo < 0:
            self.tiene_fraude = True

    def deposito_seguro(self, dinero):
        self.depositar(dinero)
        self.saldo_actual = self.dinero
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            archivo.write(f"{self.id_cliente}, deposita, {dinero}")

    def retiro_seguro(self, dinero):
        if not self.tiene_fraude:
            self.retirar(dinero)
            self.saldo_actual(self.dinero)
        ruta_transacciones = path.join('banco_seguro', 'transacciones.txt')
        with open(ruta_transacciones, 'a+', encoding='utf-8') as archivo:
            archivo.write(f"{self.id_cliente}, retira, {dinero}")

class BancoSeguroDCC(BancoDCC):
    def __init__(self):
        super().__init__(self)

    def cargar_clientes(self, ruta):
        with open(ruta, "rt") as archivo:
            lines = archivo.readlines()
        clients = []
        for linea in lines:
            persona = linea.split(",")
            clients.append(ClienteSeguro(persona[0], persona[1], persona[2])
        self.clientes = clients

    def realizar_transaccion(self, id_cliente, dinero, accion):
        for client in range(len(self.clientes)):
            if id_cliente == clientes[client][0]:
                break
        
    def verificar_historial_transacciones(self, historial):
        print('Validando transacciones')
        # completar
        pass

    def validar_monto_clientes(self, ruta):
        print('Validando monto de los clientes')
        # completar
        pass
