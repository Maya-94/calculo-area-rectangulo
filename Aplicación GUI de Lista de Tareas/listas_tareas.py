import tkinter as tk
from tkinter import messagebox

class AppTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x400")

        self.tareas = []

        self.crear_widgets()

    def crear_widgets(self):
        self.entrada = tk.Entry(self.root, width=30)
        self.entrada.pack(pady=10)
        self.entrada.bind("<Return>", self.evento_enter)

        self.lista = tk.Listbox(self.root, width=40, height=10)
        self.lista.pack(pady=10)

        tk.Button(self.root, text="Añadir Tarea", command=self.agregar_tarea).pack(pady=5)
        tk.Button(self.root, text="Marcar como Completada", command=self.marcar_completada).pack(pady=5)
        tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea).pack(pady=5)

    def agregar_tarea(self):
        tarea = self.entrada.get()

        if tarea == "":
            messagebox.showwarning("Advertencia", "Escribe una tarea")
            return

        self.tareas.append({"texto": tarea, "completada": False})
        self.actualizar_lista()
        self.entrada.delete(0, tk.END)

    def marcar_completada(self):
        try:
            indice = self.lista.curselection()[0]
            self.tareas[indice]["completada"] = True
            self.actualizar_lista()
        except:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")

    def eliminar_tarea(self):
        try:
            indice = self.lista.curselection()[0]
            self.tareas.pop(indice)
            self.actualizar_lista()
        except:
            messagebox.showwarning("Advertencia", "Selecciona una tarea")

    def actualizar_lista(self):
        self.lista.delete(0, tk.END)

        for tarea in self.tareas:
            if tarea["completada"]:
                texto = "✔ " + tarea["texto"]
            else:
                texto = tarea["texto"]

            self.lista.insert(tk.END, texto)

    def evento_enter(self, event):
        self.agregar_tarea()


if __name__ == "__main__":
    root = tk.Tk()
    app = AppTareas(root)
    root.mainloop()