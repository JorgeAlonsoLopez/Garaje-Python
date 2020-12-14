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


import servicio.AbonoService as serv_abo
LARGE_FONT= ("Verdana", 10)
# Configuración de la raíz
root = tk.Tk()
root.geometry("900x800")




sol = tk.StringVar()
dni = tk.StringVar()


def delet(sol):
    print("")
    if dni.get() != "":
        if abon_serv.search_by_dni(lista_abonos, dni.get().upper()) != None:
            abon_serv.remove(lista_abonos,abon_serv.search_by_dni(lista_abonos, dni.get().upper()))
            sol.set("La acción de borrado ha concluido satisfactoriamente")
            print("")
            #abon_serv.save_file(lista_abonos)
        else:
            sol.set("No nos consta un abono perteneciente a un cliente con ese DNI")
    else:
        sol.set("Debe proporcionarnos el DNI")

label_tex = tk.Label(root, text="Inserte el DNI del abonado en cuestión", font=LARGE_FONT).pack(pady=10)


frame_1=tk.Frame(root)
frame_1.pack(pady=5)

label_tex = tk.Label(frame_1, text="DNI ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
Inp_dni = tk.Entry(frame_1, textvariable=dni).pack(padx=5, pady=15, side=tk.LEFT)


boton = tk.Button(root, text="Confrimar aliminación del abonado",command= lambda : delet(sol), font=LARGE_FONT).pack(pady=20)

label_tex = tk.Label(root, textvariable=sol, font=LARGE_FONT).pack()



boton2 = tk.Button(root, text="Salir", font=LARGE_FONT).pack(pady=20)

root.mainloop()
