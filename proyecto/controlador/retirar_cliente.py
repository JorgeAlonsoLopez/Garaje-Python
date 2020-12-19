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
plz=tk.StringVar()
pin=tk.StringVar()
ticketInf=tk.StringVar()
fail = tk.StringVar()
exito = tk.StringVar()
pago = False
precio_mostrar=tk.StringVar()
dinero = tk.IntVar()
ticket = None

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
                ticket = tick
                boton1 = tk.Button(frame_tick, text="Descargar ticket", font=LARGE_FONT, command=lambda :infoTick(ticket)).pack(pady=20)
                tick_serv.save_file(lista_tickets)
                park_serv.save_file(parking)
            else:
                ticketInf.set("La cantidad insertada no es suficiente")


def infoTick(ticket):

    fileName = 'Ticket_retirada.pdf'
    documentTitle = 'Ticket de retirada'
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

    pdf = canvas.Canvas("../"+fileName)
    pdf.setTitle(documentTitle)
    pdf.setAuthor("Jorge Alosno")

    pdf.drawCentredString(300, 770, title)

    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier", 14)

    from reportlab.lib import colors

    text = pdf.beginText(120, 680)
    text.setFont("Courier", 16)
    text.setFillColor(colors.black)
    for line in textLines:
        text.textLine(line)

    pdf.drawText(text)

    pdf.save()




label_tex = tk.Label(root, text="Inserte la matrícula del vehículo, el nombre de la plaza y pin", font=NEGRITA).pack(pady=20)

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

frame_tick=tk.Frame(root)
frame_tick.pack(pady=20)


boton2 = tk.Button(root, text="Salir", font=LARGE_FONT, command=lambda: redirecc(root, "inicio")).pack(pady=10)

root.mainloop()
