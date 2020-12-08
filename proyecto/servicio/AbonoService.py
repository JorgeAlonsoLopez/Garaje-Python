import repositorio.AbonoRepository as repo
from datetime import datetime
from datetime import timedelta
from modelo.Factura import *
import servicio.FacturaService as fact_serv

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

def caducidad_proximos_dias(listado_abonos):
    lista = []
    hoy = datetime.now()
    tope = hoy + timedelta(days=10)
    for abono in listado_abonos:
        if abono.fechaFinal >= hoy and abono.fechaFinal <= tope:
            lista.append(abono)
    return lista

def renovar_abono(listado_abonos,listado_facturas, dni, opt):
    abono = search_by_dni(listado_abonos, dni)
    if opt == 1:
        abono.fechaFinal(abono.fechaFinal + timedelta(months=1))
        abono.meses=1
        abono.precio=25
        factura = Factura(datetime.now(), abono.cliente, 25)
        fact_serv.add(listado_facturas, factura)
    elif opt == 2:
        abono.fechaFinal(abono.fechaFinal + timedelta(months=3))
        abono.meses =3
        abono.precio=70
        factura = Factura(datetime.now(), abono.cliente, 70)
        fact_serv.add(listado_facturas, factura)
    elif opt == 3:
        abono.fechaFinal(abono.fechaFinal + timedelta(months=6))
        abono.meses=6
        abono.precio=130
        factura = Factura(datetime.now(), abono.cliente, 130)
        fact_serv.add(listado_facturas, factura)
    elif opt == 4:
        abono.fechaFinal(abono.fechaFinal + timedelta(months=12))
        abono.meses=12
        abono.precio=200
        factura = Factura(datetime.now(), abono.cliente, 200)
        fact_serv.add(listado_facturas, factura)






