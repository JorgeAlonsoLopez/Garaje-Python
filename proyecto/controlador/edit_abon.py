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
dni = tk.StringVar()
nom = tk.StringVar()
apl = tk.StringVar()
taj = tk.StringVar()
mail = tk.StringVar()


def renov(sol):
    if dni.get() != "" and nom.get() != "" and apl.get() != "" and taj.get() != "" and mail.get() != "":
        res = abon_serv.modificar_abonado(lista_abonos, dni.get().upper(), nom.get(), apl.get(), taj.get(), mail.get())
        sol.set(res)
        abon_serv.save_file(lista_abonos)
    else:
        sol.set("Todos los campos deben estar rellenos")

label_tex = tk.Label(root, text="Inserte el DNI del abonado en cuestión y los datos a modificar", font=NEGRITA).pack(pady=10)


frame_1=tk.Frame(root)
frame_1.pack(pady=5)

label_tex = tk.Label(frame_1, text="DNI ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
Inp_dni = tk.Entry(frame_1, textvariable=dni).pack(padx=5, pady=15, side=tk.LEFT)


frame_1=tk.Frame(root)
frame_1.pack(pady=5)

label_tex = tk.Label(frame_1, text="Nombre ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
Inp_nom = tk.Entry(frame_1, textvariable=nom).pack(padx=5, pady=15, side=tk.LEFT)
label_tex = tk.Label(frame_1, text="Apellidos ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
Inp_ape = tk.Entry(frame_1, textvariable=apl).pack(padx=5, pady=15, side=tk.LEFT)

frame_2=tk.Frame(root)
frame_2.pack(pady=5)

label_tex = tk.Label(frame_2, text="Nº tarjeta ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
Inp_tarj = tk.Entry(frame_2, textvariable=taj).pack(padx=5, pady=15, side=tk.LEFT)
label_tex = tk.Label(frame_2, text="Correo ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
Inp_mail = tk.Entry(frame_2, textvariable=mail).pack(padx=5, pady=15, side=tk.LEFT)

boton = tk.Button(root, text="Confrimar datos del abonado",command= lambda : renov(sol), font=LARGE_FONT).pack(pady=20)

label_tex = tk.Label(root, textvariable=sol, font=LARGE_FONT).pack()

boton2 = tk.Button(root, text="Volver a la zona de administración", font=LARGE_FONT, command=lambda: redirecc(root, "admin")).pack(pady=10)

root.mainloop()
