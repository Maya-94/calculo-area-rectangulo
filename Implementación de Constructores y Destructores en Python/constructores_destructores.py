class ArchivoTexto:
    """
    Clase que demuestra el uso de constructor y destructor en Python.
    """

    def __init__(self, nombre_archivo):
        """
        CONSTRUCTOR
        Se ejecuta automáticamente cuando se crea el objeto.
        Inicializa los atributos del objeto.
        """
        self.nombre_archivo = nombre_archivo
        self.archivo = open(self.nombre_archivo, 'w')
        print(f"[Constructor] Archivo '{self.nombre_archivo}' abierto correctamente.")

    def escribir(self, texto):
        """
        Método para escribir texto en el archivo.
        """
        self.archivo.write(texto + "\n")
        print("[Método] Texto escrito en el archivo.")

    def __del__(self):
        """
        DESTRUCTOR
        Se ejecuta cuando el objeto se elimina o el programa finaliza.
        Libera recursos (cierra el archivo).
        """
        self.archivo.close()
        print(f"[Destructor] Archivo '{self.nombre_archivo}' cerrado correctamente.")


# Programa principal
if __name__ == "__main__":
    print("Inicio del programa")

    archivo1 = ArchivoTexto("ejemplo.txt")
    archivo1.escribir("Hola, este es un ejemplo de constructores y destructores en Python.")

    # Eliminamos explícitamente el objeto para activar el destructor
    del archivo1

    print("Fin del programa")
