"""
EJERCICIO 8: División con control de excepciones

ENUNCIADO:
Pide al usuario dos números e intenta dividirlos. Si introduce un valor no numérico o divide por cero, maneja las excepciones e indica si la división tuvo éxito.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def dividir_desde_teclado():
    try:
        numero1 = float(input("Primer número: "))
        numero2 = float(input("Segundo número: "))
        resultado = numero1 / numero2
    except ValueError:
        print("Error: debes introducir números válidos.")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    else:
        print("La división se ha realizado correctamente:", resultado)

if __name__ == "__main__":
    dividir_desde_teclado()
