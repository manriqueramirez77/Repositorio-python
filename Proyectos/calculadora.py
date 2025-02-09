from tkinter import Tk, Entry, Button, StringVar

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora Alternativa")
        self.ventana.resizable(0, 0)  # Evita que la ventana sea redimensionable

        # Variable para almacenar la expresión
        self.expresion = StringVar()
        self.expresion.set("")

        # Entrada de texto
        self.entrada = Entry(ventana, textvariable=self.expresion, font=("Arial", 18), bd=10, insertwidth=4, width=14, justify="right")
        self.entrada.grid(row=0, column=0, columnspan=4)

        # Botones
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', 'C', '+',
            '='
        ]

        # Posiciones de los botones
        posiciones = [
            (1, 0), (1, 1), (1, 2), (1, 3),
            (2, 0), (2, 1), (2, 2), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3),
            (4, 0), (4, 1), (4, 2), (4, 3),
            (5, 0)
        ]

        # Crear y colocar los botones
        for (texto, pos) in zip(botones, posiciones):
            if texto == '=':
                boton = Button(ventana, text=texto, bg="lightblue", fg="black", font=("Arial", 18), bd=5, command=self.calcular)
                boton.grid(row=pos[0], column=pos[1], columnspan=4, sticky="nsew")
            elif texto == 'C':
                boton = Button(ventana, text=texto, bg="red", fg="white", font=("Arial", 18), bd=5, command=self.limpiar)
                boton.grid(row=pos[0], column=pos[1], sticky="nsew")
            else:
                boton = Button(ventana, text=texto, bg="gray", fg="white", font=("Arial", 18), bd=5, command=lambda t=texto: self.agregar(t))
                boton.grid(row=pos[0], column=pos[1], sticky="nsew")

    def agregar(self, valor):
        """Agrega un valor a la expresión actual."""
        self.expresion.set(self.expresion.get() + valor)

    def limpiar(self):
        """Limpia la expresión."""
        self.expresion.set("")

    def calcular(self):
        """Evalúa la expresión y muestra el resultado."""
        try:
            resultado = str(eval(self.expresion.get()))
            self.expresion.set(resultado)
        except Exception as e:
            self.expresion.set("Error")

# Iniciar la aplicación
if __name__ == "__main__":
    ventana = Tk()
    calculadora = Calculadora(ventana)
    ventana.mainloop()