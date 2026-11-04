"""
EJERCICIO 24: Diferencia total con reduce

ENUNCIADO:
Calcula la diferencia total en los valores de una lista. Usa reduce().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
from functools import reduce

def diferencia_total(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía.")
    # Se resta de izquierda a derecha: (((a - b) - c) - d).
    return reduce(lambda acumulado, numero: acumulado - numero, numeros)

if __name__ == "__main__":
    print(diferencia_total([20, 3, 2]))
