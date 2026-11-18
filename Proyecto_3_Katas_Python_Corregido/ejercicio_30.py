"""
EJERCICIO 30: Comprobar anagramas

ENUNCIADO:
Determina si dos palabras son anagramas: están formadas por las mismas letras en diferente orden.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def son_anagramas(palabra1, palabra2):
    # Se ignoran mayúsculas, espacios y caracteres de separación.
    limpiar = lambda texto: sorted(c for c in texto.casefold() if c.isalnum())
    return limpiar(palabra1) == limpiar(palabra2)

if __name__ == "__main__":
    print(son_anagramas("Roma", "Amor"))
    print(son_anagramas("Python", "Java"))
