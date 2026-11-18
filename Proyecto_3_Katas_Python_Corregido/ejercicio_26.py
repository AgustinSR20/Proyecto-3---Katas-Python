"""
EJERCICIO 26: Resto de división con lambda

ENUNCIADO:
Crea una función lambda que calcule el resto de la división entre dos números dados.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
resto = lambda dividendo, divisor: dividendo % divisor

if __name__ == "__main__":
    try:
        a = int(input("Dividendo: "))
        b = int(input("Divisor: "))
        print("Resto:", resto(a, b))
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    except ValueError:
        print("Debes introducir números enteros.")
