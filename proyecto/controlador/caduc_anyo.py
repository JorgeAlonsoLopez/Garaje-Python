import tkinter as tk
from tkcalendar import *
from tkinter import ttk
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
import os

import servicio.AbonoService as serv_abo
LARGE_FONT= ("Verdana", 10)
NEGRITA= ("Verdana", 12, "bold")
# Configuración de la raíz
root = tk.Tk()
root.geometry("900x800")

def redirecc(root, nombre):
    root.destroy()
    os.system(f'python controlador/{nombre}.py')


sol = tk.StringVar()
fail = tk.StringVar()
f1 = tk.StringVar()
today = datetime.today()

def obt_fecha(lista_abonos):
    lista = []
    fallo = True
    faill=""
    soll=""
    fallo ,lista, faill, soll = abon_serv.obtener_lista_cad(lista_abonos,cal1.get_date()[0:2], cal1.get_date()[6:10])
    fail.set(faill)
    sol.set(soll)
    return fallo, lista

def consulta(sol):
    fallo, lista = obt_fecha(lista_abonos)
    res=""
    res = abon_serv.listar_caducidad_mes(fallo, lista)
    sol.set(res)

label_tex = tk.Label(root, text="Seleccione la fecha donde se encuentre el mes y año a consultar", font=LARGE_FONT).pack(pady=10)
def fecha():
    f1.set(cal1.get_date()[0:2] + " - " + cal1.get_date()[6:10])

cal1 = Calendar(root, selectmode="day",date_pattern='mm/dd/y', year=today.year, month=today.month, day=today.day)
cal1.pack(pady=20)

botonFec1 = tk.Button(root, text="Confrimar fecha",command=fecha, font=LARGE_FONT).pack(pady=10)
fech1 = tk.Label(root, textvariable=f1).pack()

boton = tk.Button(root, text="Consultar caducidad de abonos",command= lambda : consulta(sol), font=LARGE_FONT).pack(pady=20)

label_tex = tk.Label(root, textvariable=fail, font=LARGE_FONT).pack()

label_tex = tk.Label(root, textvariable=sol, font=LARGE_FONT).pack()

boton2 = tk.Button(root, text="Volver a la zona de administración", font=LARGE_FONT, command=lambda: redirecc(root, "admin")).pack(pady=10)

root.mainloop()
