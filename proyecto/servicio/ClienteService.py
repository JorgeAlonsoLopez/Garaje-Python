from modelo.Cliente import *
from modelo.Vehiculo import *

def modificar_cliente(cliente):
    nombre = input("Por favor, inserte su nombre: ")
    apellidos = input("Por favor, inserte sus apellidos: ")
    tarjeta = input("Por favor, inserte su número de tarjeta: ")
    email = input("Por favor, inserte su email: ")
    cliente.nombre=nombre
    cliente.apellidos=apellidos
    cliente.numTarjeta=tarjeta
    cliente.email=email
    return cliente


def crear_cliente():
    dni = input("Introduzca el dni del usuario: ")
    nombre = input("Introduzca el nombre del usuario: ")
    apellidos = input("Introduzca los apellido del usuario: ")
    tarjeta = input("Introduzca la tarjeta de crédito del usuario: ")
    email = input("Introduzca el email del usuario: ")
    matricula = input("Introduzca la matrícula del vehículo: ")
    vehiculo = Vehiculo(matricula)
    cliente = Cliente(dni, nombre, apellidos, email, tarjeta, vehiculo)
    return cliente
