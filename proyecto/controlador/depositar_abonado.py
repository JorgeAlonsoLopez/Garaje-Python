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
# Configuración de la raíz
root = tk.Tk()
root.geometry("900x800")

def redirecc(root, nombre):
    root.destroy()
    os.system(f'python controlador/{nombre}.py')


matr=tk.StringVar()
dni=tk.StringVar()
res=tk.StringVar()

def reservar(res):
    resp =""

    if dni.get() != "" and matr.get() != "":
        resp = park_serv.depositar_vehiculo_abonado(dni.get().upper(), matr.get().upper(), lista_abonos, parking)
        res.set(resp)
        abon_serv.save_file(lista_abonos)
        park_serv.save_file(parking)
    else:
        res.set("Los campos debes estar rellenos")

label_tex = tk.Label(root, text="Inserte la matrícula del vehículo y su DNI", font=LARGE_FONT).pack(pady=20)

frame1=tk.Frame(root)
frame1.pack(pady=20)

label_tex = tk.Label(frame1, text="Matrícula", font=LARGE_FONT).pack(pady=10, side=tk.LEFT)
cuadro = tk.Entry(frame1, textvariable=matr).pack(padx=5, side=tk.LEFT)
label_tex = tk.Label(frame1, text="DNI", font=LARGE_FONT).pack(pady=10, side=tk.LEFT)
cuadro = tk.Entry(frame1, textvariable=dni).pack(padx=5, side=tk.LEFT)

boton1 = tk.Button(root, text="Confirmar el deposito", font=LARGE_FONT, command= lambda :reservar(res)).pack(pady=20)

label_tex = tk.Label(root, textvariable=res, font=LARGE_FONT).pack()


boton2 = tk.Button(root, text="Salir", font=LARGE_FONT, command=lambda: redirecc(root, "inicio")).pack(pady=50)

root.mainloop()
