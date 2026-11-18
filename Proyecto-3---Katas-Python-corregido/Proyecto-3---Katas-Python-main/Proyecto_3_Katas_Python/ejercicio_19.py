"""
EJERCICIO 19: Lambda para filtrar impares

ENUNCIADO:
Crea una función lambda que filtre los números impares de una lista dada.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
filtrar_impares = lambda numeros: list(filter(lambda numero: numero % 2 != 0, numeros))

if __name__ == "__main__":
    print(filtrar_impares([1, 2, 3, 4, 5, 6, 7]))
