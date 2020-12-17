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


sol = tk.StringVar()
dni = tk.StringVar()
tip_abon = tk.IntVar()


def renov(sol):
    ok, resl = abon_serv.renovar_abono(lista_abonos,lista_facturas, dni.get().upper(), tip_abon.get())
    if ok:
        abon_serv.save_file(lista_abonos)
        fact_serv.save_file(lista_facturas)
    sol.set(resl)

label_tex = tk.Label(root, text="Inserte el DNI del abonado en cuestión y por cuanto desea renovarlo", font=LARGE_FONT).pack(pady=10)


frame_1=tk.Frame(root)
frame_1.pack(pady=5)

label_tex = tk.Label(frame_1, text="DNI ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
Inp_dni = tk.Entry(frame_1, textvariable=dni).pack(padx=5, pady=5, side=tk.LEFT)


label_tex = tk.Label(root, text="Tipo de abono", font=LARGE_FONT).pack(pady=5)

frame_opt_ab=tk.Frame(root)
frame_opt_ab.pack(pady=5)

tk.Radiobutton(frame_opt_ab, text="Mensual (25€)", variable=tip_abon, value=1).pack(side=tk.LEFT, padx = 5)
tk.Radiobutton(frame_opt_ab, text="Trimestral (70€)", variable=tip_abon, value=2).pack(side=tk.LEFT, padx = 5)
tk.Radiobutton(frame_opt_ab, text="Semestral (130€)",variable=tip_abon, value=3).pack(side=tk.LEFT, padx = 5)
tk.Radiobutton(frame_opt_ab, text="Anual (200€)",variable=tip_abon, value=4).pack(side=tk.LEFT, padx = 5)

boton = tk.Button(root, text="Confrimar renovación de abono",command= lambda : renov(sol), font=LARGE_FONT).pack(pady=5)

label_tex = tk.Label(root, textvariable=sol, font=LARGE_FONT).pack()

boton2 = tk.Button(root, text="Volver a la zona de administración", font=LARGE_FONT, command=lambda: redirecc(root, "admin")).pack(pady=10)

root.mainloop()
