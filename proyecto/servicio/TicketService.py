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
            try:
                print(f"El precio a pagar son: {precio} €")
                dinero = int(input("Inserte el dinero, en euros(€), sin céntimos. "))
                if dinero >= 0:
                    raise ValueError
                if dinero >= precio:
                    correcto = True
                    ticket.coste = precio
                    print(f"El cambio es: {round(dinero - precio,2)} €")
                else:
                    print("La cantidad es menor a la esperada. ")
            except ValueError:
                print("La cantidad a insertar debe ser superior o igual a 0 €.")
                print("Se volverán a pedir los datos")


def pedir_fecha(msg):

    fecha = None
    fin = True
    while fin:
        try:
            dia = int(input(f'Introduzca el día de la fecha de {msg}, p. ej. 1, 21: '))
            if dia > 31 or dia < 1:
                raise ValueError
            mes = int(input(f'Introduzca el mes de la fecha de {msg}, p. ej. 1, 11: '))
            if mes > 12 or mes < 1:
                raise ValueError
            anio = int(input(f'Introduzca el año de la fecha de {msg}, p. ej. 2004, 1999: '))
            if anio < 2019 :
                raise ValueError
            hora = int(input(f'Introduzca la hora de la fecha de {msg} en formato 24H, p. ej. 1, 23: '))
            if hora > 23 or hora < 0:
                raise ValueError
            min = int(input(f'Introduzca los minutos de la fecha de {msg}, p. ej. 1, 48: '))
            if min > 59 or min < 0:
                raise ValueError
            fecha = datetime(anio, mes, dia, hora, min)
            fin = False
        except ValueError:
            print("Los datos tienen que ser enteros, para los meses tiene que estar entre 1 y 12 para los meses, de 1 a 31 para días, "
                  "de 0 a 11 para horas, de 0 a 59 para minutos y años superiores al 2019.")
            print("Se volverán a pedir los datos")
    return fecha

def datos_facturacion():
    fecha1 = pedir_fecha("inicio")
    fecha2 = pedir_fecha("fin")
    return fecha1, fecha2






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
    res=""
    res += "*********************************\n"
    res += f"Matrícula del vehículo: {ticket.matricula} \n"
    res += f"Plaza del parking: {ticket.plaza.nombre} \n"
    res += f"Fecha y hora de estacionamiento: {ticket.fechaEntrada.strftime('%d-%m-%Y  %H:%M:%S')} \n"
    res += f"PIN: {ticket.pin} \n"
    if ticket.coste != 0:
        res += f"Coste: {ticket.coste} €\n"

    if ticket.fechaSalida != None:
        res += f"Fecha y hora de salida: {ticket.fechaSalida.strftime('%d-%m-%Y  %H:%M:%S')} \n"

    res += "**********************************\n"
    return res



