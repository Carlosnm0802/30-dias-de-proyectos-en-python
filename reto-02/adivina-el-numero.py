#Juego de adivinar el número con interfaz gráfica

import tkinter as tk
import random

#Clase para iniciar ek juego 
class JuegoAdivinar:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el número")
        self.root.geometry("300x200")
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
