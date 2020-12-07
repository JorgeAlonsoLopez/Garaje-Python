import pickle
from datetime import datetime

def add(lista, factura):
    return lista.append(factura)

def remove(lista, factura):
    if factura in lista:
        lista.remove(factura)

def searchByDni(lista, dni):
    result = list(filter(lambda factura: factura.cliente.dni == dni, lista))
    if len(result) == 1:
        return result[0]
    else:
        return None

def searchByYear(lista, year):
    result = list(filter(lambda factura: factura.fecha.year == year, lista))
    if len(result) >= 1:
        return result
    else:
        return None


def saveFile(lista):
    fichero = open('listaFacturas.pckl','wb')
    pickle.dump(lista, fichero)
    fichero.close()

def loadFile():
    lista = []
    try:
        fichero = open('listaFacturas.pckl','rb')
        lista = pickle.load(fichero)
        fichero.close()
    except (OSError, IOError) as e:
        fichero = open('listaFacturas.pckl', 'wb')
        pickle.dump(lista, fichero)
        fichero.close()
    return lista
