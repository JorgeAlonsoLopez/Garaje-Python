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

hor = tk.StringVar()
min = tk.StringVar()
f1 = tk.StringVar()
f2 = tk.StringVar()
sol = tk.StringVar()
fail = tk.StringVar()
v=tk.IntVar()
res = tk.StringVar()
text=tk.StringVar()
today = datetime.today()


def fechas(err):
    fecha1= None
    fecha2=None

    try:
        if f1.get() != "" and f2.get() != "":
            anio1 = int(f1.get()[6:10])
            mes1= int(f1.get()[0:2])
            dia1= int(f1.get()[3:5])
            hor1= int(f1.get()[11:13])
            min1= int(f1.get()[14:16])
            if dia1 > 31 or dia1 < 1:
                raise ValueError
            if mes1 > 12 or mes1 < 1:
                raise ValueError
            if anio1 < 2019 :
                raise ValueError
            if hor1 > 23 or hor1 < 0:
                raise ValueError
            if min1 > 59 or min1 < 0:
                raise ValueError
            fecha1 = datetime(anio1, mes1, dia1, hor1, min1)
            anio2 = int(f2.get()[6:10])
            mes2= int(f2.get()[0:2])
            dia2= int(f2.get()[3:5])
            hor2= int(f2.get()[11:13])
            min2= int(f2.get()[14:16])
            if dia2 > 31 or dia2 < 1:
                raise ValueError
            if mes2 > 12 or mes2 < 1:
                raise ValueError
            if anio2 < 2019 :
                raise ValueError
            if hor2 > 23 or hor2 < 0:
                raise ValueError
            if min2 > 59 or min2 < 0:
                raise ValueError
            fecha2 = datetime(anio2, mes2, dia2, hor2, min2)
            fail.set("")
            err = False
        else:
            fail.set( "Tiene que completarse las dos fechas")
            err = True
    except ValueError:
        fail.set("Los datos tienen que ser enteros, para los meses tiene que estar entre 1 y 12 para los meses, de 1 a 31 para días,\n "
                 "de 0 a 11 para horas, de 0 a 59 para minutos y años superiores al 2019.")
        err = True

    return fecha1, fecha2, err

def calculo(err, sol):
    fecha1, fecha2, err = fechas(err)
    if not err:
        total, dinero = tick_serv.facturacion(lista_tickets, fecha1, fecha2)
        sol.set(f"Se han obtenido {dinero} €  entre las dos fechas por el cobro de {total} tichets")

label_tex = tk.Label(root, text="Establezca las dos fechas entre las que se a a buscar la facturación de los tickets\n"
                                "Para las horas y minutos, inserte dos números", font=NEGRITA).pack(pady=20)

frame_opt=tk.Frame(root)
frame_opt.pack(pady=20)

tk.Radiobutton(frame_opt, text="Fecha de inicio", variable=v, value=1).pack(side=tk.LEFT, padx = 10)
tk.Radiobutton(frame_opt, text="Fecha de fin", variable=v, value=2).pack(side=tk.LEFT, padx = 10)

cal1 = Calendar(root, selectmode="day",date_pattern='mm/dd/y', year=today.year, month=today.month, day=today.day)
cal1.pack(pady=20)

def fecha():
    if v.get()==1:
        f1.set(cal1.get_date()+"-"+hor.get()+":"+min.get())
    else:
        f2.set(cal1.get_date()+"-"+hor.get()+":"+min.get())

frame_1=tk.Frame(root)
frame_1.pack(pady=5)

label_tex = tk.Label(frame_1, text="Hora (24H) ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
Inp_h1 = tk.Entry(frame_1, textvariable=hor).pack(padx=5, pady=5, side=tk.LEFT)
label_tex = tk.Label(frame_1, text="Minutos ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
Inp_m1 = tk.Entry(frame_1, textvariable=min).pack(padx=5, pady=5, side=tk.LEFT)

botonFec1 = tk.Button(root, text="Confrimar fecha",command=fecha, font=LARGE_FONT).pack(pady=10)

frame_2=tk.Frame(root)
frame_2.pack(pady=5)
label_tex = tk.Label(frame_2, text="La fecha y hora de inicio es: ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
fech1 = tk.Label(frame_2, textvariable=f1)
fech1.pack(side=tk.LEFT)

frame_3=tk.Frame(root)
frame_3.pack(pady=5)
label_tex = tk.Label(frame_3, text="La fecha y hora de fin es: ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
fech2 = tk.Label(frame_3, textvariable=f2)
fech2.pack(side=tk.LEFT)

botonFec1 = tk.Button(root, text="Obtener facturación",command= lambda : calculo(fail, sol), font=LARGE_FONT).pack(pady=10)

label_tex = tk.Label(root, textvariable=fail, font=LARGE_FONT).pack()

label_tex = tk.Label(root, textvariable=sol, font=LARGE_FONT).pack()

boton2 = tk.Button(root, text="Volver a la zona de administración", font=LARGE_FONT, command=lambda: redirecc(root, "admin")).pack(pady=10)

root.mainloop()
