import os
import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image

class ConvertidorImagenes(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Convertidor de Imágenes")
        self.geometry("450x380")
        self.rutas_imagenes = []
        
        # 1. Botón seleccionar imágenes
        self.btn_seleccionar = ctk.CTkButton(self, text="Seleccionar Imágenes", command=self.seleccionar_archivos)
        self.btn_seleccionar.pack(pady=15)
        
        self.lbl_contador = ctk.CTkLabel(self, text="0 imágenes seleccionadas")
        self.lbl_contador.pack()

        # 2. Selector de formato
        self.formato_var = ctk.StringVar(value="WEBP")
        self.menu_formato = ctk.CTkOptionMenu(self, values=["WEBP", "JPG", "PNG", "ICO"], variable=self.formato_var)
        self.menu_formato.pack(pady=15)

        # 3. Control de calidad
        self.slider_calidad = ctk.CTkSlider(self, from_=10, to=100)
        self.slider_calidad.set(85)
        self.slider_calidad.pack(pady=10)

        # 4. Barra de progreso y botón convertir
        self.progreso = ctk.CTkProgressBar(self)
        self.progreso.set(0)
        self.progreso.pack(pady=15)

        self.btn_convertir = ctk.CTkButton(self, text="Convertir", command=self.iniciar_conversion)
        self.btn_convertir.pack(pady=10)

    def seleccionar_archivos(self):
        archivos = filedialog.askopenfilenames(filetypes=[("Imágenes", "*.png *.jpg *.jpeg *.webp *.bmp")])
        if archivos:
            self.rutas_imagenes = archivos
            self.lbl_contador.configure(text=f"{len(archivos)} imágenes seleccionadas")

    def iniciar_conversion(self):
        if not self.rutas_imagenes:
            messagebox.showwarning("Atención", "Selecciona al menos una imagen.")
            return
        # Ejecutar en un hilo separado para no congelar la interfaz
        threading.Thread(target=self.procesar_imagenes, daemon=True).start()

    def procesar_imagenes(self):
        formato = self.formato_var.get().lower()
        calidad = int(self.slider_calidad.get())
        total = len(self.rutas_imagenes)

        for i, ruta in enumerate(self.rutas_imagenes):
            img = Image.open(ruta)
            # Manejar transparencia si se convierte a JPG
            if formato in ["jpg", "jpeg"] and img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
                
            nombre_base = os.path.splitext(ruta)[0]
            nueva_ruta = f"{nombre_base}_convertida.{formato}"
            
            img.save(nueva_ruta, quality=calidad)
            self.progreso.set((i + 1) / total)
            
        messagebox.showinfo("Éxito", "Conversión completada.")

if __name__ == "__main__":
    app = ConvertidorImagenes()
    app.mainloop()
