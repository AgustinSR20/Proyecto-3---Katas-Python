"""
EJERCICIO 10: Promedio con excepción personalizada

ENUNCIADO:
Crea una función que calcule el promedio de una lista. Si está vacía, lanza una excepción personalizada y maneja el error adecuadamente.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
class ListaVaciaError(Exception):
    """Error propio para indicar que no hay números que promediar."""
    pass

def promedio(numeros):
    if len(numeros) == 0:
        raise ListaVaciaError("No se puede calcular el promedio de una lista vacía.")
    return sum(numeros) / len(numeros)

if __name__ == "__main__":
    try:
        print("Promedio:", promedio([5, 7, 8, 10]))
        print("Promedio:", promedio([]))
    except ListaVaciaError as error:
        print("Error:", error)
