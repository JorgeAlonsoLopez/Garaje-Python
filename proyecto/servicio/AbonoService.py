import repositorio.AbonoRepository as repo
from datetime import datetime
from datetime import timedelta
import datedelta
from modelo.Factura import *
from modelo.Abono import *
from modelo.Cliente import *
import calendar
import servicio.FacturaService as fact_serv
import servicio.ParkingService as park_serv
import servicio.ClienteService as clin_serv

def add(listado_abonos, abono):
    return repo.add(listado_abonos, abono)

def remove(listado_abonos, abono):
    return repo.remove(listado_abonos, abono)

def search_by_dni(listado_abonos, dni):
    return repo.search_by_dni(listado_abonos, dni)

def search_by_nombre_plaza(listado_abonos, nombre_plaza):
    return repo.search_by_nombre_plaza(listado_abonos, nombre_plaza)

def save_file(listado_abonos):
    return repo.save_file(listado_abonos)

def load_file():
    return repo.load_file()

def caducidad_abono_m_y(mes, anio, listado_abonos):
    lista = []
    for abono in listado_abonos:
        if abono.fechaFinal.month == mes and abono.fechaFinal.year == anio:
            lista.append(abono)
    return lista

def pedir_datos_fecha():
    fecha1 = None
    fin = True
    while fin:
        try:
            dia = int(input(f'Introduzca el día, p. ej. 1, 21: '))
            if dia > 31 or dia < 1:
                raise ValueError
            mes = int(input(f'Introduzca el mes, p. ej. 1, 11: '))
            if mes > 12 or mes < 1:
                raise ValueError
            anio = int(input(f'Introduzca el año, p. ej. 2004, 1999: '))
            if anio < 2019 :
                raise ValueError
            fecha1 = datetime(anio, mes, dia)
            fin = False
            return fecha1
        except TypeError:
            print("Solo se permiten números enteros.")
            print("Se volverán a pedir los datos")
        except ValueError:
            print("La opción del mes tiene que estar entre 1 y 12 para los meses y de 1 a 31 para los días según corresponda el mes.")
            print("Se volverán a pedir los datos")

def crear_abono(listado_abonos, lista_facturas, parking, tipo_abo, tipo_plaza, fecha, cliente):
    sol=""
    rest = park_serv.is_free_space(tipo_plaza, parking)
    if rest:
        plaza = park_serv.asignar_plaza(parking, tipo_plaza)
        plaza.reservado = True
        mes, precio = tipo_abono(tipo_abo)
        abono = Abono(cliente, fecha, (fecha + datedelta.datedelta(months=mes)), mes, precio)
        abono.plaza = plaza
        repo.add(listado_abonos, abono)
        factura = Factura(datetime.now(), cliente, precio)
        fact_serv.add(lista_facturas, factura)
        sol += f"Su plaza es la siguiente, no se olvide: {abono.plaza.nombre}\n"
        sol += f"Su pin es el siguiente, no lo pierda: {abono.pin}"
    else:
       sol = "No es posible conceder el abono ya que no hay plazas disponibles en este momento."
    return sol

def tipo_abono(opt):

    if opt > 4 or opt < 1:
        raise ValueError
    if opt == 1:
        mes=1
        precio=25
        return mes, precio
    elif opt == 2:
        mes=3
        precio=70
        return mes, precio
    elif opt == 3:
        mes=6
        precio=130
        return mes, precio
    elif opt == 4:
        mes=12
        precio=200
        return mes, precio



def listar_caducidad_proximos_dias(listado_abonos):
    res = ""
    lista = []
    hoy = datetime.now()
    tope = hoy + timedelta(days=10)
    for abono in listado_abonos:
        if abono.fechaFinal >= hoy and abono.fechaFinal <= tope:
            lista.append(abono)
    res += f"El número de abonos que caducan en los próximos 10 días son: {len(lista)}\n\n"
    if len(lista) > 0:
        res +="Los abonos que caducan son los siguinetes: \n\n"
        for abono in lista:
            res += f"El abono perteneciente a {abono.cliente.nombre} {abono.cliente.apellidos}, " \
                   f"con una duración de {abono.meses} mes/es, emitido el {abono.fechaInicial.strftime('%d-%m-%Y')} " \
            f"para el vehículo con matrícula {abono.cliente.vehiculo.matricula}\n\n"
    return res

def obtener_lista_cad(lista_abonos,mes, anio):

    lista = []
    fallo = True
    fail=""
    sol=""
    try:
        mesComprobar = int(mes)
        anioComprobar = int(anio)
        if mesComprobar > 12 or mesComprobar < 1:
            raise ValueError
        if anioComprobar < 2010:
            raise ValueError
        fallo = False
        fail=""
        for abono in lista_abonos:
            if abono.fechaFinal.month == mesComprobar and abono.fechaFinal.year == anioComprobar:
                lista.append(abono)
        sol=""
        return fallo ,lista, fail, sol
    except ValueError:
        fail="Los datos tienen que ser número enteros. La opción del mes tiene que estar entre 1 y 12 y años superiores al 2010."
        sol=""
        return fallo ,lista, fail, sol

def listar_caducidad_mes(fallo, lista):
    res=""
    if not fallo:
        res += f"El número de abonos que caducan en el mes y año indicado son: {len(lista)} \n\n"
        if len(lista) > 0:
            res += "Los abonos que caducan son los siguinetes: \n\n"
            for abono in lista:
                res += f"El abono perteneciente a {abono.cliente.nombre} {abono.cliente.apellidos}, " \
                       f"con una duración de {abono.meses} mes/es, emitido el {abono.fechaInicial.strftime('%d-%m-%Y')} " \
                       f"para el vehículo con matrícula {abono.cliente.vehiculo.matricula}\n\n"
    return res

def renovar_abono(listado_abonos,listado_facturas, dni, tipo_abo):
    ok = False
    res=""
    abono = search_by_dni(listado_abonos, dni)
    if abono != None:
        ok = True
        mes, precio = tipo_abono(tipo_abo)
        abono.fechaFinal= (datetime.now() + datedelta.datedelta(months=mes))
        abono.meses=mes
        abono.precio=precio
        factura = Factura(datetime.now(), abono.cliente, precio)
        fact_serv.add(listado_facturas, factura)
        res = "Se ha renovado el abono con éxito"
    else:
        res = "No nos consta un abono que esté contratado por una persona con ese DNI"
    return ok, res

def modificar_abonado(listado_abonos, dni, nombre, apellidos, tarjeta, email):
    abono = search_by_dni(listado_abonos, dni)
    res =""
    if abono != None:
        cliente = clin_serv.modificar_cliente(abono.cliente, nombre, apellidos, tarjeta, email)
        abono.cliente = cliente
        res="La actualización de los datos del cliente ha sido correcta"
    else:
        res="No nos consta un abono perteneciente a un cliente con ese DNI"
    return res


