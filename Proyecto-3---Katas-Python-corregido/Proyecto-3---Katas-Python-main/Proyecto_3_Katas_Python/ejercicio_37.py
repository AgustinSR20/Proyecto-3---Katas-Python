"""
EJERCICIO 37: Determinar momento del día

ENUNCIADO:
Indica si es de noche, de día o de tarde según la hora proporcionada por el usuario.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def momento_del_dia(hora):
    if not 0 <= hora <= 23:
        raise ValueError("La hora debe estar entre 0 y 23.")
    if 6 <= hora < 12:
        return "día (mañana)"
    elif 12 <= hora < 20:
        return "tarde"
    else:
        return "noche"

if __name__ == "__main__":
    try:
        hora = int(input("Introduce la hora (0-23): "))
        print("Es de", momento_del_dia(hora))
    except ValueError as error:
        print("Dato no válido:", error)
