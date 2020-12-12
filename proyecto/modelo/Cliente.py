
class Cliente():
    def __init__(self, dni, nombre, apellidos, email, numTarjeta, vehiculo):
        self.__dni = dni
        self.__nombre = nombre
        self.__apellidos = apellidos
        self.__email = email
        self.__numTarjeta = numTarjeta
        self.__vehiculo = vehiculo

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def apellidos(self):
        return self.__apellidos

    @apellidos.setter
    def apellidos(self, apellidos):
        self.__apellidos = apellidos

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def numTarjeta(self):
        return self.__numTarjeta

    @numTarjeta.setter
    def numTarjeta(self, numTarjeta):
        self.__numTarjeta = numTarjeta

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo





