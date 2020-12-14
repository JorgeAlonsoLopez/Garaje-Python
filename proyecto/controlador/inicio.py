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
lista_abonos = abon_serv.load_file()
lista_tickets = tick_serv.load_file()
lista_facturas = fact_serv.load_file()
parking = park_serv.load_file()


import servicio.AbonoService as serv_abo
LARGE_FONT= ("Verdana", 10)
# Configuración de la raíz
root = tk.Tk()
root.geometry("900x800")



anyo = tk.StringVar()
sol = tk.StringVar()

def calculo(sol, anyo):
    total = fact_serv.facturacion_anyo(lista_facturas,anyo.get())
    sol.set(total)

label_tex = tk.Label(root, text="Seleccione el año por el que va a buscar la facturación de los abonados", font=LARGE_FONT).pack(pady=20)

cuadro = tk.Entry(root, textvariable=anyo).pack(padx=5)


botonFec1 = tk.Button(root, text="Obtener facturación",command= lambda : calculo(sol, anyo), font=LARGE_FONT).pack(pady=30)

label_tex = tk.Label(root, textvariable=sol, font=LARGE_FONT).pack()



boton2 = tk.Button(root, text="Salir", font=LARGE_FONT).pack(pady=30)

root.mainloop()
