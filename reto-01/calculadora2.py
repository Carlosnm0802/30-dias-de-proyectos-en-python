import tkinter as tk
from tkinter import messagebox, ttk

root = tk.Tk() #Creamos la pantalla principal
root.title("Segunda version de Calculara") #Título de la ventana principal
root.geometry("400x500") #Dimensiones de calculadora
root.resizable(0,0)

#Variables de color 
color_texto = "white"
color_boton = "#5b21b6"
color_boton_igual = "#166534"
color_boton_clear = "#b91c1c"

estilo = ttk.Style(root)
estilo.theme_use("clam")
for nombre, color, color_activo in (
    ("Numero.TButton", color_boton, "#4c1d95"),
    ("Igual.TButton", color_boton_igual, "#14532d"),
    ("Limpiar.TButton", color_boton_clear, "#991b1b"),
):
    estilo.configure(nombre, background=color, foreground=color_texto, font=("Helvetica", 20))
    estilo.map(nombre, background=[("pressed", color_activo), ("active", color_activo)])

screen_text = tk.StringVar() #Creamos la pantalla de la calculadora 
screen_label = tk.Label(root, textvariable=screen_text, bg="black", fg=color_texto, font=("Helvetica", 20),anchor="e",padx=10)
screen_label.grid(row=0, column=0, columnspan=4, sticky="we",pady=10)
expression = ""  #Variable que almacena el contenido de la calculadora

#Diferentes funciones de la calculadora 
def press(num):
    global expression
    expression += str(num)
    screen_text.set(expression)

def equalpress():
    global expression
    try:
        result = str(eval(expression))
        screen_text.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Not valid entry")
        screen_text.set("")
        expression = ""

def clear():
    global expression
    screen_text.set("")
    expression = ""
    
#Botones de la calculadora
buttons = [
    ('7',1,0),
    ('8',1,1),
    ('9',1,2),
    ('/',1,3),
    ('4',2,0),
    ('5',2,1),
    ('6',2,2),
    ('*',2,3),
    ('1',3,0),
    ('2',3,1),
    ('3',3,2),
    ('-',3,3),
    ('0',4,0),
    ('.',4,1),
    ('+',4,2)
]

for (text,row,col) in buttons:
    button = ttk.Button(root, text=text, style="Numero.TButton", command=lambda t=text: press(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

equal_button = ttk.Button(root, text="=", style="Igual.TButton", command=equalpress)
equal_button.grid(row=4, column=3, sticky="nsew", padx=5, pady=5)
clear_button = ttk.Button(root, text="C", style="Limpiar.TButton", command=clear)
clear_button.grid(row=5, column=0, sticky="nsew", padx=5, pady=5)
    
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()