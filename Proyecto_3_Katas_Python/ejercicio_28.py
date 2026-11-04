"""
EJERCICIO 28: Encontrar primer elemento duplicado

ENUNCIADO:
Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def primer_duplicado(elementos):
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None  # None significa que no se encontró ningún duplicado.

if __name__ == "__main__":
    print(primer_duplicado([1, 2, 3, 2, 4, 1]))
    print(primer_duplicado(["a", "b", "c"]))
