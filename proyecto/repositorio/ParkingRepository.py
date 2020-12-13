import pickle
from modelo.Parking import *

def search_plaza_by_name(parking, nombre):
    result = []
    if list(nombre)[1] == "C":
        result = list(filter(lambda plazaCoche: plazaCoche.nombre == nombre, parking.listaCoches))
    elif list(nombre)[1] == "M":
        result = list(filter(lambda PlazaMoto: PlazaMoto.nombre == nombre, parking.listaMotos))
    elif list(nombre)[1] == "R":
        result = list(filter(lambda PlazaMin: PlazaMin.nombre == nombre, parking.listaMoviReduc))

    if len(result) == 1:
        return result
    else:
        return None


def save_file(parking):
    fichero = open('parking.pckl','wb')
    pickle.dump(parking, fichero)
    fichero.close()

def load_file():
    parking = Parking()
    try:
        fichero = open('parking.pckl','rb')
        parking = pickle.load(fichero)
        fichero.close()
    except (OSError, IOError) as e:
        fichero = open('parking.pckl', 'wb')
        pickle.dump(parking, fichero)
        fichero.close()
    return parking
