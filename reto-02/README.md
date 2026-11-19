# Reto 02: adivina el número

Un juego con interfaz gráfica creado con Python y Tkinter. El programa piensa un número aleatorio del 1 al 100 y el jugador intenta adivinarlo.

## Cómo ejecutarlo

Desde la raíz del repositorio:

```bash
python reto-02/adivina-el-numero.py
```

Se necesita Python con soporte para Tkinter.

## Cómo funciona

1. Al iniciar, `Tk()` crea la ventana y `JuegoAdivinar` configura sus controles. `mainloop()` mantiene la ventana abierta y espera las acciones del usuario.
2. `random.randint(1, 100)` elige el número secreto. El atributo `intentos` comienza en cero.
3. El jugador puede escribir un número y pulsar **Adivinar**, o presionar `Enter`. Ambas acciones llaman a `verificar_intento`.
4. El método elimina espacios al principio y al final del texto y comprueba que contenga solo dígitos. Si no es válido, muestra un mensaje y limpia el campo; ese valor no cuenta como intento.
5. Si la entrada es válida, la convierte a entero, suma un intento, actualiza el contador y compara el número con el secreto. Muestra si el valor es demasiado bajo o demasiado alto.
6. Cuando el jugador acierta, aparece un mensaje con la cantidad de intentos y se deshabilitan el campo y el botón. También se quita la acción asociada a `Enter`.
7. **Reiniciar Juego** elige otro número secreto, pone el contador en cero, restaura el mensaje inicial y vuelve a habilitar el campo y el botón.

El programa valida que la entrada sean dígitos, pero no comprueba que el número esté entre 1 y 100. Por eso, cualquier entero fuera de ese rango también se compara y cuenta como intento.
