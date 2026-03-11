"""
--------------------------------------------------------
TAREA: Creación de una Aplicación GUI

Autor: María Pianda
Lenguaje: Python
Librería: Tkinter / ttk
--------------------------------------------------------

DESCRIPCIÓN
Esta aplicación permite ingresar datos mediante una interfaz gráfica,
visualizarlos en una tabla tipo Excel, eliminar elementos seleccionados
y limpiar todos los registros.

REQUISITOS CUMPLIDOS
✔ Ventana principal con título
✔ Uso de Labels
✔ Campo de texto
✔ Botones (Agregar, Eliminar, Limpiar)
✔ Tabla para mostrar datos (Treeview)
✔ Manejo de eventos
✔ Uso de Tkinter
✔ Programación Orientada a Objetos
✔ Interfaz gráfica organizada

DISEÑO DE INTERFAZ

---------------------------------------------------
                GESTOR DE DATOS
---------------------------------------------------

Ingrese un dato:
[________________________]

[Agregar] [Eliminar] [Limpiar]

Tabla de datos

ID        DATO
1         Ejemplo
2         Ejemplo

---------------------------------------------------

PRUEBAS

1. Ingresar texto y presionar "Agregar".
Resultado: el dato aparece en la tabla.

2. Seleccionar un elemento y presionar "Eliminar".
Resultado: el elemento desaparece.

3. Presionar "Limpiar".
Resultado: la tabla se vacía.
---------------------------------------------------
"""

import tkinter as tk
from tkinter import ttk


class InterfazGUI:
    """
    Clase que maneja toda la interfaz gráfica.
    """

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Gestor de Datos - GUI")
        self.ventana.geometry("500x400")
        self.ventana.resizable(False, False)

        self.contador_id = 1

        self.crear_componentes()

    def crear_componentes(self):
        """
        Crea todos los elementos de la interfaz.
        """

        # Título
        titulo = tk.Label(
            self.ventana,
            text="GESTOR DE DATOS",
            font=("Arial", 16, "bold")
        )
        titulo.pack(pady=10)

        # Frame de entrada
        frame_entrada = tk.Frame(self.ventana)
        frame_entrada.pack(pady=10)

        label = tk.Label(frame_entrada, text="Ingrese un dato:")
        label.grid(row=0, column=0, padx=5)

        self.campo_texto = tk.Entry(frame_entrada, width=25)
        self.campo_texto.grid(row=0, column=1, padx=5)

        # Frame de botones
        frame_botones = tk.Frame(self.ventana)
        frame_botones.pack(pady=10)

        boton_agregar = tk.Button(
            frame_botones,
            text="Agregar",
            width=10,
            command=self.agregar_dato
        )
        boton_agregar.grid(row=0, column=0, padx=5)

        boton_eliminar = tk.Button(
            frame_botones,
            text="Eliminar",
            width=10,
            command=self.eliminar_dato
        )
        boton_eliminar.grid(row=0, column=1, padx=5)

        boton_limpiar = tk.Button(
            frame_botones,
            text="Limpiar",
            width=10,
            command=self.limpiar_tabla
        )
        boton_limpiar.grid(row=0, column=2, padx=5)

        # Tabla tipo Excel
        frame_tabla = tk.Frame(self.ventana)
        frame_tabla.pack(pady=10)

        columnas = ("ID", "Dato")

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=columnas,
            show="headings",
            height=10
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Dato", text="Dato")

        self.tabla.column("ID", width=50, anchor="center")
        self.tabla.column("Dato", width=300)

        self.tabla.pack()

    def agregar_dato(self):
        """
        Evento del botón Agregar.
        Inserta un nuevo dato en la tabla.
        """

        dato = self.campo_texto.get()

        if dato.strip() != "":
            self.tabla.insert(
                "",
                "end",
                values=(self.contador_id, dato)
            )

            self.contador_id += 1
            self.campo_texto.delete(0, tk.END)

    def eliminar_dato(self):
        """
        Elimina el elemento seleccionado en la tabla.
        """

        seleccionado = self.tabla.selection()

        if seleccionado:
            self.tabla.delete(seleccionado)

    def limpiar_tabla(self):
        """
        Elimina todos los datos de la tabla.
        """

        for elemento in self.tabla.get_children():
            self.tabla.delete(elemento)

        self.contador_id = 1


class Aplicacion:
    """
    Clase principal que inicia el programa.
    """

    def __init__(self):
        self.ventana = tk.Tk()
        self.gui = InterfazGUI(self.ventana)

    def ejecutar(self):
        self.ventana.mainloop()


# Programa principal
if __name__ == "__main__":
    app = Aplicacion()
    app.ejecutar()