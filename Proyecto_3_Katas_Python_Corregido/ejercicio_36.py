"""
EJERCICIO 36: Procesar texto

ENUNCIADO:
Crea procesar_texto con opciones contar, reemplazar y eliminar. contar devuelve frecuencias de palabras; reemplazar sustituye palabra_original por palabra_nueva; eliminar borra una palabra. Recibe argumentos variables según la opción.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def contar_palabras(texto):
    frecuencias = {}
    for palabra in texto.split():
        palabra = palabra.strip(".,;:!?¿¡").lower()
        if palabra:
            frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    return frecuencias

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    # Se separa y vuelve a unir para evitar espacios dobles.
    return " ".join(p for p in texto.split() if p != palabra)

def procesar_texto(texto, opcion, *argumentos):
    if opcion == "contar":
        return contar_palabras(texto)
    if opcion == "reemplazar":
        if len(argumentos) != 2:
            raise ValueError("La opción reemplazar necesita palabra_original y palabra_nueva.")
        return reemplazar_palabras(texto, argumentos[0], argumentos[1])
    if opcion == "eliminar":
        if len(argumentos) != 1:
            raise ValueError("La opción eliminar necesita la palabra que se borrará.")
        return eliminar_palabra(texto, argumentos[0])
    raise ValueError("Opción no válida: usa contar, reemplazar o eliminar.")

if __name__ == "__main__":
    frase = "Python es genial y Python es útil"
    print("Contar:", procesar_texto(frase, "contar"))
    print("Reemplazar:", procesar_texto(frase, "reemplazar", "genial", "fantástico"))
    print("Eliminar:", procesar_texto(frase, "eliminar", "y"))
