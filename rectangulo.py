"""
Programa: Cálculo del área de un rectángulo
Descripción: Este programa utiliza Programación Orientada a Objetos para
calcular el área de un rectángulo a partir de la base y la altura ingresadas
por el usuario.
Autor: María Pianda
"""

class Rectangulo:
    """
    Clase que representa un rectángulo
    """

    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        """
        Calcula el área del rectángulo
        """
        return self.base * self.altura


def main():
    # Entrada de datos
    nombre_usuario: str = input("Ingrese su nombre: ")
    base: float = float(input("Ingrese la base del rectángulo: "))
    altura: float = float(input("Ingrese la altura del rectángulo: "))

    # Creación del objeto
    rectangulo = Rectangulo(base, altura)

    # Cálculo del área
    area: float = rectangulo.calcular_area()

    # Variable booleana
    area_valida: bool = area > 0

    # Salida de resultados
    print("\nResultados")
    print("Usuario:", nombre_usuario)
    print("Área del rectángulo:", area)

    if area_valida:
        print("El área calculada es válida.")
    else:
        print("El área calculada no es válida.")


# Ejecución del programa
main()
