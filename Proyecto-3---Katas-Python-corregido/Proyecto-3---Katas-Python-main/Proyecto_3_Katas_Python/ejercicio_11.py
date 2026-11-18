"""
EJERCICIO 11: Validar edad

ENUNCIADO:
Pide al usuario su edad. Si introduce un valor no numérico o fuera del rango esperado (menor que 0 o mayor que 120), maneja las excepciones adecuadamente.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if not 0 <= edad <= 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
    except ValueError as error:
        print("Edad no válida:", error)
    else:
        print("Edad válida:", edad)

if __name__ == "__main__":
    pedir_edad()
