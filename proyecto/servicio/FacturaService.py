import repositorio.FacturaRepository as repo

def add(listado_facturas, factura):
    return repo.add(listado_facturas, factura)

def remove(listado_facturas, factura):
    return repo.remove(listado_facturas, factura)

def search_by_dni(listado_facturas, dni):
    return repo.search_by_dni(listado_facturas, dni)

def search_by_year(listado_facturas, year):
     return repo.search_by_year(listado_facturas, year)

def save_file(listado_facturas):
    return repo.save_file(listado_facturas)

def load_file():
    return repo.load_file()


def facturacion_anyo(lista_facturas, year):
    lista = repo.search_by_year(lista_facturas, year)
    contd = 0
    recaudac = 0
    if len(lista) > 0:
        for factura in lista:
            contd += 1
            recaudac += factura.coste
        recaudac = format(recaudac, ".2f")
        print(f"Ha habido en el año seleccionado ({year}), un total de {contd}"
              f" cobros de abonos por un valor de {recaudac} + €.")
    else:
        print("No se ha encontrado ningún pago de abono perteneciente al año insertado")

