"""
EJERCICIO 7: Convertir lista de tuplas a strings

ENUNCIADO:
Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def tuplas_a_strings(lista_tuplas):
    # str convierte cada tupla completa en una cadena de texto.
    return list(map(str, lista_tuplas))

if __name__ == "__main__":
    datos = [(1, "Ana"), (2, "Luis"), (3, "Marta")]
    print(tuplas_a_strings(datos))
