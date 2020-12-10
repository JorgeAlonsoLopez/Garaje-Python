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

def comprobar_creacion_abono(parking):
    rest = False
    try:
        tipo = int(input("Introduzca el tipo de vehículo (1-coche, 2-moto, 3-movilidad reducida): "))
        if not type(tipo) is int:
            raise TypeError
        if tipo > 3 and tipo < 1:
            raise ValueError
        rest = park_serv.is_free_space_abon(tipo, parking)
        return tipo, rest
    except TypeError:
        print("Solo se permiten números entreos.")
        print("Se cancela la operación")
    except ValueError:
        print("Los numeros tienen que estar entre 1 y 3.")
        print("Se cancela la operación")


def crear_abono(listado_abonos, lista_facturas, parking):
    tipo, rest = comprobar_creacion_abono(parking)
    acept = int(input("Las condiciones son las siguientes:\n"
                      "Si en el momento de contratar su abono no hay una plaza que se encuentre libre para asignarsela,\n"
                      "se le asignará una ocupada y el tiempo contratado empezará a contar a partir de que deposite su\n"
                      "vehículo por primera vez.\n\n"
                      "Si está de acuerdo pulse 1, en caso contrario, pulse 2 y se cancelará la contratación del abono."))
    try:
        if not type(acept) is int:
            raise TypeError
        if acept != 1 or acept != 2:
            raise ValueError
        if acept == 1:
            if rest:
                cliente = clin_serv.crear_cliente()
                plaza = park_serv.asignar_plaza_abon(parking, tipo)
                plaza.reservado = True
                mes, precio = tipo_abono()
                abono = Abono(cliente, datetime.now(), (datetime.now() + datedelta.datedelta(months=mes)), mes, precio)
                if plaza.ocupado == False:
                    abono.estrenado = True
                else:
                    abono.estrenado = False
                    abono.fechaInicial = None
                    abono.fechaFinal = None
                abono.plaza = plaza
                repo.add(listado_abonos, abono)
                factura = Factura(datetime.now(), cliente, precio)
                fact_serv.add(lista_facturas, factura)
                print(f"Su pin es el siguiente, no lo pierda: {abono.pin}")
    except TypeError:
        print("Solo se permiten números entreos.")
        print("Se cancela la operación")
    except ValueError:
        print("Los numeros tienen que ser 1 o 2.")
        print("Se cancela la operación")


def tipo_abono():
    try:
        opt = int(input("Introduzca el tipo de abono que sea contratar.\n"
                    "(1-mensual(25€), 2-trimestral(75€), 3-semestral(130€), 4-anual(200€)"))
        if not type(opt) is int:
            raise TypeError
        if opt > 4 and opt < 1:
            raise ValueError
        if opt == 1:
            mes=1
            precio=25
            return mes, precio
        elif opt == 2:
            mes=3
            precio=75
            return mes, precio
        elif opt == 3:
            mes=6
            precio=130
            return mes, precio
        elif opt == 4:
            mes=12
            precio=200
            return mes, precio
    except TypeError:
        print("Solo se permiten números entreos.")
        print("Se cancela la operación")
    except ValueError:
        print("La opción tienen que estar entre 1 y 4.")
        print("Se cancela la operación")


def listar_caducidad_proximos_dias(listado_abonos):
    lista = []
    hoy = datetime.now()
    tope = hoy + timedelta(days=10)
    for abono in listado_abonos:
        if abono.fechaFinal >= hoy and abono.fechaFinal <= tope:
            lista.append(abono)
    print(f"El número de abonos que caducan en los próximos 10 días son: {len(lista)}")
    if len(lista) > 0:
        print("Los abonos que caducan son los siguinetes: ")
        for abono in lista:
            print(f"El abono perteneciente a {abono.cliente.nombre} {abono.cliente.apellidos}, "
            f"con una duración de {abono.meses} mes/es, emitido el {abono.fechaInicial.strftime('%d-%m-%Y')} "
            f"para el vehículo con matrícula {abono.cliente.vehiculo.matricula}")

def listar_caducidad_mes(listado_abonos):
    lista = []
    try:
        mesComprobar = int(input('Introduzca el mes a comprobar en numeros, p. ej. 1, 11: '))
        anioComprobar = int(input('Introduzca el año a comprobar, p. ej. 2004, 1999: '))
        if not type(mesComprobar) is int:
                raise TypeError
        if mesComprobar > 12 and mesComprobar < 1:
            raise ValueError
        if not type(anioComprobar) is int:
            raise TypeError
        for abono in listado_abonos:
            if abono.fechaFinal.month == mesComprobar and abono.fechaFinal.year == anioComprobar:
                lista.append(abono)
        print(f"El número de abonos que caducan en el mes y año indicado son: {len(lista)}")
        if len(lista) > 0:
            print("Los abonos que caducan son los siguinetes: ")
            for abono in lista:
                print(f"El abono perteneciente a {abono.cliente.nombre} {abono.cliente.apellidos}, "
                      f"con una duración de {abono.meses} mes/es, emitido el {abono.fechaInicial.strftime('%d-%m-%Y')} "
                      f"para el vehículo con matrícula {abono.cliente.vehiculo.matricula}")
    except TypeError:
        print("Solo se permiten números entreos.")
        print("Se cancela la operación")
    except ValueError:
        print("La opción del mes tiene que estar entre 1 y 12.")
        print("Se cancela la operación")

def renovar_abono(listado_abonos,listado_facturas, dni):
    abono = search_by_dni(listado_abonos, dni)
    mes, precio = tipo_abono()
    abono.fechaFinal= (datetime.now() + datedelta.datedelta(months=mes))
    abono.meses=mes
    abono.precio=precio
    factura = Factura(datetime.now(), abono.cliente, precio)
    fact_serv.add(listado_facturas, factura)







