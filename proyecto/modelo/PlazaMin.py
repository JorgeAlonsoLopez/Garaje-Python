from .Plaza import Plaza

class PlazaMin(Plaza):
    def __init__(self, nombre, coste):
        super().__init__(nombre, coste)

    def __str__(self):
        if self.ocupado:
            if self.reservado:
                return f"La plaza para movilidad reducida {self.nombre} está ocupada por un abonado."
            else:
                return f"La plaza para movilidad reducida {self.nombre}  está ocupada por una persona de forma temporal."
        else:
            if self.reservado:
                return f"La plaza para movilidad reducida {self.nombre} está libre pero le pertenece a un abonado."
            else:
                return f"La plaza para movilidad reducida {self.nombre} está libre."

    def info(self, abono):
        if self.reservado:
            return self.__str__() + f"El abonado es: {abono.cliente.nombre} {abono.cliente.nombre} (DNI: {abono.cliente.dni})"
        else:
            if self.ocupado:
                return self.__str__() + f"El vehiculo de movilidad reducida posee la matrícula: {self.vehiculo.matricula}."
