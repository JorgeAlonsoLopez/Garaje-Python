import repositorio.TicketRepository as repo
import servicio.ParkingService as park_serv
from datetime import datetime
from datetime import timedelta
from math import ceil

def add(listado_ticket, ticket):
    return repo.add(listado_ticket, ticket)

def remove(listado_ticket, ticket):
    return repo.remove(listado_ticket, ticket)

def search_by_matricula(listado_ticket, matricula):
    return repo.search_by_matricula(listado_ticket, matricula)

def save_file(listado_ticket):
    return repo.save_file(listado_ticket)

def load_file():
    return repo.load_file()


def pagar_ticket(nombre_plaza, parking, ticket):

    plaza = park_serv.search_plaza_by_name(parking, nombre_plaza)
    if(plaza != None):
        correcto = False
        actual=datetime.now()
        min=(ceil((actual-ticket.fechaEntrada).total_seconds()/60))
        precio = min * plaza.coste
        while not correcto:
            print(f"El precio a pagar son: {precio} €")
            dinero = int(input("Inserte el dinero, en euros(€). "))
            if dinero >= precio:
                correcto = True
                ticket.coste = precio
                print(f"El cambio es: {round(dinero - precio,2)} €")
            else:
                print("La cantidad es menor a la esperada. ")


def facturacion(listado_ticket, fecha1, fecha2):

    aux=[];
    total=0;
    for ticket in listado_ticket:
        if ticket.fechaEntrada >= fecha1 and ticket.fechaEntrada <= fecha2:
            aux.append(ticket)
    for i in aux:
        total += i

    return round(total,2)

def pintar_ticket(ticket):

    print("*********************************")
    print(f"Matrícula del vehículo: {ticket.matricula} ")
    print(f"Plaza del parking: {ticket.plaza.nombre} ")
    print(f"Fecha y hora de estacionamiento: {ticket.fechaEntrada.strftime('%d-%m-%Y  %H:%M:%S')} ")
    print(f"PIN: {ticket.pin} ")
    if ticket.coste != 0:
        print(f"Coste: {ticket.coste} €")

    if ticket.fechaSalida != None:
        print(f"Fecha y hora de salida: {ticket.fechaSalida.strftime('%d-%m-%Y  %H:%M:%S')} ")

    print("**********************************")




