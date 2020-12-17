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

label = tk.Label(root, text="Bienvenido a la zona de administración", font=LARGE_FONT).pack(pady=20)

frame_0=tk.Frame(root)
frame_0.pack(pady=5)
frame_1=tk.Frame(root)
frame_1.pack(pady=5)
frame_2=tk.Frame(root)
frame_2.pack(pady=5)
frame_3=tk.Frame(root)
frame_3.pack(pady=5)


label_tex_cli1 = tk.Label(frame_0, text="Estado del parking", font=LARGE_FONT).pack(pady=15)

button_estado_park = tk.Button(frame_0, text="Comprobar el estado del parking", command=lambda: redirecc(root, "estado_park")).pack(padx=5, pady=5)


label_tex_cli2 = tk.Label(frame_1, text="Facturación y cobros", font=LARGE_FONT).pack(pady=15)

button_fact = tk.Button(frame_1, text="Facturación de tickets ",command=lambda: redirecc(root, "fact_tik")).pack(padx=5, pady=5, side=tk.LEFT)
button_cob_abon = tk.Button(frame_1, text="Cobros de abonados", command=lambda: redirecc(root, "cobro_abon")).pack(padx=5, pady=5, side=tk.LEFT)


label_tex_cli3 = tk.Label(frame_2, text="Consultar caducidad de abonos", font=LARGE_FONT).pack(pady=15)

button_caduc_anyo = tk.Button(frame_2, text="Año y mes determinados", command=lambda: redirecc(root, "caduc_anyo")).pack(padx=5, pady=5, side=tk.LEFT)
button_caduc_10 = tk.Button(frame_2, text="Próximos 10 días", command=lambda: redirecc(root, "caduc_dias")).pack(padx=5, pady=5, side=tk.LEFT)



label_tex_cli4 = tk.Label(frame_3, text="Gestión de abonos", font=LARGE_FONT).pack(pady=15)

button_new_ab = tk.Button(frame_3, text="Crear abono", command=lambda: redirecc(root, "nuevo_abon")).pack(padx=5, pady=5, side=tk.LEFT)
button_edit = tk.Button(frame_3, text="Editar datos del abonado", command=lambda: redirecc(root, "edit_abon")).pack(padx=5, pady=5, side=tk.LEFT)
button_renov = tk.Button(frame_3, text="Renovar abono", command=lambda:redirecc(root, "renov_abon")).pack(padx=5, pady=5, side=tk.LEFT)
button_delet = tk.Button(frame_3, text="Eliminar abono", command=lambda: redirecc(root, "elimn_abon")).pack(padx=5, pady=5, side=tk.LEFT)

boton2 = tk.Button(root, text="Salir", font=LARGE_FONT, command=lambda: redirecc(root, "inicio")).pack(pady=50)

root.mainloop()
