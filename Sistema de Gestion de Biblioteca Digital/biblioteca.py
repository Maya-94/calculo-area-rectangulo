# ==============================
# SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL
# ==============================

# ---------- CLASE LIBRO ----------
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Tupla para titulo y autor (inmutable)
        self.datos = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"Título: {self.datos[0]}, Autor: {self.datos[1]}, Categoría: {self.categoria}, ISBN: {self.isbn}"


# ---------- CLASE USUARIO ----------
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para libros prestados

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}"


# ---------- CLASE BIBLIOTECA ----------
class Biblioteca:
    def __init__(self):
        self.libros = {}        # Diccionario: ISBN -> Libro
        self.usuarios = {}      # Diccionario: ID -> Usuario
        self.ids_usuarios = set()  # Conjunto para IDs únicos

    # Añadir libro
    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro
        print("Libro añadido correctamente.")

    # Quitar libro
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            print("Libro eliminado correctamente.")
        else:
            print("El libro no existe.")

    # Registrar usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print("Usuario registrado correctamente.")
        else:
            print("Error: ID ya registrado.")

    # Eliminar usuario
    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)
            print("Usuario eliminado.")
        else:
            print("Usuario no encontrado.")

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros and id_usuario in self.usuarios:
            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]
            usuario.libros_prestados.append(libro)
            del self.libros[isbn]
            print("Libro prestado correctamente.")
        else:
            print("Libro o usuario no encontrado.")

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    print("Libro devuelto correctamente.")
                    return
            print("El usuario no tiene ese libro.")
        else:
            print("Usuario no encontrado.")

    # Buscar libro
    def buscar_libro(self, criterio):
        resultados = []
        for libro in self.libros.values():
            if (criterio.lower() in libro.datos[0].lower() or
                criterio.lower() in libro.datos[1].lower() or
                criterio.lower() in libro.categoria.lower()):
                resultados.append(libro)

        if resultados:
            print("Resultados encontrados:")
            for libro in resultados:
                print(libro)
        else:
            print("No se encontraron libros.")

    # Listar libros prestados
    def listar_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("El usuario no tiene libros prestados.")
        else:
            print("Usuario no encontrado.")


# ---------- PRUEBA DEL SISTEMA ----------
if __name__ == "__main__":

    biblioteca = Biblioteca()

    # Crear libros
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "123")
    libro2 = Libro("El Principito", "Antoine de Saint-Exupéry", "Ficción", "456")

    # Añadir libros
    biblioteca.añadir_libro(libro1)
    biblioteca.añadir_libro(libro2)

    # Crear usuario
    usuario1 = Usuario("María", "001")

    # Registrar usuario
    biblioteca.registrar_usuario(usuario1)

    # Prestar libro
    biblioteca.prestar_libro("123", "001")

    # Listar libros prestados
    biblioteca.listar_prestados("001")

    # Devolver libro
    biblioteca.devolver_libro("123", "001")

    # Buscar libro
    biblioteca.buscar_libro("Principito")