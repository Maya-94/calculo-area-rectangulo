from producto import Producto

class Inventario:
    def __init__(self):
        # Lista que almacenará objetos Producto
        self.productos = []

    def añadir_producto(self, producto):
        # Verificar que el ID no exista
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("❌ Error: El ID ya existe.")
                return

        self.productos.append(producto)
        print("✅ Producto añadido correctamente.")

    def eliminar_producto(self, id):
        for p in self.productos:
            if p.get_id() == id:
                self.productos.remove(p)
                print("✅ Producto eliminado.")
                return

        print("❌ Producto no encontrado.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)

                if precio is not None:
                    p.set_precio(precio)

                print("✅ Producto actualizado.")
                return

        print("❌ Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = []

        for p in self.productos:
            if nombre.lower() in p.get_nombre().lower():
                encontrados.append(p)

        if encontrados:
            print("\n🔎 Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("❌ No se encontraron productos.")

    def mostrar_productos(self):
        if not self.productos:
            print("📦 Inventario vacío.")
            return

        print("\n📋 Inventario:")
        for p in self.productos:
            print(p)
