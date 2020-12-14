import repositorio.ParkingRepository as repo
from modelo.Vehiculo import *
from modelo.Ticket import *
from datetime import datetime
from datetime import timedelta
import datedelta
import servicio.TicketService as serv_tick
import servicio.AbonoService as serv_abo

def search_plaza_by_name(parking, nombre):
     return repo.search_plaza_by_name(parking, nombre)

def save_file(parking):
    return repo.save_file(parking)

def load_file():
    return repo.load_file()

def mostrar_info_detll(parking):
    lista = []
    res = ""
    for plaza in parking.listaCoches:
        lista.append(plaza)
    for plaza in parking.listaMotos:
        lista.append(plaza)
    for plaza in parking.listaMoviReduc:
        lista.append(plaza)

    for i in lista:
        res += str(i)+"\n\n"

    return res

def mostrar_info_gen(parking):

    res = ""
    cont = 0
    for plaza in parking.listaCoches:
        if plaza.reservado == False:
            if plaza.ocupado == False:
                cont += 1
    res += f"Para las plazas de coches, hay el siguiente número de plazas libres: {cont} \n"
    cont = 0
    for plaza in parking.listaMotos:
        if plaza.reservado == False:
            if plaza.ocupado == False:
                cont += 1
    res += f"Para las plazas de motos, hay el siguiente número de plazas libres: {cont} \n"
    cont = 0
    for plaza in parking.listaMoviReduc:
        if plaza.reservado == False:
            if plaza.ocupado == False:
                cont += 1
    res += f"Para las plazas de movilidad reducida, hay el siguiente número de plazas libres: {cont} \n"

    return res


def asignar_plaza(parking, tipo):
    plaza_libre = None
    encontrado = False
    if tipo == 1:
        for plaza in parking.listaCoches:
            if plaza.reservado == False and plaza.ocupado == False and encontrado == False:
                plaza_libre = plaza
                encontrado = True
    elif tipo == 2:
        for plaza in parking.listaMotos:
            if plaza.reservado == False and plaza.ocupado == False and encontrado == False:
                plaza_libre = plaza
                encontrado = True
    elif tipo ==3:
        for plaza in parking.listaMoviReduc:
            if plaza.reservado == False and plaza.ocupado == False and encontrado == False:
                plaza_libre = plaza
                encontrado = True

    return plaza_libre

def is_free_space(tipo, parking):
    resl = False
    if tipo == 1:
        for plaza in parking.listaCoches:
            if plaza.reservado == False and plaza.ocupado == False:
                resl = True
    elif tipo == 2:
        for plaza in parking.listaMotos:
            if plaza.reservado == False and plaza.ocupado == False:
                resl = True
    elif tipo ==3:
        for plaza in parking.listaMoviReduc:
            if plaza.reservado == False and plaza.ocupado == False:
                resl = True
    return resl


def depositar_vehiculo(matricula, tipo, lista_tick, parking):
    result = False
    if is_free_space(tipo,parking):
        result = True
        plaza = asignar_plaza(parking, tipo)
        vehiculo = Vehiculo(matricula)
        plaza.vehiculo = vehiculo
        ticket = Ticket(datetime.now(),matricula,plaza)
        ticket.pin = random.randrange(100000,1000000)
        serv_tick.add(lista_tick,ticket)
        plaza.ocupado = True
        #serv_tick.pintar_ticket(ticket)
        if result:
            res = "Se ha finalizado el aparcado el vehículo sin problemas."
            return res, ticket
    else:
        res = "No se puede aparcar, no hay sitio."
        return res, None

def modifPlz(ocupado, vehiculo, nombre, parking):
    plaza = search_plaza_by_name(parking, nombre)
    plaza.ocupado = ocupado
    plaza.vehiculo = vehiculo
    

def depositar_vehiculo_abonado(dni, matricula, lista_abonos, parking):
    res = ""
    abono = serv_abo.search_by_dni(lista_abonos,dni)
    if abono != None:
        if abono.fechaFinal >= datetime.now():
            if abono.fechaInicial <= datetime.now():
                if abono.cliente.vehiculo.matricula == matricula :
                    if abono.plaza.ocupado == False:
                        abono.plaza.ocupado = True
                        abono.plaza.vehiculo = abono.cliente.vehiculo
                        modifPlz(True, abono.cliente.vehiculo, abono.plaza.nombre, parking)
                        res +="El vehículo se ha aparcado con éxito.\n"
                        res +="Gracias por usar nuestros servicios."
                    else:
                       res +="Puede que se le haya olvidado, pero ya a aparcado."
                else:
                    res +="No se puede proceder con los datos aportados."
            else:
                res +="Todavía no ha entrado en vigor el abono, tiene que esperar a la fecha establecida"
        else:
            res +="Su abono a caducado, va a tener que renovarlo"
    else:
       res +="No se puede proceder con los datos aportados."
    return res

def retirar_vehiculo(matricula, nombre_plaza, pin, parking, lista_tick):
    plaza = search_plaza_by_name(parking, nombre_plaza)
    if plaza != None:
        tick = serv_tick.search_by_matricula(lista_tick, matricula)
        if tick != None:
            if pin == tick.pin:
                tick.fechaSalida = datetime.now()
                plaza.ocupado = False
                plaza.vehiculo=None
                tick.plaza = plaza



def retirar_vehiculo_abonado(matricula, nombre_plaza, lista_abonos, pin, parking):
    res = ""
    abono = serv_abo.search_by_nombre_plaza(lista_abonos,nombre_plaza)
    if abono != None:
        if abono.fechaInicial <= datetime.now():
            if abono.cliente.vehiculo.matricula == matricula and abono.pin == pin:
                if abono.plaza.ocupado == True:
                    abono.plaza.ocupado = False
                    abono.plaza.vehiculo = None
                    modifPlz(False, None, abono.plaza.nombre, parking)
                    res +="El vehículo se ha retirado con éxito.\n"
                    res +="Gracias por usar nuestros servicios."
                else:
                    res +="Puede que se le haya olvidado, pero no ha guardado el vehículo."
            else:
                res +="No se puede proceder con los datos aportados."
        else:
            res +="Todavía no ha entrado en vigor el abono, tiene que esperar a la fecha establecida"
    else:
        res +="No se puede proceder con los datos aportados."
    return res





