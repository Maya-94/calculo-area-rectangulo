# ===============================
# Programación Orientada a Objetos en Python
# Autor: María Pianda
# ===============================

# ---------- CLASE BASE ----------
class Persona:
    """
    Clase base que representa a una persona.
    Aplica el concepto de encapsulación.
    """

    def __init__(self, nombre, edad):
        self.nombre = nombre          # Atributo público
        self._edad = edad             # Atributo protegido (encapsulación)

    def presentarse(self):
        """
        Método que será sobrescrito (polimorfismo).
        """
        return f"Hola, soy {self.nombre} y tengo {self._edad} años."

    def get_edad(self):
        """
        Método para acceder al atributo encapsulado.
        """
        return self._edad


# ---------- CLASE DERIVADA ----------
class Estudiante(Persona):
    """
    Clase derivada que hereda de Persona.
    Aplica herencia y polimorfismo.
    """

    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)   # Llamada al constructor de la clase base
        self.carrera = carrera

    def presentarse(self):
        """
        Método sobrescrito (polimorfismo).
        """
        return (
            f"Hola, soy {self.nombre}, tengo {self._edad} años "
            f"y estudio la carrera de {self.carrera}."
        )


# ---------- PROGRAMA PRINCIPAL ----------
if __name__ == "__main__":
    # Creación de objetos (instancias)
    persona1 = Persona("Carlos", 30)
    estudiante1 = Estudiante("María", 20, "Ingeniería en Tecnologias de la Informacion")

    # Uso de métodos
    print(persona1.presentarse())
    print(estudiante1.presentarse())
