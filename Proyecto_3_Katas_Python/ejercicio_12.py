"""
EJERCICIO 12: Longitud de cada palabra con map

ENUNCIADO:
Recibe una frase y devuelve una lista con la longitud de cada palabra. Usa map().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def longitudes_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    print(longitudes_palabras(frase))
