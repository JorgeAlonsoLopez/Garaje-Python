import tkinter as tk
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
root.geometry("900x700")



matr=tk.StringVar()
ticketInf=tk.StringVar()
v=tk.IntVar()

def reservar():
    res =""
    tick=None
    if (v.get() == 1 or v.get() == 2 or v.get() == 3) and matr.get() != "":
        res, tick = park_serv.depositar_vehiculo(matr.get().upper(),v.get(),lista_tickets,parking)
        if tick != None:
            ticketInf.set(tick_serv.pintar_ticket(tick))
        else:
            ticketInf.set(res)

label_tex = tk.Label(root, text="Plazas libres:", font=LARGE_FONT).pack(pady=20)

label_tex = tk.Label(root, text=park_serv.mostrar_info_gen(parking), font=LARGE_FONT).pack(pady=5)

label_tex = tk.Label(root, text="Inserte la matrícula del vehículo y su tipo", font=LARGE_FONT).pack(pady=20)

label_tex = tk.Label(root, text="Tipo", font=LARGE_FONT).pack(pady=5)

frame_opt=tk.Frame(root)
frame_opt.pack(pady=20)

tk.Radiobutton(frame_opt, text="Coche", variable=v, value=1).pack(side=tk.LEFT, padx = 20)
tk.Radiobutton(frame_opt, text="Moto", variable=v, value=2).pack(side=tk.LEFT, padx = 20)
tk.Radiobutton(frame_opt, text="Movilidad reducida",variable=v, value=3).pack(side=tk.LEFT, padx = 20)

label_tex = tk.Label(root, text="Matrícula", font=LARGE_FONT).pack(pady=10)

cuadro = tk.Entry(root, textvariable=matr).pack(padx=5)

label_tex = tk.Label(root, text="Por favor, acuerdese del nombre de la plaza y del pin para poder "
                                    "sacar su vehículo posteriormente", font=LARGE_FONT).pack(pady=10)

boton1 = tk.Button(root, text="Confirmar el deposito", font=LARGE_FONT, command=reservar).pack(pady=20)

label_tex = tk.Label(root, textvariable=ticketInf, font=LARGE_FONT).pack(pady=5)


boton2 = tk.Button(root, text="Salir", font=LARGE_FONT).pack(pady=30)


root.mainloop()
