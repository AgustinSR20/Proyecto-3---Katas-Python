"""
EJERCICIO 27: Promedio de una lista

ENUNCIADO:
Crea una función que calcule el promedio de una lista de números.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def calcular_promedio(numeros):
    if not numeros:
        raise ValueError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)

if __name__ == "__main__":
    print(calcular_promedio([4, 6, 8, 10]))
