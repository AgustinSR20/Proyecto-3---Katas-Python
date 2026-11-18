"""
EJERCICIO 20: Filtrar valores enteros

ENUNCIADO:
Para una lista con elementos integer y string, obtén una nueva lista solo con los valores int. Usa filter().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def solo_enteros(elementos):
    # type(x) is int evita considerar True y False como enteros.
    return list(filter(lambda elemento: type(elemento) is int, elementos))

if __name__ == "__main__":
    print(solo_enteros([1, "hola", 2, "3", 4, 5.5, True]))
