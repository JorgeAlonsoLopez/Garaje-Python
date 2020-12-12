import pickle

def add(lista, abono):
    return lista.append(abono)

def remove(lista, abono):
    if abono in lista:
        lista.remove(abono)

def search_by_dni(lista, dni):
    result = list(filter(lambda abono: abono.cliente.dni == dni, lista))
    if len(result) == 1:
        return result[0]
    else:
        return None

def search_by_nombre_plaza(lista, nombre_plaza):
    result = list(filter(lambda abono: abono.plaza.nombre == nombre_plaza, lista))
    if len(result) == 1:
        return result[0]
    else:
        return None

def save_file(lista):
    fichero = open('listaAbonos.pckl','wb')
    pickle.dump(lista, fichero)
    fichero.close()

def load_file():
    lista = []
    try:
        fichero = open('listaAbonos.pckl','rb')
        lista = pickle.load(fichero)
        fichero.close()
    except (OSError, IOError) as e:
        fichero = open('listaAbonos.pckl', 'wb')
        pickle.dump(lista, fichero)
        fichero.close()
    return lista
