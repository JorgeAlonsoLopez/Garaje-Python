class Plaza():
    def __init__(self, nombre, coste):
        self.__nombre = nombre
        self.__coste = coste
        self.__ocupado = False
        self.__reservado = False
        self.__vehiculo = None
        self.__abono = None

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def coste(self):
        return self.__coste

    @coste.setter
    def coste(self, coste):
        self.__coste = coste

    @property
    def ocupado(self):
        return self.__ocupado

    @ocupado.setter
    def ocupado(self, ocupado):
        self.__ocupado = ocupado

    @property
    def reservado(self):
        return self.__reservado

    @reservado.setter
    def reservado(self, reservado):
        self.__reservado = reservado

    @property
    def vehiculo(self):
        return self.__vehiculo

    @vehiculo.setter
    def vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo

    @property
    def abono(self):
        return self.__abono

    @abono.setter
    def abono(self, abono):
        self.__abono = abono


    def __str__(self):
        if self.ocupado:
            if self.reservado:
                return f"La plaza genérica {self.nombre} está ocupada por {self.abono.cliente.nombre} {self.abono.cliente.nombre} (DNI: {self.abono.cliente.dni})."
            else:
                return f"La plaza genérica {self.nombre} está ocupada por una persona de forma temporal, con el vehiculo con matricula {self.vehiculo.matricula}."
        else:
            if self.reservado:
                return f"La plaza genérica {self.nombre} está libre pero le pertenece a {self.abono.cliente.nombre} {self.abono.cliente.nombre} (DNI: {self.abono.cliente.dni})."
            else:
                return f"La plaza genérica {self.nombre} está libre."

