"""
EJERCICIO 21: Cubo con lambda

ENUNCIADO:
Crea una función que calcule el cubo de un número dado mediante una función lambda.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
cubo = lambda numero: numero ** 3

if __name__ == "__main__":
    numero = float(input("Introduce un número: "))
    print("Su cubo es:", cubo(numero))
