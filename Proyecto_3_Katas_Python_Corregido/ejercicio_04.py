"""
EJERCICIO 4: Diferencia entre dos listas con map

ENUNCIADO:
Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def diferencias(lista1, lista2):
    if len(lista1) != len(lista2):
        raise ValueError("Las dos listas deben tener la misma longitud.")
    # Se resta cada pareja de elementos que ocupa la misma posición.
    return list(map(lambda pareja: pareja[0] - pareja[1], zip(lista1, lista2)))

if __name__ == "__main__":
    print(diferencias([10, 20, 30], [1, 2, 3]))
