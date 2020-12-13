import tkinter as tk
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

        for F in (StartPage, PageOne, PageTwo):

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
                            command=lambda: controller.show_frame(PageOne))
        button_ret_cli = tk.Button(frame_clien, text="Retirar vehículo",
                            command=lambda: controller.show_frame(PageOne))
        button_ing_abo = tk.Button(frame_clien, text="Depositar vehículo (abonado)",
                            command=lambda: controller.show_frame(PageOne))
        button_ret_abo = tk.Button(frame_clien, text="Retirar vehículo (abonado)",
                            command=lambda: controller.show_frame(PageOne))
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
                return controller.show_frame(PageOne)
            else:
                return controller.show_frame(StartPage)

        button2 = tk.Button(frame_admin, text="Comprobar",
                            command=comprobar_contr)
        button2.pack(padx=5, pady=20)


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


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = tk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One",
                            command=lambda: controller.show_frame(PageOne))
        button2.pack()



app = SeaofBTCapp()
app.wm_geometry("800x500")
app.mainloop()
