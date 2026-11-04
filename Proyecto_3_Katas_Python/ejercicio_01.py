"""
EJERCICIO 1: Frecuencia de letras

ENUNCIADO:
Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def frecuencia_letras(texto):
    frecuencias = {}
    for letra in texto.lower():
        if letra != " ":
            # get devuelve 0 si la letra todavía no existe en el diccionario.
            frecuencias[letra] = frecuencias.get(letra, 0) + 1
    return frecuencias

if __name__ == "__main__":
    frase = input("Escribe una frase: ")
    print("Frecuencia de letras:", frecuencia_letras(frase))
