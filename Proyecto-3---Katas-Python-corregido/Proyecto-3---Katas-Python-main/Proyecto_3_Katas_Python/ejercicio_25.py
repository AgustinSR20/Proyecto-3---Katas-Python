"""
EJERCICIO 25: Contar caracteres

ENUNCIADO:
Crea una función que cuente el número de caracteres en una cadena de texto dada.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def contar_caracteres(texto):
    # len cuenta también espacios y signos de puntuación.
    return len(texto)

if __name__ == "__main__":
    texto = input("Escribe un texto: ")
    print("Número de caracteres:", contar_caracteres(texto))
