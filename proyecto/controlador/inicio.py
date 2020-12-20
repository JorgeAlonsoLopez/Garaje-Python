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
TITULO= ("Verdana", 15, "bold")
PASSW = "1234"
# Configuración de la raíz
root = tk.Tk()
root.geometry("900x800")

def redirecc(root, nombre):
    root.destroy()
    os.system(f'python controlador/{nombre}.py')

label = tk.Label(root, text="Bienvenido a AppGarage, ¿qué desea hacer?", font=TITULO)
label.pack(pady=20)

frame_clien=tk.Frame(root)
frame_clien.pack(pady=20)
frame_admin=tk.Frame(root)
frame_admin.pack(pady=20)

label_tex_cli = tk.Label(frame_clien, text="Zona de clienes", font=NEGRITA)
label_tex_cli.pack()

button_ing_cli = tk.Button(frame_clien, text="Depositar vehículo",
                    command=lambda: redirecc(root, "depositar_cliente"))
button_ret_cli = tk.Button(frame_clien, text="Retirar vehículo",
                   command=lambda: redirecc(root, "retirar_cliente"))
button_ing_abo = tk.Button(frame_clien, text="Depositar vehículo (abonado)",
                    command=lambda: redirecc(root, "depositar_abonado"))
button_ret_abo = tk.Button(frame_clien, text="Retirar vehículo (abonado)",
                    command=lambda: redirecc(root, "retirar_abonado"))
button_ing_cli.pack(padx=5, pady=20, side=tk.LEFT)
button_ret_cli.pack(padx=5, pady=20, side=tk.LEFT)
button_ing_abo.pack(padx=5, pady=20, side=tk.LEFT)
button_ret_abo.pack(padx=5, pady=20, side=tk.LEFT)



label_tex_adm = tk.Label(frame_admin, text="Zona de administradores", font=NEGRITA)
label_tex_adm.pack()

label_tex_adm = tk.Label(frame_admin, text="Inserte la contraseña para acceder", font=LARGE_FONT)
label_tex_adm.pack(pady=10)

contr=tk.StringVar()
cuadro_pass = tk.Entry(frame_admin, textvariable=contr)
cuadro_pass.pack(padx=5, pady=20)

def comprobar_contr():
    if PASSW == contr.get():
        contr.set("")
        return redirecc(root, "admin")
    else:
        return redirecc(root, "inicio")

button2 = tk.Button(frame_admin, text="Acceder",
                    command=comprobar_contr)
button2.pack(padx=5, pady=20)


boton3 = tk.Button(root, text="Salir de la aplicación", font=LARGE_FONT, command=quit).pack(pady=30)




root.mainloop()
