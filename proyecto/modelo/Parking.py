from .PlazaCoche import PlazaCoche
from .PlazaMoto import PlazaMoto
from .PlazaMin import PlazaMin

class Parking():

    def __init__(self):
        self.__listaCoches = [PlazaCoche(("PC-" + str(numero) ), 0.12) for numero in range(1,29)]
        self.__listaMotos = [PlazaMoto(("PM-" + str(numero) ), 0.08) for numero in range(29,35)]
        self.__listaMoviReduc = [PlazaMin(("PR-" + str(numero) ), 0.10) for numero in range(35,41)]

    @property
    def listaCoches(self):
        return self.__listaCoches

    @listaCoches.setter
    def listaCoches(self, listaCoches):
        self.__listaCoches = listaCoches

    @property
    def listaMotos(self):
        return self.__listaMotos

    @listaMotos.setter
    def listaMotos(self, listaMotos):
        self.__listaMotos = listaMotos

    @property
    def listaMoviReduc(self):
        return self.__listaMoviReduc

    @listaMoviReduc.setter
    def listaMoviReduc(self, listaMoviReduc):
        self.__listaMoviReduc = listaMoviReduc
