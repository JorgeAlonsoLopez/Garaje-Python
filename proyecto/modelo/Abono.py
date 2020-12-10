import random
class Abono():
    def __init__(self, cliente, fechaInicial, fechaFinal, meses, precio):
        self.__cliente = cliente
        self.__fechaInicial = fechaInicial
        self.__fechaFinal = fechaFinal
        self.__meses = meses
        self.__precio = precio
        self.__pin = random.randrange(100000,1000000)
        self.__plaza = None
        self.__estrenado = False

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def estrenado(self):
        return self.__estrenado

    @estrenado.setter
    def estrenado(self, estrenado):
        self.__estrenado = estrenado

    @property
    def fechaInicial(self):
        return self.__fechaInicial

    @fechaInicial.setter
    def fechaInicial(self, fechaInicial):
        self.__fechaInicial = fechaInicial

    @property
    def fechaFinal(self):
        return self.__fechaFinal

    @fechaFinal.setter
    def fechaFinal(self, fechaFinal):
        self.__fechaFinal = fechaFinal

    @property
    def meses(self):
        return self.__meses

    @meses.setter
    def meses(self, meses):
        self.__meses = meses

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, precio):
        self.__precio = precio

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

