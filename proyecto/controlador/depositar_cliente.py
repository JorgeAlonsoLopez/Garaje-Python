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

matr=tk.StringVar()
ticketInf=tk.StringVar()
v=tk.IntVar()
park = tk.StringVar()
park.set(park_serv.mostrar_info_gen(parking))
ticket = None

def reservar():
    res =""
    tick=None
    if (v.get() == 1 or v.get() == 2 or v.get() == 3) and matr.get() != "":
        res, tick = park_serv.depositar_vehiculo(matr.get().upper(),v.get(),lista_tickets,parking)
        if tick != None:
            ticket = tick
            boton1 = tk.Button(frame_tick, text="Descargar ticket", font=LARGE_FONT, command=lambda :infoTick(ticket)).pack(pady=20)
            tick_serv.save_file(lista_tickets)
            park_serv.save_file(parking)
        else:
            ticketInf.set(res)

def infoTick(ticket):

    fileName = 'Ticket_ingreso.pdf'
    documentTitle = 'Ticket de deposito'
    title = 'TICKET'


    if ticket.coste != 0:
        textLines = [
            f"Matrícula del vehículo: {ticket.matricula}",
            "",
            f"Plaza del parking: {ticket.plaza.nombre}",
            "",
            f"Fecha y hora de estacionamiento: ",
            f"{ticket.fechaEntrada.strftime('%d-%m-%Y  %H:%M:%S')}",
            "",
            f"PIN: {ticket.pin}",
            "",
            f"Coste: {ticket.coste} €",
            "",
            f"Cambio: {ticket.cambio} €",
            "",
            f"Fecha y hora de salida: ",
            f"{ticket.fechaSalida.strftime('%d-%m-%Y  %H:%M:%S')}",
            "",
            "Gracias por usar nuestros servicios"
        ]
    else:
        textLines = [
            f"Matrícula del vehículo: {ticket.matricula}",
            "",
            f"Plaza del parking: {ticket.plaza.nombre}",
            "",
            f"Fecha y hora de estacionamiento: ",
            f"{ticket.fechaEntrada.strftime('%d-%m-%Y  %H:%M:%S')}",
            "",
            f"PIN: {ticket.pin}",
            "",
            "Gracias por usar nuestros servicios"
        ]


    from reportlab.pdfgen import canvas

    path = os.path.expanduser("~/Desktop")
    pdf = canvas.Canvas(f"{path}/"+fileName)
    pdf.setTitle(documentTitle)
    pdf.setAuthor("Jorge Alonso")


    pdf.drawCentredString(300, 770, title)

    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier", 14)

    from reportlab.lib import colors

    text = pdf.beginText(120, 680)
    text.setFont("Courier", 12)
    text.setFillColor(colors.black)
    for line in textLines:
        text.textLine(line)

    pdf.drawText(text)

    pdf.save()




label_tex = tk.Label(root, text="Plazas libres:", font=NEGRITA).pack(pady=20)

label_tex = tk.Label(root, textvariable=park, font=LARGE_FONT).pack(pady=5)

label_tex = tk.Label(root, text="Inserte la matrícula del vehículo y su tipo", font=NEGRITA).pack(pady=20)

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

frame_tick=tk.Frame(root)
frame_tick.pack(pady=20)

boton2 = tk.Button(root, text="Salir", font=LARGE_FONT, command=lambda: redirecc(root, "inicio")).pack(pady=30)

root.mainloop()
