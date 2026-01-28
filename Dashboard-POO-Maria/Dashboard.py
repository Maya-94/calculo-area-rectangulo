# Dashboard personalizado
# Autor: María Pianda
# Proyecto POO
# Funcionalidad: gestor de tareas

class Dashboard:

    def __init__(self):
        self.tareas = []

    def mostrar_menu(self):
        print("\n===== DASHBOARD POO =====")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Eliminar tarea")
        print("4. Salir")

    def agregar_tarea(self):
        nombre = input("Ingrese nombre de la tarea: ")
        self.tareas.append(nombre)
        print("Tarea agregada correctamente.")

    def ver_tareas(self):
        if not self.tareas:
            print("No hay tareas registradas.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i+1}. {tarea}")

    def eliminar_tarea(self):
        self.ver_tareas()
        try:
            indice = int(input("Número de tarea a eliminar: ")) - 1
            self.tareas.pop(indice)
            print("Tarea eliminada.")
        except:
            print("Error al eliminar tarea.")

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.agregar_tarea()
            elif opcion == "2":
                self.ver_tareas()
            elif opcion == "3":
                self.eliminar_tarea()
            elif opcion == "4":
                print("Saliendo...")
                break
            else:
                print("Opción inválida")


if __name__ == "__main__":
    app = Dashboard()
    app.ejecutar()
