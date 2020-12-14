from modelo.Cliente import *
from modelo.Vehiculo import *

def modificar_cliente(cliente, nombre, apellidos, tarjeta, email):
    cliente.nombre=nombre
    cliente.apellidos=apellidos
    cliente.numTarjeta=tarjeta
    cliente.email=email
    return cliente


def crear_cliente():
    try:
        dni = input("Introduzca el dni del usuario: ")
        if dni == "":
            raise ValueError
        nombre = input("Introduzca el nombre del usuario: ")
        if nombre == "":
            raise ValueError
        apellidos = input("Introduzca los apellido del usuario: ")
        if apellidos == "":
            raise ValueError
        tarjeta = input("Introduzca la tarjeta de crédito del usuario: ")
        if tarjeta == "":
            raise ValueError
        email = input("Introduzca el email del usuario: ")
        if email == "":
            raise ValueError
        matricula = input("Introduzca la matrícula del vehículo: ")
        if matricula == "":
            raise ValueError
        vehiculo = Vehiculo(matricula)
        cliente = Cliente(dni, nombre, apellidos, email, tarjeta, vehiculo)
        return cliente
    except ValueError:
        print("Los campos no deben estar vacíos.")
        print("Se cancela la operación")
