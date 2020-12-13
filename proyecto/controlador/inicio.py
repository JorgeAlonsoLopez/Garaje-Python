import tkinter as tk
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



matr=tk.StringVar()
plz=tk.StringVar()
pin=tk.StringVar()
ticketInf=tk.StringVar()
v=tk.IntVar()
fail = tk.StringVar()
exito = tk.StringVar()
fin = False
pago = False
precio_mostrar=tk.StringVar()
dinero = tk.IntVar()


#exito.set("El vehículo se ha retirado con éxito.\nGracias por usar nuestros servicios.")

def calculo(pago, fail, precio_mostrar):
    if plz.get() != "" and matr.get() != "" and pin.get() != "":
        plaza = park_serv.search_plaza_by_name(parking, plz.get().upper())
        tick = tick_serv.search_by_matricula(lista_tickets, matr.get().upper())
        if plaza != None and tick != None and tick.pin == int(pin.get()):
            fail.set("")
            actual=datetime.now()
            min=(ceil((actual-tick.fechaEntrada).total_seconds()/60))
            precio = min * plaza.coste
            precio_mostrar.set("El coste es:(€)\n"+str(round(precio,2)))
        else:
            fail.set("No se puede proceder con los datos aprotados, inténtelo de nuevo.")
    else:
        fail.set("No se puede proceder con los datos aprotados, inténtelo de nuevo.")

def retirar():
    if plz.get() != "" and matr.get() != "" and pin.get() != "":
        plaza = park_serv.search_plaza_by_name(parking, plz.get().upper())
        tick = tick_serv.search_by_matricula(lista_tickets, matr.get().upper())

        if plaza != None and tick != None and dinero.get() >= 0:

            ok = tick_serv.pagar_ticket(plz.get().upper(),parking,tick, dinero.get())
            if ok:
                park_serv.retirar_vehiculo(matr.get().upper(),plz.get().upper(),int(pin.get()),parking,lista_tickets)
                ticketInf.set(tick_serv.pintar_ticket(tick))
            else:
                ticketInf.set("La cantidad insertada no es suficiente")


def pagar(pago, tick, plaz):
    pago = True



label_tex = tk.Label(root, text="Inserte la matrícula del vehículo, el nombre de la plaza y pin", font=LARGE_FONT).pack(pady=20)

""""
label_tex = tk.Label(root, text="Tipo", font=LARGE_FONT).pack(pady=5)

frame_opt=tk.Frame(root)
frame_opt.pack(pady=20)

tk.Radiobutton(frame_opt, text="Coche", variable=v, value=1).pack(side=tk.LEFT, padx = 20)
tk.Radiobutton(frame_opt, text="Moto", variable=v, value=2).pack(side=tk.LEFT, padx = 20)
tk.Radiobutton(frame_opt, text="Movilidad reducida",variable=v, value=3).pack(side=tk.LEFT, padx = 20)
"""

label_tex = tk.Label(root, text="Matrícula", font=LARGE_FONT).pack(pady=10)

cuadro = tk.Entry(root, textvariable=matr).pack(padx=5)

label_tex = tk.Label(root, text="Nombre de la plaza", font=LARGE_FONT).pack(pady=10)

cuadro = tk.Entry(root, textvariable=plz).pack(padx=5)

label_tex = tk.Label(root, text="PIN", font=LARGE_FONT).pack(pady=10)

cuadro = tk.Entry(root, textvariable=pin).pack(padx=5)

boton1 = tk.Button(root, text="Calcular precio", font=LARGE_FONT, command=lambda :calculo(pago, fail, precio_mostrar)).pack(pady=5)

label_tex = tk.Label(root, textvariable=fail, font=LARGE_FONT).pack()

label_tex = tk.Label(root, textvariable=exito, font=LARGE_FONT).pack()

label_tex = tk.Label(root, textvariable=precio_mostrar, font=LARGE_FONT).pack(pady=5)
label_tex = tk.Label(root, text="Inserte la cantidad establecida (no se admiten céntimos)", font=LARGE_FONT).pack(pady=10)
cuadro = tk.Entry(root, textvariable=dinero).pack(padx=5)
boton2 = tk.Button(root, text="Confirmar la retirada", font=LARGE_FONT, command=retirar).pack(pady=20)

label_tex = tk.Label(root, textvariable=ticketInf, font=LARGE_FONT).pack(pady=5)

boton2 = tk.Button(root, text="Salir", font=LARGE_FONT).pack(pady=10)


root.mainloop()
