# Reto 01: calculadora gráfica

Una calculadora sencilla con interfaz gráfica creada con Python y Tkinter. Permite escribir números y operaciones, calcular el resultado y limpiar la pantalla.

## Cómo ejecutarla

Desde la raíz del repositorio:

```bash
python reto-01/calculadora.py
```

También puedes ejecutar la segunda versión con `python reto-01/calculadora2.py`. Esta utiliza una etiqueta para la pantalla y muestra un mensaje si la operación no es válida.

Se necesita Python con soporte para Tkinter. Para comprobarlo, ejecuta `python -m tkinter`: debería abrirse una ventana de prueba. En macOS, si usas Python 3.14 de Homebrew y falta `_tkinter`, puedes instalarlo con `brew install python-tk@3.14`.

## Cómo funciona

1. `Tk()` crea la ventana y la clase `Interfaz` configura la pantalla y los botones. `mainloop()` mantiene la ventana abierta y espera las acciones del usuario.
2. `crearBoton` crea cada botón y conecta su acción con el método `click`. Los botones se organizan en una cuadrícula con `grid`.
3. Al pulsar un número o un operador, `click` agrega su valor a `self.operacion` y lo muestra en pantalla. El botón `⌫` limpia toda la operación.
4. Al pulsar `=`, se reemplaza `÷` por `/` y se calcula la expresión con `eval`. Por ejemplo, `7÷2` se convierte en `7/2` y muestra `3.5`.
5. La operación guardada se vacía después de calcular; el resultado permanece visible hasta que se limpia la pantalla.

La pantalla está deshabilitada para evitar que se escriba directamente en ella. Los métodos `mostrarenPantalla` y `limpiarPantalla` la habilitan temporalmente para actualizar su contenido.

## Aspectos por mejorar

La primera versión todavía no maneja expresiones inválidas ni divisiones entre cero, por lo que pueden aparecer errores en la terminal. Además, ambas versiones usan `eval`, que ejecuta expresiones de Python: para una versión más segura conviene reemplazarlo por operaciones explícitas y validar la entrada.
