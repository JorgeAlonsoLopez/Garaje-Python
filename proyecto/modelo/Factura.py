
class Factura():
    def __init__(self, fecha, cliente, coste):
        self.__fecha = fecha
        self.__cliente = cliente
        self.__coste = coste

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, fecha):
        self.__fecha = fecha

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, coste):
        self.__coste = coste







