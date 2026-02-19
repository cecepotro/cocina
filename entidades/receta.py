from entidades.ingrediente import Ingrediente
from entidades.procedimiento import Procedimiento

class Receta:

    def __init__(self, nombre: str, porciones: int, ingredientes: list[Ingrediente], procedimientos: list[Procedimiento]):
        self.nombre = nombre
        self.porciones = porciones
        self.ingredientes = ingredientes
        self.procedimientos = procedimientos


    def calcular_precio_total(self) -> float:
        total = 0
        for i in self.ingredientes:
            total += i.precio
        return total
        