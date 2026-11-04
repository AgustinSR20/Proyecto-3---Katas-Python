"""
EJERCICIO 16: Palabras más largas que n

ENUNCIADO:
Toma una cadena de texto y un entero n y devuelve las palabras que sean más largas que n. Usa filter().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def palabras_mas_largas(texto, n):
    if n < 0:
        raise ValueError("n no puede ser negativo.")
    palabras = texto.split()
    return list(filter(lambda palabra: len(palabra) > n, palabras))

if __name__ == "__main__":
    print(palabras_mas_largas("Python es un lenguaje muy interesante", 4))
