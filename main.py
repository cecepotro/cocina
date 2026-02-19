from entidades.ingrediente import Ingrediente
from entidades.procedimiento import Procedimiento
from entidades.receta import Receta

ingrediente1 = Ingrediente("Carne molida", "200 gr", 100)
ingrediente2 = Ingrediente("Tomate", "1 pieza", 12)
ingrediente3 = Ingrediente("Queso amarillo", "10 gramos", 43)

ingredientes = [ingrediente1, ingrediente2, ingrediente3]


proc1 = Procedimiento(1, "Preparar la carne a 180°C")
proc2 = Procedimiento(2, "Calentar el pan en una vaporera")

procedimientos = [proc1, proc2]

object1 = Receta("Hamburguesa", 1,  ingredientes, procedimientos)

precio_total = object1.calcular_precio_total()

print(f"El precio total de la receta {precio_total}")
print("")