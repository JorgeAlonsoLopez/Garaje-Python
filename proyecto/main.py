import sys
import os
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

LARGE_FONT= ("Verdana", 10)
NEGRITA= ("Verdana", 12, "bold")
TITULO= ("Verdana", 15, "bold")
PASSW = "1234"
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Ingrs_clien, Ingrs_abon, Opcion_admin, Retir_abon, Retir_client):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Bienvenido a AppGarage, ¿qué desea hacer?", font=TITULO)
        label.pack(pady=20)

        frame_clien=tk.Frame(self)
        frame_clien.pack(pady=20)
        frame_admin=tk.Frame(self)
        frame_admin.pack(pady=20)

        label_tex_cli = tk.Label(frame_clien, text="Zona de clienes", font=NEGRITA)
        label_tex_cli.pack()

        button_ing_cli = tk.Button(frame_clien, text="Depositar vehículo",
                            command=lambda: controller.show_frame(Ingrs_clien))
        button_ret_cli = tk.Button(frame_clien, text="Retirar vehículo",
                            command=lambda: controller.show_frame(Retir_client))
        button_ing_abo = tk.Button(frame_clien, text="Depositar vehículo (abonado)",
                            command=lambda: controller.show_frame(Ingrs_abon))
        button_ret_abo = tk.Button(frame_clien, text="Retirar vehículo (abonado)",
                            command=lambda: controller.show_frame(Retir_abon))
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
                return controller.show_frame(Opcion_admin)
            else:
                return controller.show_frame(StartPage)

        button2 = tk.Button(frame_admin, text="Comprobar",
                            command=comprobar_contr)
        button2.pack(padx=5, pady=20)


class Ingrs_clien(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        matr=tk.StringVar()
        ticketInf=tk.StringVar()
        v=tk.IntVar()
        park = tk.StringVar()
        park.set(park_serv.mostrar_info_gen(parking))

        def reservar():
            res =""
            tick=None
            if (v.get() == 1 or v.get() == 2 or v.get() == 3) and matr.get() != "":
                res, tick = park_serv.depositar_vehiculo(matr.get().upper(),v.get(),lista_tickets,parking)
                if tick != None:
                    ticketInf.set(tick_serv.pintar_ticket(tick))
                    tick_serv.save_file(lista_tickets)
                    park_serv.save_file(parking)
                else:
                    ticketInf.set(res)

        label_tex = tk.Label(self, text="Plazas libres:", font=LARGE_FONT).pack(pady=20)

        label_tex = tk.Label(self, textvariable=park, font=LARGE_FONT).pack(pady=5)

        label_tex = tk.Label(self, text="Inserte la matrícula del vehículo y su tipo", font=LARGE_FONT).pack(pady=20)

        label_tex = tk.Label(self, text="Tipo", font=LARGE_FONT).pack(pady=5)

        frame_opt=tk.Frame(self)
        frame_opt.pack(pady=20)

        tk.Radiobutton(frame_opt, text="Coche", variable=v, value=1).pack(side=tk.LEFT, padx = 20)
        tk.Radiobutton(frame_opt, text="Moto", variable=v, value=2).pack(side=tk.LEFT, padx = 20)
        tk.Radiobutton(frame_opt, text="Movilidad reducida",variable=v, value=3).pack(side=tk.LEFT, padx = 20)

        label_tex = tk.Label(self, text="Matrícula", font=LARGE_FONT).pack(pady=10)

        cuadro = tk.Entry(self, textvariable=matr).pack(padx=5)

        label_tex = tk.Label(self, text="Por favor, acuerdese del nombre de la plaza y del pin para poder "
                                            "sacar su vehículo posteriormente", font=LARGE_FONT).pack(pady=10)

        boton1 = tk.Button(self, text="Confirmar el deposito", font=LARGE_FONT, command=reservar).pack(pady=20)

        label_tex = tk.Label(self, textvariable=ticketInf, font=LARGE_FONT).pack(pady=5)

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=30)



class Ingrs_abon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()


class Retir_client(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        matr=tk.StringVar()
        plz=tk.StringVar()
        pin=tk.StringVar()
        ticketInf=tk.StringVar()
        fail = tk.StringVar()
        exito = tk.StringVar()
        pago = False
        precio_mostrar=tk.StringVar()
        dinero = tk.IntVar()

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
                        tick_serv.save_file(lista_tickets)
                        park_serv.save_file(parking)
                    else:
                        ticketInf.set("La cantidad insertada no es suficiente")


        label_tex = tk.Label(self, text="Inserte la matrícula del vehículo, el nombre de la plaza y pin", font=LARGE_FONT).pack(pady=20)

        label_tex = tk.Label(self, text="Matrícula", font=LARGE_FONT).pack(pady=10)

        cuadro = tk.Entry(self, textvariable=matr).pack(padx=5)

        label_tex = tk.Label(self, text="Nombre de la plaza", font=LARGE_FONT).pack(pady=10)

        cuadro = tk.Entry(self, textvariable=plz).pack(padx=5)

        label_tex = tk.Label(self, text="PIN", font=LARGE_FONT).pack(pady=10)

        cuadro = tk.Entry(self, textvariable=pin).pack(padx=5)

        boton1 = tk.Button(self, text="Calcular precio", font=LARGE_FONT, command=lambda :calculo(pago, fail, precio_mostrar)).pack(pady=5)

        label_tex = tk.Label(self, textvariable=fail, font=LARGE_FONT).pack()

        label_tex = tk.Label(self, textvariable=exito, font=LARGE_FONT).pack()

        label_tex = tk.Label(self, textvariable=precio_mostrar, font=LARGE_FONT).pack(pady=5)
        label_tex = tk.Label(self, text="Inserte la cantidad establecida (no se admiten céntimos)", font=LARGE_FONT).pack(pady=10)
        cuadro = tk.Entry(self, textvariable=dinero).pack(padx=5)
        boton2 = tk.Button(self, text="Confirmar la retirada", font=LARGE_FONT, command=retirar).pack(pady=20)

        label_tex = tk.Label(self, textvariable=ticketInf, font=LARGE_FONT).pack(pady=5)

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=10)



class Retir_abon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()

class Opcion_admin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()























class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page Two",
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()




app = SeaofBTCapp()
app.wm_geometry("900x800")
app.mainloop()
