import tkinter as tk
from tkinter import ttk, messagebox

# =====================
# MODELO
# =====================
class Evento:
    def __init__(self, fecha, hora, descripcion):
        self.fecha = fecha
        self.hora = hora
        self.descripcion = descripcion


class Agenda:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def eliminar_evento(self, index):
        if 0 <= index < len(self.eventos):
            del self.eventos[index]


# =====================
# VISTA + CONTROLADOR
# =====================
class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        self.agenda = Agenda()

        # ===== Frame Lista =====
        frame_lista = tk.Frame(root)
        frame_lista.pack(pady=10)

        self.tree = ttk.Treeview(frame_lista, columns=("Fecha", "Hora", "Descripción"), show="headings")
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")

        self.tree.pack()

        # ===== Frame Entradas =====
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        tk.Label(frame_entrada, text="Fecha (dd/mm/aaaa):").grid(row=0, column=0)
        self.entry_fecha = tk.Entry(frame_entrada)
        self.entry_fecha.grid(row=0, column=1)

        tk.Label(frame_entrada, text="Hora:").grid(row=1, column=0)
        self.entry_hora = tk.Entry(frame_entrada)
        self.entry_hora.grid(row=1, column=1)

        tk.Label(frame_entrada, text="Descripción:").grid(row=2, column=0)
        self.entry_desc = tk.Entry(frame_entrada)
        self.entry_desc.grid(row=2, column=1)

        # ===== Frame Botones =====
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar Evento", command=self.agregar_evento).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Eliminar Evento", command=self.eliminar_evento).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=2, padx=5)

    # =====================
    # FUNCIONES
    # =====================
    def agregar_evento(self):
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        if not fecha or not hora or not descripcion:
            messagebox.showwarning("Error", "Todos los campos son obligatorios")
            return

        evento = Evento(fecha, hora, descripcion)
        self.agenda.agregar_evento(evento)

        self.tree.insert("", "end", values=(fecha, hora, descripcion))

        self.entry_fecha.delete(0, tk.END)
        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)

    def eliminar_evento(self):
        seleccion = self.tree.selection()

        if not seleccion:
            messagebox.showwarning("Error", "Seleccione un evento")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Eliminar evento?")
        if confirmar:
            index = self.tree.index(seleccion)
            self.agenda.eliminar_evento(index)
            self.tree.delete(seleccion)


# =====================
# EJECUCIÓN
# =====================
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()