import random
class Ticket():
    def __init__(self, fechaEntrada, matricula, plaza):
        self.__fechaEntrada = fechaEntrada
        self.__fechaSalida = None
        self.__matricula = matricula
        self.__plaza = plaza
        self.__coste = 0
        self.__pin = random.randrange(100000,1000000)

    @property
    def fechaEntrada(self):
        return self.__fechaEntrada

    @fechaEntrada.setter
    def fechaEntrada(self, fechaEntrada):
        self.__fechaEntrada = fechaEntrada

    @property
    def fechaSalida(self):
        return self.__fechaSalida

    @fechaSalida.setter
    def fechaSalida(self, fechaSalida):
        self.__fechaSalida = fechaSalida

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, coste):
        self.__coste = coste

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, pin):
        self.__pin = pin

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza








