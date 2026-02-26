import json

# =========================
# CLASE PRODUCTO
# =========================
class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_cantidad(self, cantidad):
        self.cantidad = cantidad

    def actualizar_precio(self, precio):
        self.precio = precio

    def mostrar_info(self):
        return f"ID: {self.id} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


# =========================
# CLASE INVENTARIO
# =========================
class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            print("❌ Error: ID ya existe.")
        else:
            self.productos[producto.id] = producto
            print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("✅ Producto eliminado.")
        else:
            print("❌ Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].actualizar_cantidad(cantidad)
            if precio is not None:
                self.productos[id].actualizar_precio(precio)
            print("✅ Producto actualizado.")
        else:
            print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            p for p in self.productos.values()
            if nombre.lower() in p.nombre.lower()
        ]

        if encontrados:
            print("\n🔎 Resultados:")
            for p in encontrados:
                print(p.mostrar_info())
        else:
            print("❌ No se encontraron productos.")

    def mostrar_todos(self):
        if self.productos:
            print("\n📦 Inventario:")
            for producto in self.productos.values():
                print(producto.mostrar_info())
        else:
            print("📦 Inventario vacío.")

    def guardar_archivo(self, archivo):
        data = {
            id: {
                "nombre": p.nombre,
                "cantidad": p.cantidad,
                "precio": p.precio
            }
            for id, p in self.productos.items()
        }

        with open(archivo, "w") as f:
            json.dump(data, f, indent=4)

        print("✅ Inventario guardado en archivo.")

    def cargar_archivo(self, archivo):
        try:
            with open(archivo, "r") as f:
                data = json.load(f)

            for id, info in data.items():
                producto = Producto(
                    id,
                    info["nombre"],
                    info["cantidad"],
                    info["precio"]
                )
                self.productos[id] = producto

            print("✅ Inventario cargado desde archivo.")
        except FileNotFoundError:
            print("⚠ Archivo no encontrado. Se creará uno nuevo.")


# =========================
# MENÚ INTERACTIVO
# =========================
def menu():
    inventario = Inventario()
    archivo = "inventario.json"

    inventario.cargar_archivo(archivo)

    while True:
        print("\n===== SISTEMA AVANZADO DE INVENTARIO =====")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar por nombre")
        print("5. Mostrar todos")
        print("6. Guardar inventario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == "2":
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == "3":
            id = input("ID del producto: ")

            cantidad = input("Nueva cantidad (enter para omitir): ")
            precio = input("Nuevo precio (enter para omitir): ")

            inventario.actualizar_producto(
                id,
                int(cantidad) if cantidad else None,
                float(precio) if precio else None
            )

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_archivo(archivo)

        elif opcion == "7":
            inventario.guardar_archivo(archivo)
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida.")


# =========================
# EJECUCIÓN DEL PROGRAMA
# =========================
menu()