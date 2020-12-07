
class Ticket():
    def __init__(self, fechaEntrada, matricula, plaza):
        self.__fechaEntrada = fechaEntrada
        self.__matricula = matricula
        self.__plaza = plaza

    @property
    def fechaEntrada(self):
        return self.__fechaEntrada

    @fechaEntrada.setter
    def fechaEntrada(self, fechaEntrada):
        self.__fechaEntrada = fechaEntrada

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    @property
    def plaza(self):
        return self.__plaza

    @plaza.setter
    def plaza(self, plaza):
        self.__plaza = plaza








