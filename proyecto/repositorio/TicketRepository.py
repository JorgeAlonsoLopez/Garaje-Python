import pickle

def add(lista, ticket):
    return lista.append(ticket)

def remove(lista, ticket):
    if ticket in lista:
        lista.remove(ticket)

def search_by_matricula(lista, matricula):
    result = list(filter(lambda ticket: ticket.matricula == matricula, search_pendi(lista)))
    if len(result) == 1:
        return result[0]
    else:
        return None

def search_pendi(lista):
    result = list(filter(lambda ticket: ticket.coste == 0, lista))
    if len(result) >= 1:
        return result
    else:
        return None


def save_file(lista):
    fichero = open('listaTickets.pckl','wb')
    pickle.dump(lista, fichero)
    fichero.close()

def load_file():
    lista = []
    try:
        fichero = open('listaTickets.pckl','rb')
        lista = pickle.load(fichero)
        fichero.close()
    except (OSError, IOError) as e:
        fichero = open('listaTickets.pckl', 'wb')
        pickle.dump(lista, fichero)
        fichero.close()
    return lista
