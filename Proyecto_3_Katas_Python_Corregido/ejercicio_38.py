"""
EJERCICIO 38: Calificación en texto

ENUNCIADO:
Determina la calificación textual según la nota: 0-69 insuficiente, 70-79 bien, 80-89 muy bien, 90-100 excelente.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def calificacion_texto(nota):
    if not 0 <= nota <= 100:
        raise ValueError("La nota debe estar entre 0 y 100.")
    if nota < 70:
        return "insuficiente"
    elif nota < 80:
        return "bien"
    elif nota < 90:
        return "muy bien"
    return "excelente"

if __name__ == "__main__":
    try:
        nota = float(input("Introduce la calificación (0-100): "))
        print("Resultado:", calificacion_texto(nota))
    except ValueError as error:
        print("Dato no válido:", error)
