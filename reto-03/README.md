# Convertidor de Imágenes 🖼️

## Descripción

Este programa es un **convertidor de imágenes con interfaz gráfica** que permite convertir múltiples imágenes a diferentes formatos de forma fácil y rápida. Está desarrollado en Python utilizando `customtkinter` para una interfaz moderna.

## Características ✨

- ✅ **Convertir múltiples imágenes** simultáneamente
- ✅ **Múltiples formatos soportados**: WEBP, JPG, PNG, ICO
- ✅ **Control de calidad** ajustable mediante slider
- ✅ **Barra de progreso** en tiempo real
- ✅ **Interfaz moderna** y fácil de usar
- ✅ **Manejo de transparencia** automático (convierte RGBA a RGB para JPG)
- ✅ **Procesamiento en segundo plano** sin congelar la interfaz

## Requisitos Previos 📋

Antes de ejecutar el programa, necesitas tener instalados:

- **Python 3.9+** (con soporte para tkinter)
- **customtkinter**: Librería para interfaces gráficas modernas
- **Pillow**: Librería para procesamiento de imágenes

### Instalación de Dependencias

Si aún no has instalado las dependencias, ejecuta:

```bash
pip install customtkinter Pillow
```

**Nota para macOS:** Si tienes problemas con tkinter, instala:

```bash
brew install python@3.9
brew install python-tk@3.9
```

## Uso 🚀

### Opción 1: Con Python de Homebrew (macOS)

```bash
/opt/homebrew/bin/python3.9 /path/to/image_converter.py
```

### Opción 2: Con Python del sistema

```bash
python3 /path/to/image_converter.py
```

### Opción 3: Desde la carpeta del proyecto

```bash
cd reto-03
python3 image_converter.py
```

## Cómo Usar la Aplicación 📱

1. **Seleccionar Imágenes**: Haz clic en el botón "Seleccionar Imágenes"
   - Se abrirá un diálogo para elegir una o más imágenes
   - Formatos soportados: `.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`

2. **Elegir Formato de Salida**: Usa el menú desplegable para seleccionar el formato deseado
   - **WEBP**: Mejor compresión (recomendado)
   - **JPG**: Formato tradicional
   - **PNG**: Con transparencia
   - **ICO**: Iconos

3. **Ajustar Calidad**: Mueve el slider de calidad (10-100)
   - Valores más altos = mejor calidad pero archivos más grandes
   - Valor recomendado: 85

4. **Convertir**: Haz clic en el botón "Convertir"
   - La barra de progreso mostrará el avance
   - Se abrirá un mensaje confirmando el éxito

5. **Resultado**: Las imágenes convertidas se guardarán en la misma carpeta con el sufijo `_convertida`
   - Ejemplo: `foto.jpg` → `foto_convertida.webp`

## Estructura del Código 🏗️

```
image_converter.py
├── ConvertidorImagenes (Clase principal)
│   ├── __init__()          # Configuración de la interfaz
│   ├── seleccionar_archivos()  # Diálogo para seleccionar imágenes
│   ├── iniciar_conversion()    # Inicia el proceso en hilo separado
│   └── procesar_imagenes()     # Realiza la conversión
```

### Componentes Principales

- **Botón "Seleccionar Imágenes"**: Abre un diálogo para elegir archivos
- **Contador**: Muestra cuántas imágenes se han seleccionado
- **Menú de Formato**: Permite elegir el formato de salida
- **Slider de Calidad**: Controla la calidad de compresión (10-100)
- **Barra de Progreso**: Muestra el avance de la conversión
- **Botón "Convertir"**: Inicia el proceso de conversión

## Detalles Técnicos 🔧

### Procesamiento de Imágenes

- **Conversión de modo de color**: Convierte automáticamente imágenes RGBA y P a RGB cuando se convierten a JPG (ya que JPG no soporta transparencia)
- **Preservación de ruta**: Las imágenes convertidas se guardan en la misma carpeta que las originales
- **Procesamiento asincrónico**: Utiliza threading para no congelar la interfaz gráfica

### Formato de Salida

```python
imagen_convertida.save(nueva_ruta, quality=calidad)
```

Donde:
- `nueva_ruta`: Ruta del archivo con nombre `{nombre_original}_convertida.{formato}`
- `quality`: Valor entre 10 y 100

## Ejemplo de Uso 📸

```bash
# 1. Abre la aplicación
python3 image_converter.py

# 2. Haz clic en "Seleccionar Imágenes"
# 3. Selecciona: foto1.jpg, foto2.png, foto3.bmp
# 4. Elige formato: WEBP
# 5. Ajusta calidad a: 90
# 6. Haz clic en "Convertir"

# Resultado:
# foto1_convertida.webp
# foto2_convertida.webp
# foto3_convertida.webp
```

## Solución de Problemas ⚠️

### Error: "ModuleNotFoundError: No module named 'customtkinter'"

```bash
pip install customtkinter
```

### Error: "ModuleNotFoundError: No module named 'PIL'"

```bash
pip install Pillow
```

### Advertencia: "DEPRECATION WARNING: The system version of Tk is deprecated"

Esto es solo una advertencia. Para evitarla, usa Python de Homebrew:

```bash
brew install python@3.9 python-tk@3.9
/opt/homebrew/bin/python3.9 image_converter.py
```

### La ventana no se abre en macOS

En macOS, el Python del sistema tiene problemas con tkinter. Solución:

```bash
brew install python@3.9
brew install python-tk@3.9
/opt/homebrew/bin/python3.9 image_converter.py
```

## Formatos Soportados 🎨

| Formato | Extensión | Descripción |
|---------|-----------|-------------|
| WEBP    | .webp     | Mejor compresión, ideal para web |
| JPG     | .jpg      | Formato tradicional, ampliamente compatible |
| PNG     | .png      | Soporta transparencia |
| ICO     | .ico      | Formato de iconos |

## Notas Importantes 📌

- ⚠️ **Preservación**: Las imágenes originales **NO se modifican**
- ⚠️ **Transparencia**: Si conviertes a JPG, se perderá la transparencia (se convertirá a RGB)
- ⚠️ **Calidad**: Valores muy bajos (< 50) pueden afectar significativamente la calidad
- 💾 **Espacio**: Las nuevas imágenes se guardan en la misma carpeta
- ⏱️ **Tiempo**: El procesamiento depende del tamaño y cantidad de imágenes

## Autor 👨‍💻

Reto #3 del proyecto "30 Días de Proyectos en Python"

## Licencia 📄

Este proyecto es de código abierto y puede ser modificado libremente.
