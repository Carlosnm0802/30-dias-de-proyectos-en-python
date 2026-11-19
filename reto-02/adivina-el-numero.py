#Juego de adivinar el número con interfaz gráfica

import tkinter as tk
import random

#Clase para iniciar ek juego 
class JuegoAdivinar:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el número")
        self.root.geometry("300x260")
        self.root.resizable(False, False)
    
        #Variables del juego 
        self.numero_secreto = random.randint(1,100)
        self.intentos = 0
        
        #Etiqueta de instrucciones
        self.label_info = tk.Label(
        root,
        text=(
            "He pensado un número del 1 al 100.\n¿Puedes adivinar cuál es?"
        ),
        font=("Arial", 11),
        pady=10,
    )
        self.label_info.pack()
        
        #Campo de texto para ingresar el numero 
        self.entry_numero = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry_numero.pack(pady=10)
        self.entry_numero.focus()
        self.entry_numero.bind("<Return>", lambda event: self.verificar_intento())
        
        #Boton para adivinar
        self.btn_adivinar = tk.Button(
        root,
        text="Adivinar",
        font=("Arial", 11, "bold"),
        bg="#4CAF50",
        fg="white",
        command=self.verificar_intento,
        )
        self.btn_adivinar.pack(pady=5)
        
        #Boton para reiniciar el juego
        self.btn_reiniciar = tk.Button(
            root,
            text="Reiniciar Juego",
            font=("Arial", 10),
            command=self.reiniciar_juego,
        )
        self.btn_reiniciar.pack(pady=10)
        
        # Etiqueta de intentos
        self.label_intentos = tk.Label(
            root, text="Intentos: 0", font=("Arial", 10, "italic")
        )
        self.label_intentos.pack(pady=5)
        
        #Logica de verificacion de intentos
    def verificar_intento(self):
            valor = self.entry_numero.get().strip()
            if not valor.isdigit():
                self.label_info.config(text="Por favor, ingresa un número válido.")
                self.entry_numero.delete(0, tk.END)
                return
            numero = int(valor)
            self.intentos +=1
            self.label_intentos.config(text=f"Intentos: {self.intentos}")
            self.entry_numero.delete(0, tk.END)
            if numero < self.numero_secreto:
                self.label_info.config(text="Demasiado bajo. Intenta de nuevo.")
            elif numero > self.numero_secreto:
                self.label_info.config(text="Demasiado alto. Intenta de nuevo.")
            else:
                self.label_info.config(text=f"¡Felicidades! Adivinaste el número en {self.intentos} intentos.")
                self.entry_numero.config(state="disabled")
                self.btn_adivinar.config(state="disabled")
                self.entry_numero.unbind("<Return>")
    
    def reiniciar_juego(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0
        self.label_info.config(
            text="He pensado un número del 1 al 100.\n¿Puedes adivinar cuál es?"
        )
        self.label_intentos.config(text="Intentos: 0")
        self.entry_numero.delete(0, tk.END)
        self.btn_adivinar.config(state="normal")
        self.entry_numero.focus()
        self.entry_numero.config(state="normal")
        self.entry_numero.bind("<Return>", lambda event: self.verificar_intento())
    
    #INICIAR EL JUEGO
if __name__ == "__main__":
    root = tk.Tk()
    app = JuegoAdivinar(root)  
    root.mainloop()
    

