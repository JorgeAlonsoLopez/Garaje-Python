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

label_tex_cli4 = tk.Label(root, text="Información detallada del parking", font=NEGRITA).pack(pady=15)

canvas = tk.Canvas(root)
canvas.pack(fill="both", expand="yes", padx=10, pady=10)

scroll_bar = ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
scroll_bar.pack(side=tk.RIGHT, fill="y")

canvas.configure(yscrollcommand=scroll_bar.set)

canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

main_frame = tk.Frame(canvas)

canvas.create_window((0,0), window=main_frame, anchor="nw")

plz=tk.StringVar()
plz.set(park_serv.mostrar_info_detll(parking))



label_tex = tk.Label(main_frame, textvariable=plz, font=LARGE_FONT).pack(pady=5)


boton2 = tk.Button(root, text="Volver a la zona de administración", font=LARGE_FONT, command=lambda: redirecc(root, "admin")).pack(pady=10)

root.mainloop()
