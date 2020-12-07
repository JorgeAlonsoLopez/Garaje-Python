from .Plaza import Plaza

class PlazaMin(Plaza):
    def __init__(self, nombre, coste):
        self.__nombre = nombre
        self.__coste = coste

    def __str__(self):
        if self.ocupado:
            if self.reservado:
                return f"La plaza para movilidad reducida {self.nombre} está ocupada por {self.abono.cliente.nombre} {self.abono.cliente.nombre} (DNI: {self.abono.cliente.dni})."
            else:
                return f"La plaza para movilidad reducida {self.nombre}  está ocupada por una persona de forma temporal, con el vehiculo de movilidad reducida con matricula {self.vehiculo.matricula}."
        else:
            if self.reservado:
                return f"La plaza para movilidad reducida {self.nombre} está libre pero le pertenece a {self.abono.cliente.nombre} {self.abono.cliente.nombre} (DNI: {self.abono.cliente.dni})."
            else:
                return f"La plaza para movilidad reducida {self.nombre} está libre."
