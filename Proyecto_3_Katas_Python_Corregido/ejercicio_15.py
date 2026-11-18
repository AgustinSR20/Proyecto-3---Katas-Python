"""
EJERCICIO 15: Lambda que suma tres

ENUNCIADO:
Crea una función lambda que sume 3 a cada número de una lista dada.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
sumar_tres = lambda numeros: list(map(lambda numero: numero + 3, numeros))

if __name__ == "__main__":
    print(sumar_tres([1, 2, 3, 4]))
