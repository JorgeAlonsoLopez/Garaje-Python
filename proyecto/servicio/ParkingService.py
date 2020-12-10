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
    for plaza in parking.listaMoviReducf:
        lista.append(plaza)

    for i in lista:
        res += str(i)+"\n"

    return print(res)

def mostrar_info_gen(parking):

    res = ""
    cont = 0
    for plaza in parking.listaCoches:
        if plaza.reservado == False and plaza.ocupado == False:
            cont += 1
    res += f"Para las plazas de coches, hay el siguiente número de plazas libres: {cont} \n"
    cont = 0
    for plaza in parking.listaMotos:
        if plaza.reservado == False and plaza.ocupado == False:
            cont += 1
    res += f"Para las plazas de motos, hay el siguiente número de plazas libres: {cont} \n"
    cont = 0
    for plaza in parking.listaMoviReducf:
        if plaza.reservado == False and plaza.ocupado == False:
            cont += 1
    res += f"Para las plazas de movilidad reducida, hay el siguiente número de plazas libres: {cont} \n"

    return print(res)


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
        for plaza in parking.listaMoviReducf:
            if plaza.reservado == False and plaza.ocupado == False and encontrado == False:
                plaza_libre = plaza
                encontrado = True

    return plaza_libre

def asignar_plaza_abon(parking, tipo):
    plaza_libre = None
    encontrado = False
    if tipo == 1:
        for plaza in parking.listaCoches:
            if plaza.reservado == False and encontrado == False:
                plaza_libre = plaza
                encontrado = True
    elif tipo == 2:
        for plaza in parking.listaMotos:
            if plaza.reservado == False and encontrado == False:
                plaza_libre = plaza
                encontrado = True
    elif tipo ==3:
        for plaza in parking.listaMoviReducf:
            if plaza.reservado == False and encontrado == False:
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
        for plaza in parking.listaMoviReducf:
            if plaza.reservado == False and plaza.ocupado == False:
                resl = True
    return resl

def is_free_space_abon(tipo, parking):
    resl = False
    if tipo == 1:
        for plaza in parking.listaCoches:
            if plaza.reservado == False:
                resl = True
    elif tipo == 2:
        for plaza in parking.listaMotos:
            if plaza.reservado == False:
                resl = True
    elif tipo ==3:
        for plaza in parking.listaMoviReducf:
            if plaza.reservado == False:
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
        serv_tick.pintar_ticket(ticket)
    if result:
        return "Se ha finalizado el aparcado el vehículo sin problemas."
    else:
        return "No se puede aparcar, no hay sitio."

def depositar_vehiculo_abonado(dni, matricula, lista_abonos):
    abono = serv_abo.search_by_dni(lista_abonos,dni)
    if abono != None:
        if abono.cliente.vehiculo.matricula == matricula :
            if abono.plaza.ocupado == False:
                if abono.estrenado == False:
                    abono.estrenado = True
                    abono.fechaInicial = datetime.now()
                    abono.fechaFinal = (datetime.now() + datedelta.datedelta(months=abono.meses))
                abono.plaza.ocupado = True
                abono.plaza.vehiculo = abono.cliente.vehiculo
                print("El vehículo se ha aparcado con éxito.")
                print("Gracias por usar nuestros servicios.")
            else:
                if abono.plaza.vehiculo.matricula == matricula:
                    print("Puede que se le haya olvidado, pero ya a apacado.")
                else:
                    print("Va tener que esperar para estrenar la plaza.")
        else:
            print("No se puede proceder con los datos aportados.")
    else:
        print("No se puede proceder con los datos aportados.")


    return


