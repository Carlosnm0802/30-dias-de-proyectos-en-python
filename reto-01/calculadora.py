from tkinter import Text, Tk , Button


class Interfaz:
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")
        
        #Agregar pantalla de calculadora
        self.pantalla = Text(ventana,state="disabled",width=40, height=3,background="orchid",foreground="white",font=("Helvetica", 15))
        self.pantalla.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
         
        #Variable global
        self.operacion = ""
        
        #Agregar botones de la calculadora
        boton1= self.crearBoton(7)
        boton2= self.crearBoton(8)
        boton3= self.crearBoton(9)
        boton4 = self.crearBoton(u"\u232b",escribir=False)
        boton5= self.crearBoton(4)
        boton6= self.crearBoton(5)
        boton7= self.crearBoton(6)
        boton8= self.crearBoton(u"\u00F7",escribir=False) 
        boton9 = self.crearBoton(1) 
        boton10 = self.crearBoton(2)
        boton11 = self.crearBoton(3)
        boton12 = self.crearBoton("*") #Multiplicar
        boton13 = self.crearBoton(".")
        boton14 = self.crearBoton(0)
        boton15 = self.crearBoton("+")
        boton16 = self.crearBoton("-")
        boton17 = self.crearBoton("=", escribir=False, ancho=10, alto=2)

        #Arreglo de botones
        botones = [
            boton1, boton2, boton3, boton4,
            boton5, boton6, boton7, boton8,
            boton9, boton10, boton11, boton12,
            boton13, boton14, boton15, boton16,
            boton17
        ]
ventana_principal = Tk()
calculadora = Interfaz(ventana_principal)
ventana_principal.mainloop()
