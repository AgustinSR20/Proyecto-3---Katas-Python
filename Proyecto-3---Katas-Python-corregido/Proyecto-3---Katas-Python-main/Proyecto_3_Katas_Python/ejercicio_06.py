"""
EJERCICIO 6: Factorial recursivo

ENUNCIADO:
Escribe una función que calcule el factorial de un número de manera recursiva.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def factorial(numero):
    if not isinstance(numero, int) or numero < 0:
        raise ValueError("El número debe ser un entero no negativo.")
    # Caso base: 0! y 1! valen 1. Evita llamadas infinitas.
    if numero <= 1:
        return 1
    # Caso recursivo: n! = n * (n-1)!
    return numero * factorial(numero - 1)

if __name__ == "__main__":
    n = int(input("Introduce un entero no negativo: "))
    print(f"{n}! = {factorial(n)}")
