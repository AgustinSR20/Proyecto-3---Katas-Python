"""
EJERCICIO 23: Concatenar palabras con reduce

ENUNCIADO:
Concatena una lista de palabras. Usa reduce().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
from functools import reduce

def concatenar_palabras(palabras):
    if not palabras:
        return ""
    return reduce(lambda acumulado, palabra: acumulado + palabra, palabras)

if __name__ == "__main__":
    print(concatenar_palabras(["Hola", " ", "mundo", "!"]))
