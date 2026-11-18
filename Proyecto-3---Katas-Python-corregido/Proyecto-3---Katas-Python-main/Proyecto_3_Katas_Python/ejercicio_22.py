"""
EJERCICIO 22: Producto total con reduce

ENUNCIADO:
Dada una lista numérica, obtén el producto total de los valores. Usa reduce().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
from functools import reduce

def producto_total(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    return reduce(lambda acumulado, numero: acumulado * numero, numeros)

if __name__ == "__main__":
    print(producto_total([2, 3, 4]))
