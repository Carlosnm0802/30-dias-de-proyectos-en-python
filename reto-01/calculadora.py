from tkinter import Tk


class Interfaz:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        self.ventana.geometry("300x400")

ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()