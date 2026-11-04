"""
EJERCICIO 33: Sumar elementos correspondientes de dos listas

ENUNCIADO:
Crea una función lambda que sume elementos correspondientes de dos listas dadas.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
sumar_listas = lambda lista1, lista2: list(map(lambda pareja: pareja[0] + pareja[1], zip(lista1, lista2)))

if __name__ == "__main__":
    print(sumar_listas([1, 2, 3], [10, 20, 30]))
