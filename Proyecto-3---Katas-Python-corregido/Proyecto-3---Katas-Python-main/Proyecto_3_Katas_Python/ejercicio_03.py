"""
EJERCICIO 3: Buscar palabras que contienen otra

ENUNCIADO:
Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def palabras_que_contienen(palabras, objetivo):
    return [palabra for palabra in palabras if objetivo.lower() in palabra.lower()]

if __name__ == "__main__":
    palabras = ["perro", "perrito", "gato", "perrera"]
    print(palabras_que_contienen(palabras, "per"))
