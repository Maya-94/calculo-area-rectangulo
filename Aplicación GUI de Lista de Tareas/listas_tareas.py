# =============================
# APP LISTA DE TAREAS PRO MAX
# =============================
# Incluye:
# - Interfaz moderna DARK PRO
# - Tabla tipo Excel (Treeview)
# - Doble clic para completar
# - Persistencia JSON
# - POO

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

ARCHIVO = "tareas.json"

class AppTareas:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager PRO MAX")
        self.root.geometry("600x500")
        self.root.configure(bg="#1E1E2E")

        self.tareas = []
        self.cargar_tareas()

        self.estilo()
        self.crear_interfaz()
        self.actualizar_tabla()

    # ----------------------------
    # ESTILO MODERNO
    # ----------------------------
    def estilo(self):
        style = ttk.Style()
        style.theme_use("default")

        style.configure("Treeview",
                        background="#2A2A3C",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#2A2A3C")

        style.map('Treeview', background=[('selected', '#3A86FF')])

    # ----------------------------
    # INTERFAZ
    # ----------------------------
    def crear_interfaz(self):
        titulo = tk.Label(self.root, text="📋 Task Manager", font=("Arial", 18, "bold"), bg="#1E1E2E", fg="white")
        titulo.pack(pady=10)

        frame = tk.Frame(self.root, bg="#1E1E2E")
        frame.pack(pady=10)

        self.entrada = tk.Entry(frame, width=30, font=("Arial", 12))
        self.entrada.grid(row=0, column=0, padx=5)
        self.entrada.bind("<Return>", self.agregar_tarea)

        tk.Button(frame, text="➕", command=self.agregar_tarea, bg="#06D6A0", fg="black", width=4).grid(row=0, column=1)

        # TABLA
        columnas = ("Estado", "Tarea")
        self.tabla = ttk.Treeview(self.root, columns=columnas, show="headings")
        self.tabla.heading("Estado", text="✔")
        self.tabla.heading("Tarea", text="Tarea")

        self.tabla.column("Estado", width=50, anchor="center")
        self.tabla.column("Tarea", width=400)

        self.tabla.pack(pady=10)

        # EVENTO DOBLE CLICK
        self.tabla.bind("<Double-1>", self.doble_click)

        frame_btn = tk.Frame(self.root, bg="#1E1E2E")
        frame_btn.pack(pady=10)

        tk.Button(frame_btn, text="✔ Completar", command=self.marcar_completada, bg="#118AB2", fg="white").grid(row=0, column=0, padx=5)
        tk.Button(frame_btn, text="🗑 Eliminar", command=self.eliminar_tarea, bg="#EF476F", fg="white").grid(row=0, column=1, padx=5)

    # ----------------------------
    # FUNCIONES
    # ----------------------------
    def agregar_tarea(self, event=None):
        texto = self.entrada.get()
        if texto == "":
            messagebox.showwarning("Aviso", "Escribe una tarea")
            return

        self.tareas.append({"texto": texto, "completada": False})
        self.entrada.delete(0, tk.END)
        self.guardar_tareas()
        self.actualizar_tabla()

    def marcar_completada(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Aviso", "Selecciona una tarea")
            return

        index = int(self.tabla.item(seleccionado)['iid'])
        self.tareas[index]['completada'] = True
        self.guardar_tareas()
        self.actualizar_tabla()

    def doble_click(self, event):
        seleccionado = self.tabla.selection()
        if seleccionado:
            index = int(self.tabla.item(seleccionado)['iid'])
            self.tareas[index]['completada'] = not self.tareas[index]['completada']
            self.guardar_tareas()
            self.actualizar_tabla()

    def eliminar_tarea(self):
        seleccionado = self.tabla.selection()
        if not seleccionado:
            messagebox.showwarning("Aviso", "Selecciona una tarea")
            return

        index = int(self.tabla.item(seleccionado)['iid'])
        self.tareas.pop(index)
        self.guardar_tareas()
        self.actualizar_tabla()

    def actualizar_tabla(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)

        for i, tarea in enumerate(self.tareas):
            estado = "✔" if tarea['completada'] else ""
            self.tabla.insert("", "end", iid=i, values=(estado, tarea['texto']))

    # ----------------------------
    # PERSISTENCIA
    # ----------------------------
    def guardar_tareas(self):
        with open(ARCHIVO, "w") as f:
            json.dump(self.tareas, f)

    def cargar_tareas(self):
        if os.path.exists(ARCHIVO):
            with open(ARCHIVO, "r") as f:
                self.tareas = json.load(f)


# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AppTareas(root)
    root.mainloop()
