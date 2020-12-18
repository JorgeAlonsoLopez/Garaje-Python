import sys
import os
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
from datetime import datetime
from math import ceil
from tkinter import messagebox
import servicio.ParkingService as park_serv
import servicio.AbonoService as abon_serv
import servicio.ClienteService as clin_serv
import servicio.TicketService as tick_serv
import servicio.FacturaService as fact_serv
from modelo.Parking import *
from modelo.Cliente import *
from modelo.Vehiculo import *
lista_abonos = abon_serv.load_file()
lista_tickets = tick_serv.load_file()
lista_facturas = fact_serv.load_file()
parking = park_serv.load_file()

LARGE_FONT= ("Verdana", 10)
NEGRITA= ("Verdana", 12, "bold")
TITULO= ("Verdana", 15, "bold")


os.system(f'python controlador/inicio.py')
