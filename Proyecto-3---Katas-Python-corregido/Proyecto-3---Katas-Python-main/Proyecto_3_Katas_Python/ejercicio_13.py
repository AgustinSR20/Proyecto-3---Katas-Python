"""
EJERCICIO 13: Pares de mayúsculas y minúsculas

ENUNCIADO:
Para un conjunto de caracteres, devuelve una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden repetirse. Usa map().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def pares_mayus_minus(caracteres):
    # dict.fromkeys elimina duplicados conservando el orden de aparición.
    unicos = list(dict.fromkeys(caracteres))
    return list(map(lambda letra: (letra.upper(), letra.lower()), unicos))

if __name__ == "__main__":
    print(pares_mayus_minus(["a", "b", "a", "C", "c"]))
