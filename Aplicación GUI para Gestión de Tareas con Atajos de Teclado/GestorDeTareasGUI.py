import tkinter as tk
from tkinter import messagebox

class AppTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas PRO")
        self.root.geometry("450x550")
        self.root.configure(bg="#1e1e1e")

        # Lista de tareas (POO + estructura de datos)
        self.tareas = []

        # Crear interfaz
        self.crear_interfaz()

        # Configurar atajos de teclado
        self.configurar_atajos()

    # ---------------- INTERFAZ ----------------
    def crear_interfaz(self):
        # Campo de entrada
        self.entry = tk.Entry(self.root, font=("Arial", 14))
        self.entry.pack(pady=10, padx=10, fill=tk.X)

        # Lista de tareas
        self.lista = tk.Listbox(
            self.root,
            font=("Arial", 12),
            selectbackground="#4CAF50",
            bg="#2b2b2b",
            fg="white"
        )
        self.lista.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Evento doble clic
        self.lista.bind("<Double-Button-1>", self.completar_tarea)

        # Frame de botones
        frame_botones = tk.Frame(self.root, bg="#1e1e1e")
        frame_botones.pack(pady=10)

        tk.Button(frame_botones, text="Agregar", width=12, command=self.agregar_tarea).grid(row=0, column=0, padx=5)
        tk.Button(frame_botones, text="Completar", width=12, command=self.completar_tarea).grid(row=0, column=1, padx=5)
        tk.Button(frame_botones, text="Eliminar", width=12, command=self.eliminar_tarea).grid(row=0, column=2, padx=5)

    # ---------------- FUNCIONES ----------------
    def agregar_tarea(self, event=None):
        tarea = self.entry.get().strip()

        if tarea == "":
            messagebox.showwarning("Aviso", "Escribe una tarea")
            return

        self.tareas.append({
            "texto": tarea,
            "completada": False
        })

        self.actualizar_lista()
        self.entry.delete(0, tk.END)

    def completar_tarea(self, event=None):
        seleccion = self.lista.curselection()

        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona una tarea")
            return

        index = seleccion[0]
        self.tareas[index]["completada"] = True

        self.actualizar_lista()

    def eliminar_tarea(self, event=None):
        seleccion = self.lista.curselection()

        if not seleccion:
            messagebox.showwarning("Aviso", "Selecciona una tarea")
            return

        index = seleccion[0]
        del self.tareas[index]

        self.actualizar_lista()

    # ---------------- ACTUALIZAR LISTA ----------------
    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.tareas:
            texto = tarea["texto"]

            if tarea["completada"]:
                texto = "✔ " + texto  # feedback visual

            self.lista.insert(tk.END, texto)

    # ---------------- ATAJOS ----------------
    def configurar_atajos(self):
        self.root.bind("<Return>", self.agregar_tarea)   # Enter
        self.root.bind("<c>", self.completar_tarea)      # C
        self.root.bind("<Delete>", self.eliminar_tarea)  # Delete
        self.root.bind("<d>", self.eliminar_tarea)       # D
        self.root.bind("<Escape>", lambda e: self.root.quit())  # Esc


# ---------------- EJECUCIÓN ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AppTareas(root)
    root.mainloop()