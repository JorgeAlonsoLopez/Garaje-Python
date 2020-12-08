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


def datos_facturacion():
    fecha1 = None
    fecha2 = None
    fin = True
    while fin:
        try:
            dia1 = int(input('Introduzca el día de la fecha de inicio, p. ej. 1, 21: '))
            mes1 = int(input('Introduzca el mes de la fecha de inicio, p. ej. 1, 11: '))
            anio1 = int(input('Introduzca el año de la fecha de inicio, p. ej. 2004, 1999: '))
            hora1 = int(input('Introduzca la hora de la fecha de inicio en formato 24H, p. ej. 1, 23: '))
            min1 = int(input('Introduzca los minutos de la fecha de inicio, p. ej. 1, 48: '))
            dia2 = int(input('Introduzca el día de la fecha final, p. ej. 1, 21: '))
            mes2 = int(input('Introduzca el mes de la fecha final, p. ej. 1, 11: '))
            anio2 = int(input('Introduzca el año de la fecha final, p. ej. 2004, 1999: '))
            hora2 = int(input('Introduzca la hora de la fecha final en formato 24H, p. ej. 1, 23: '))
            min2 = int(input('Introduzca los minutos de la fecha final, p. ej. 1, 48: '))
            if not type(dia1) is int:
                raise TypeError
            if dia1 > 31 and dia1 < 1:
                raise ValueError
            if not type(mes1) is int:
                raise TypeError
            if mes1 > 12 and mes1 < 1:
                raise ValueError
            if not type(dia2) is int:
                raise TypeError
            if dia2 > 31 and dia2 < 1:
                raise ValueError
            if not type(mes2) is int:
                raise TypeError
            if mes2 > 31 and mes2 < 1:
                raise ValueError
            if not type(anio1) is int:
                raise TypeError
            if not type(anio2) is int:
                raise TypeError
            if not type(hora1) is int:
                raise TypeError
            if hora1 > 23 and hora1 < 0:
                raise ValueError
            if not type(hora2) is int:
                raise TypeError
            if hora2 > 23 and hora2 < 0:
                raise ValueError
            if not type(min1) is int:
                raise TypeError
            if min1 > 59 and min1 < 0:
                raise ValueError
            if not type(min2) is int:
                raise TypeError
            if min2 > 59 and min2 < 0:
                raise ValueError
            fecha1 = datetime(anio1, mes1, dia1, hora1, min1)
            fecha2 = datetime(anio2, mes2, dia2, hora2, min2)
            fin = False
            return fecha1, fecha2
        except TypeError:
            print("Solo se permiten números entreos.")
            print("Se volverán a pedir los datos")
        except ValueError:
            print("La opción del mes tiene que estar entre 1 y 12 para los meses y de 1 a 31 para los días según corresponda el mes.")
            print("Se volverán a pedir los datos")






def facturacion(listado_ticket):
    fecha1, fecha2 = datos_facturacion()
    aux=[]
    total=0
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




