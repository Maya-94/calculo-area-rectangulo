class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}"

    @staticmethod
    def desde_linea(linea):
        partes = linea.strip().split(',')
        if len(partes) != 4:
            raise ValueError("Formato de linea invalido")
        return Producto(partes[0], partes[1], int(partes[2]), float(partes[3]))


class Inventario:
    def __init__(self, archivo='inventario.txt'):
        self.archivo = archivo
        self.productos = {}
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        try:
            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    producto = Producto.desde_linea(linea)
                    self.productos[producto.id_producto] = producto
            print("Inventario cargado correctamente.")
        except FileNotFoundError:
            print("Archivo no encontrado. Se creará uno nuevo al guardar.")
        except PermissionError:
            print("Error: No hay permisos para leer el archivo.")
        except Exception as e:
            print(f"Error inesperado al cargar archivo: {e}")

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for producto in self.productos.values():
                    f.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No hay permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar archivo: {e}")

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            raise ValueError("El producto ya existe")
        self.productos[producto.id_producto] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado")
        del self.productos[id_producto]
        self.guardar_en_archivo()

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto not in self.productos:
            raise ValueError("Producto no encontrado")
        if cantidad is not None:
            self.productos[id_producto].cantidad = cantidad
        if precio is not None:
            self.productos[id_producto].precio = precio
        self.guardar_en_archivo()

    def mostrar_productos(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        for p in self.productos.values():
            print(f"ID: {p.id_producto} | Nombre: {p.nombre} | Cantidad: {p.cantidad} | Precio: {p.precio}")


def menu():
    inventario = Inventario()

    while True:
        print("\n--- MENU INVENTARIO ---")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Mostrar productos")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))
                producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            elif opcion == '2':
                id_producto = input("ID del producto a eliminar: ")
                inventario.eliminar_producto(id_producto)

            elif opcion == '3':
                id_producto = input("ID del producto a actualizar: ")
                cantidad = input("Nueva cantidad (enter para omitir): ")
                precio = input("Nuevo precio (enter para omitir): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_producto, cantidad, precio)

            elif opcion == '4':
                inventario.mostrar_productos()

            elif opcion == '5':
                print("Saliendo del sistema...")
                break

            else:
                print("Opción inválida")

        except ValueError as e:
            print(f"Error de validación: {e}")
        except Exception as e:
            print(f"Error inesperado: {e}")


if __name__ == '__main__':
    menu()
