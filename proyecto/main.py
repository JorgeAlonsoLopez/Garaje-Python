import sys
import os
import tkinter as tk
from tkinter import ttk
from tkcalendar import *
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

LARGE_FONT= ("Verdana", 10)
NEGRITA= ("Verdana", 12, "bold")
TITULO= ("Verdana", 15, "bold")
PASSW = "1"
class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, Ingrs_clien, Ingrs_abon, Opcion_admin, Retir_abon, Retir_client, Estado_park, Fact_tik,
                  Cobro_abon, Caduc_anyo, Caduc_dias, Nuevo_abon, Edit_abon, Renov_abon, Elimn_abon):

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

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton3 = tk.Button(self, text="Salir de la aplicación", font=LARGE_FONT, command=quit).pack(pady=30)

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

        matr=tk.StringVar()
        dni=tk.StringVar()
        res=tk.StringVar()

        def reservar(res):
            resp =""

            if dni.get() != "" and matr.get() != "":
                resp = park_serv.depositar_vehiculo_abonado(dni.get().upper(), matr.get().upper(), lista_abonos, parking)
                res.set(resp)
                abon_serv.save_file(lista_abonos)
                park_serv.save_file(parking)
            else:
                res.set("Los campos debes estar rellenos")

        label_tex = tk.Label(self, text="Inserte la matrícula del vehículo y su DNI", font=LARGE_FONT).pack(pady=20)

        frame1=tk.Frame(self)
        frame1.pack(pady=20)

        label_tex = tk.Label(frame1, text="Matrícula", font=LARGE_FONT).pack(pady=10, side=tk.LEFT)
        cuadro = tk.Entry(frame1, textvariable=matr).pack(padx=5, side=tk.LEFT)
        label_tex = tk.Label(frame1, text="DNI", font=LARGE_FONT).pack(pady=10, side=tk.LEFT)
        cuadro = tk.Entry(frame1, textvariable=dni).pack(padx=5, side=tk.LEFT)

        boton1 = tk.Button(self, text="Confirmar el deposito", font=LARGE_FONT, command= lambda :reservar(res)).pack(pady=20)

        label_tex = tk.Label(self, textvariable=res, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=30)



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

        matr=tk.StringVar()
        plz=tk.StringVar()
        pin=tk.StringVar()
        res=tk.StringVar()

        def abandonar(res):
            resp =""
            try:
                if plz.get() != "" and matr.get() != "" and pin.get() != "":
                    resp = park_serv.retirar_vehiculo_abonado(matr.get().upper(), plz.get().upper(), lista_abonos, int(pin.get()), parking)
                    res.set(resp)
                    abon_serv.save_file(lista_abonos)
                    park_serv.save_file(parking)
                else:
                    res.set("Los campos debes estar rellenos")
            except ValueError:
                    res.set("Solo se permiten números enteros para el pin.")

        label_tex = tk.Label(self, text="Inserte la matrícula del vehículo, su pin y el nombre de la plaza", font=LARGE_FONT).pack(pady=20)

        frame1=tk.Frame(self)
        frame1.pack(pady=20)

        label_tex = tk.Label(frame1, text="Matrícula", font=LARGE_FONT).pack(pady=10, side=tk.LEFT)
        cuadro = tk.Entry(frame1, textvariable=matr).pack(padx=5, side=tk.LEFT)
        label_tex = tk.Label(frame1, text="Nombre de la plaza", font=LARGE_FONT).pack(pady=10, side=tk.LEFT)
        cuadro = tk.Entry(frame1, textvariable=plz).pack(padx=5, side=tk.LEFT)
        label_tex = tk.Label(frame1, text="Pin", font=LARGE_FONT).pack(pady=10, side=tk.LEFT)
        cuadro = tk.Entry(frame1, textvariable=pin).pack(padx=5, side=tk.LEFT)

        boton1 = tk.Button(self, text="Confirmar la retirada", font=LARGE_FONT, command= lambda :abandonar(res)).pack(pady=20)

        label_tex = tk.Label(self, textvariable=res, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=30)


class Opcion_admin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label = tk.Label(self, text="Bienvenido a la zona de administración", font=LARGE_FONT).pack(pady=20)

        frame_0=tk.Frame(self)
        frame_0.pack(pady=5)
        frame_1=tk.Frame(self)
        frame_1.pack(pady=5)
        frame_2=tk.Frame(self)
        frame_2.pack(pady=5)
        frame_3=tk.Frame(self)
        frame_3.pack(pady=5)


        label_tex_cli1 = tk.Label(frame_0, text="Estado del parking", font=LARGE_FONT).pack(pady=15)

        button_estado_park = tk.Button(frame_0, text="Comprobar el estado del parking", command=lambda: controller.show_frame(Estado_park))\
            .pack(padx=5, pady=5)


        label_tex_cli2 = tk.Label(frame_1, text="Facturación y cobros", font=LARGE_FONT).pack(pady=15)

        button_fact = tk.Button(frame_1, text="Facturación de tickets ",command=lambda: controller.show_frame(Fact_tik)).pack(padx=5, pady=5, side=tk.LEFT)
        button_cob_abon = tk.Button(frame_1, text="Cobros de abonados", command=lambda: controller.show_frame(Cobro_abon)).pack(padx=5, pady=5, side=tk.LEFT)


        label_tex_cli3 = tk.Label(frame_2, text="Consultar caducidad de abonos", font=LARGE_FONT).pack(pady=15)

        button_caduc_anyo = tk.Button(frame_2, text="Año y mes determinados", command=lambda: controller.show_frame(Caduc_anyo)).pack(padx=5, pady=5, side=tk.LEFT)
        button_caduc_10 = tk.Button(frame_2, text="Próximos 10 días", command=lambda: controller.show_frame(Caduc_dias)).pack(padx=5, pady=5, side=tk.LEFT)



        label_tex_cli4 = tk.Label(frame_3, text="Gestión de abonos", font=LARGE_FONT).pack(pady=15)

        button_new_ab = tk.Button(frame_3, text="Crear abono", command=lambda: controller.show_frame(Nuevo_abon)).pack(padx=5, pady=5, side=tk.LEFT)
        button_edit = tk.Button(frame_3, text="Editar datos del abonado", command=lambda: controller.show_frame(Edit_abon)).pack(padx=5, pady=5, side=tk.LEFT)
        button_renov = tk.Button(frame_3, text="Renovar abono", command=lambda: controller.show_frame(Renov_abon)).pack(padx=5, pady=5, side=tk.LEFT)
        button_delet = tk.Button(frame_3, text="Eliminar abono", command=lambda: controller.show_frame(Elimn_abon)).pack(padx=5, pady=5, side=tk.LEFT)

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=50)

class Estado_park(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(self)
        canvas.pack(fill="both", expand="yes", padx=10, pady=10)

        scroll_bar = ttk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
        scroll_bar.pack(side=tk.RIGHT, fill="y")

        canvas.configure(yscrollcommand=scroll_bar.set)

        canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

        main_frame = tk.Frame(canvas)

        canvas.create_window((0,0), window=main_frame, anchor="nw")

        plz=tk.StringVar()
        plz.set(park_serv.mostrar_info_detll(parking))

        label_tex_cli4 = tk.Label(main_frame, text="Información detallada del parking", font=LARGE_FONT).pack(pady=15)

        label_tex = tk.Label(main_frame, textvariable=plz, font=LARGE_FONT).pack(pady=5)

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=50)

class Fact_tik(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        hor = tk.StringVar()
        min = tk.StringVar()
        f1 = tk.StringVar()
        f2 = tk.StringVar()
        sol = tk.StringVar()
        fail = tk.StringVar()
        v=tk.IntVar()
        res = tk.StringVar()
        text=tk.StringVar()


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
                else:
                    fail.set( "Tiene que completarse las dos fechas")
            except ValueError:
                fail.set("Los datos tienen que ser enteros, para los meses tiene que estar entre 1 y 12 para los meses, de 1 a 31 para días,\n" \
                    "de 0 a 11 para horas, de 0 a 59 para minutos y años superiores al 2019.")

            return fecha1, fecha2

        def calculo(err, sol):
            fecha1, fecha2 = fechas(err)
            total, dinero = tick_serv.facturacion(lista_tickets, fecha1, fecha2)
            sol.set(f"Se han obtenido {dinero} €  entre las dos fechas por el cobro de {total} tichets")

        label_tex = tk.Label(self, text="Establezca las dos fechas entre las que se a a buscar la facturación de los tickets\n"
                                        "Para las horas y minutas, insertelo con dos números", font=LARGE_FONT).pack(pady=20)

        frame_opt=tk.Frame(self)
        frame_opt.pack(pady=20)

        tk.Radiobutton(frame_opt, text="Fecha de inicio", variable=v, value=1).pack(side=tk.LEFT, padx = 10)
        tk.Radiobutton(frame_opt, text="Fecha de fin", variable=v, value=2).pack(side=tk.LEFT, padx = 10)

        cal1 = Calendar(self, selectmode="day",date_pattern='mm/dd/y', year=2020, month=12, day=10)
        cal1.pack(pady=20)

        def fecha():
            if v.get()==1:
                f1.set(cal1.get_date()+"-"+hor.get()+":"+min.get())
            else:
                f2.set(cal1.get_date()+"-"+hor.get()+":"+min.get())

        frame_1=tk.Frame(self)
        frame_1.pack(pady=5)

        label_tex = tk.Label(frame_1, text="Hora (24H) ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
        Inp_h1 = tk.Entry(frame_1, textvariable=hor).pack(padx=5, pady=5, side=tk.LEFT)
        label_tex = tk.Label(frame_1, text="Minutos ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
        Inp_m1 = tk.Entry(frame_1, textvariable=min).pack(padx=5, pady=5, side=tk.LEFT)

        botonFec1 = tk.Button(self, text="Confrimar fecha",command=fecha, font=LARGE_FONT).pack(pady=10)

        frame_2=tk.Frame(self)
        frame_2.pack(pady=5)
        label_tex = tk.Label(frame_2, text="La fecha y hora de inicio es: ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        fech1 = tk.Label(frame_2, textvariable=f1)
        fech1.pack(side=tk.LEFT)

        frame_3=tk.Frame(self)
        frame_3.pack(pady=5)
        label_tex = tk.Label(frame_3, text="La fecha y hora de fin es: ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        fech2 = tk.Label(frame_3, textvariable=f2)
        fech2.pack(side=tk.LEFT)

        botonFec1 = tk.Button(self, text="Obtener facturación",command= lambda : calculo(fail, sol), font=LARGE_FONT).pack(pady=10)

        label_tex = tk.Label(self, textvariable=fail, font=LARGE_FONT).pack()

        label_tex = tk.Label(self, textvariable=sol, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=50)

class Cobro_abon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        anyo = tk.StringVar()
        sol = tk.StringVar()

        def calculo(sol, anyo):
            if anyo.get() != "":
                total = fact_serv.facturacion_anyo(lista_facturas,int(anyo.get()))
                sol.set(total)
            else:
                sol.set("El año no puede estar vacío")

        label_tex = tk.Label(self, text="Seleccione el año por el que va a buscar la facturación de los abonados", font=LARGE_FONT).pack(pady=20)

        cuadro = tk.Entry(self, textvariable=anyo).pack(padx=5)


        botonFec1 = tk.Button(self, text="Obtener facturación",command= lambda : calculo(sol, anyo), font=LARGE_FONT).pack(pady=30)

        label_tex = tk.Label(self, textvariable=sol, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=50)

class Caduc_anyo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        sol = tk.StringVar()
        fail = tk.StringVar()
        f1 = tk.StringVar()

        def obt_fecha(lista_abonos):
            lista = []
            fallo = True
            faill=""
            soll=""
            fallo ,lista, faill, soll = abon_serv.obtener_lista_cad(lista_abonos,cal1.get_date()[0:2], cal1.get_date()[6:10])
            fail.set(faill)
            sol.set(soll)
            return fallo, lista

        def consulta(sol):
            fallo, lista = obt_fecha(lista_abonos)
            res=""
            res = abon_serv.listar_caducidad_mes(fallo, lista)
            sol.set(res)

        label_tex = tk.Label(self, text="Seleccione la fecha donde se encuentre el mes y año a consultar", font=LARGE_FONT).pack(pady=10)
        def fecha():
            f1.set(cal1.get_date()[0:2] + " - " + cal1.get_date()[6:10])

        cal1 = Calendar(self, selectmode="day",date_pattern='mm/dd/y', year=2020, month=12, day=10)
        cal1.pack(pady=20)

        botonFec1 = tk.Button(self, text="Confrimar fecha",command=fecha, font=LARGE_FONT).pack(pady=10)
        fech1 = tk.Label(self, textvariable=f1).pack()

        boton = tk.Button(self, text="Consultar caducidad de abonos",command= lambda : consulta(sol), font=LARGE_FONT).pack(pady=20)

        label_tex = tk.Label(self, textvariable=fail, font=LARGE_FONT).pack()

        label_tex = tk.Label(self, textvariable=sol, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=50)


class Caduc_dias(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        label_tex = tk.Label(self, text=abon_serv.listar_caducidad_proximos_dias(lista_abonos), font=LARGE_FONT).pack(pady=30)

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=50)




class Nuevo_abon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        fec = tk.StringVar()
        sol = tk.StringVar()
        dni = tk.StringVar()
        nom = tk.StringVar()
        apl = tk.StringVar()
        taj = tk.StringVar()
        mail = tk.StringVar()
        matrc = tk.StringVar()
        tip_park = tk.IntVar()
        tip_abon = tk.IntVar()

        def date():
            anio1 = int(fec.get()[6:10])
            mes1= int(fec.get()[0:2])
            dia1= int(fec.get()[3:5])
            return datetime(anio1, mes1, dia1)

        def client():
            cliente = Cliente(dni.get().upper(),nom.get(),apl.get(),mail.get(),taj.get(),Vehiculo(matrc.get().upper()))
            return cliente

        def abono(sol):
            if dni.get() != "" and nom.get() != "" and apl.get() != "" and taj.get() != "" and mail.get() != "" and matrc.get() != "":
                fecha = date()
                cliente = client()
                resl = abon_serv.crear_abono(lista_abonos,lista_facturas, parking, tip_abon.get(),tip_park.get(),fecha,cliente)
                abon_serv.save_file(lista_abonos)
                fact_serv.save_file(lista_facturas)
                park_serv.save_file(parking)
                sol.set(resl)
            else:
                 sol.set("Todos los campos deben estar rellenos")

        label_tex = tk.Label(self, text="Complete los datos para crear un abono", font=LARGE_FONT).pack(pady=10)


        frame_1=tk.Frame(self)
        frame_1.pack(pady=5)

        label_tex = tk.Label(frame_1, text="DNI ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        Inp_dni = tk.Entry(frame_1, textvariable=dni).pack(padx=5, pady=5, side=tk.LEFT)
        label_tex = tk.Label(frame_1, text="Nombre ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        Inp_nom = tk.Entry(frame_1, textvariable=nom).pack(padx=5, pady=5, side=tk.LEFT)
        label_tex = tk.Label(frame_1, text="Apellidos ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        Inp_ape = tk.Entry(frame_1, textvariable=apl).pack(padx=5, pady=5, side=tk.LEFT)

        frame_2=tk.Frame(self)
        frame_2.pack(pady=5)

        label_tex = tk.Label(frame_2, text="Nº tarjeta ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        Inp_tarj = tk.Entry(frame_2, textvariable=taj).pack(padx=5, pady=5, side=tk.LEFT)
        label_tex = tk.Label(frame_2, text="Correo ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        Inp_mail = tk.Entry(frame_2, textvariable=mail).pack(padx=5, pady=5, side=tk.LEFT)
        label_tex = tk.Label(frame_2, text="Matrícula ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        Inp_matric = tk.Entry(frame_2, textvariable=matrc).pack(padx=5, pady=5, side=tk.LEFT)

        label_tex = tk.Label(self, text="Tipo de vehículo", font=LARGE_FONT).pack(pady=5)

        frame_opt_park=tk.Frame(self)
        frame_opt_park.pack(pady=5)

        tk.Radiobutton(frame_opt_park, text="Coche", variable=tip_park, value=1).pack(side=tk.LEFT, padx = 5)
        tk.Radiobutton(frame_opt_park, text="Moto", variable=tip_park, value=2).pack(side=tk.LEFT, padx = 5)
        tk.Radiobutton(frame_opt_park, text="Movilidad reducida",variable=tip_park, value=3).pack(side=tk.LEFT, padx = 5)

        label_tex = tk.Label(self, text="Tipo de abono", font=LARGE_FONT).pack(pady=5)

        frame_opt_ab=tk.Frame(self)
        frame_opt_ab.pack(pady=5)

        tk.Radiobutton(frame_opt_ab, text="Mensual (25€)", variable=tip_abon, value=1).pack(side=tk.LEFT, padx = 5)
        tk.Radiobutton(frame_opt_ab, text="Trimestral (70€)", variable=tip_abon, value=2).pack(side=tk.LEFT, padx = 5)
        tk.Radiobutton(frame_opt_ab, text="Semestral (130€)",variable=tip_abon, value=3).pack(side=tk.LEFT, padx = 5)
        tk.Radiobutton(frame_opt_ab, text="Anual (200€)",variable=tip_abon, value=4).pack(side=tk.LEFT, padx = 5)

        cal1 = Calendar(self, selectmode="day",date_pattern='mm/dd/y', year=2020, month=12, day=10)
        cal1.pack(pady=5)

        def fecha():
            fec.set(cal1.get_date())

        frame_1=tk.Frame(self)
        frame_1.pack(pady=5)

        botonFec1 = tk.Button(self, text="Confrimar fecha de inicio de abono",command=fecha, font=LARGE_FONT).pack(pady=5)

        frame_h=tk.Frame(self)
        frame_h.pack(pady=5)

        label_tex = tk.Label(frame_h, text="La fecha y hora de inicio es: ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        fech1 = tk.Label(frame_h, textvariable=fec)
        fech1.pack(side=tk.LEFT)

        boton = tk.Button(self, text="Confrimar solicitud de abono",command= lambda : abono(sol), font=LARGE_FONT).pack(pady=5)

        label_tex = tk.Label(self, textvariable=sol, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=20)

class Edit_abon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        sol = tk.StringVar()
        dni = tk.StringVar()
        nom = tk.StringVar()
        apl = tk.StringVar()
        taj = tk.StringVar()
        mail = tk.StringVar()


        def renov(sol):
            if dni.get() != "" and nom.get() != "" and apl.get() != "" and taj.get() != "" and mail.get() != "":
                res = abon_serv.modificar_abonado(lista_abonos, dni.get().upper(), nom.get(), apl.get(), taj.get(), mail.get())
                sol.set(res)
                abon_serv.save_file(lista_abonos)
            else:
                sol.set("Todos los campos deben estar rellenos")

        label_tex = tk.Label(self, text="Inserte el DNI del abonado en cuestión y los datos a modificar", font=LARGE_FONT).pack(pady=10)


        frame_1=tk.Frame(self)
        frame_1.pack(pady=5)

        label_tex = tk.Label(frame_1, text="DNI ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
        Inp_dni = tk.Entry(frame_1, textvariable=dni).pack(padx=5, pady=15, side=tk.LEFT)


        frame_1=tk.Frame(self)
        frame_1.pack(pady=5)

        label_tex = tk.Label(frame_1, text="Nombre ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
        Inp_nom = tk.Entry(frame_1, textvariable=nom).pack(padx=5, pady=15, side=tk.LEFT)
        label_tex = tk.Label(frame_1, text="Apellidos ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
        Inp_ape = tk.Entry(frame_1, textvariable=apl).pack(padx=5, pady=15, side=tk.LEFT)

        frame_2=tk.Frame(self)
        frame_2.pack(pady=5)

        label_tex = tk.Label(frame_2, text="Nº tarjeta ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
        Inp_tarj = tk.Entry(frame_2, textvariable=taj).pack(padx=5, pady=15, side=tk.LEFT)
        label_tex = tk.Label(frame_2, text="Correo ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
        Inp_mail = tk.Entry(frame_2, textvariable=mail).pack(padx=5, pady=15, side=tk.LEFT)

        boton = tk.Button(self, text="Confrimar datos del abonado",command= lambda : renov(sol), font=LARGE_FONT).pack(pady=20)

        label_tex = tk.Label(self, textvariable=sol, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=30)

class Renov_abon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        sol = tk.StringVar()
        dni = tk.StringVar()
        tip_abon = tk.IntVar()


        def renov(sol):
            ok, resl = abon_serv.renovar_abono(lista_abonos,lista_facturas, dni.get().upper(), tip_abon.get())
            if ok:
                abon_serv.save_file(lista_abonos)
                fact_serv.save_file(lista_facturas)
            sol.set(resl)

        label_tex = tk.Label(self, text="Inserte el DNI del abonado en cuestión y por cuanto desea renovarlo", font=LARGE_FONT).pack(pady=10)


        frame_1=tk.Frame(self)
        frame_1.pack(pady=5)

        label_tex = tk.Label(frame_1, text="DNI ", font=LARGE_FONT).pack(pady=5, side=tk.LEFT)
        Inp_dni = tk.Entry(frame_1, textvariable=dni).pack(padx=5, pady=5, side=tk.LEFT)


        label_tex = tk.Label(self, text="Tipo de abono", font=LARGE_FONT).pack(pady=5)

        frame_opt_ab=tk.Frame(self)
        frame_opt_ab.pack(pady=5)

        tk.Radiobutton(frame_opt_ab, text="Mensual (25€)", variable=tip_abon, value=1).pack(side=tk.LEFT, padx = 5)
        tk.Radiobutton(frame_opt_ab, text="Trimestral (70€)", variable=tip_abon, value=2).pack(side=tk.LEFT, padx = 5)
        tk.Radiobutton(frame_opt_ab, text="Semestral (130€)",variable=tip_abon, value=3).pack(side=tk.LEFT, padx = 5)
        tk.Radiobutton(frame_opt_ab, text="Anual (200€)",variable=tip_abon, value=4).pack(side=tk.LEFT, padx = 5)

        boton = tk.Button(self, text="Confrimar renovación de abono",command= lambda : renov(sol), font=LARGE_FONT).pack(pady=5)

        label_tex = tk.Label(self, textvariable=sol, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=30)

class Elimn_abon(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        sol = tk.StringVar()
        dni = tk.StringVar()


        def delet(sol):
            if dni.get() != "":
                if abon_serv.search_by_dni(lista_abonos, dni.get().upper()) != None:
                    abon_serv.remove(lista_abonos,abon_serv.search_by_dni(lista_abonos, dni.get().upper()))
                    sol.set("La acción de borrado ha concluido satisfactoriamente")
                    abon_serv.save_file(lista_abonos)
                else:
                    sol.set("No nos consta un abono perteneciente a un cliente con ese DNI")
            else:
                sol.set("Debe proporcionarnos el DNI")

        label_tex = tk.Label(self, text="Inserte el DNI del abonado en cuestión", font=LARGE_FONT).pack(pady=10)


        frame_1=tk.Frame(self)
        frame_1.pack(pady=5)

        label_tex = tk.Label(frame_1, text="DNI ", font=LARGE_FONT).pack(pady=15, side=tk.LEFT)
        Inp_dni = tk.Entry(frame_1, textvariable=dni).pack(padx=5, pady=15, side=tk.LEFT)


        boton = tk.Button(self, text="Confrimar aliminación del abonado",command= lambda : delet(sol), font=LARGE_FONT).pack(pady=20)

        label_tex = tk.Label(self, textvariable=sol, font=LARGE_FONT).pack()

        def salir(self):
            python = sys.executable
            os.execl(python, python, * sys.argv)
            return controller.show_frame(StartPage)

        boton2 = tk.Button(self, text="Salir", font=LARGE_FONT, command=lambda: salir(self)).pack(pady=30)



app = SeaofBTCapp()
app.wm_geometry("900x800")
app.mainloop()
