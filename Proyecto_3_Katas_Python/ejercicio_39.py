"""
EJERCICIO 39: Calcular área de figuras

ENUNCIADO:
Toma figura ("rectangulo", "circulo" o "triangulo") y datos (tupla con las medidas necesarias) y devuelve el área.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
import math

def calcular_area(figura, datos):
    if figura == "rectangulo":
        if len(datos) != 2:
            raise ValueError("El rectángulo necesita base y altura.")
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        if len(datos) != 1:
            raise ValueError("El círculo necesita el radio.")
        (radio,) = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        if len(datos) != 2:
            raise ValueError("El triángulo necesita base y altura.")
        base, altura = datos
        return (base * altura) / 2
    else:
        raise ValueError("Figura no reconocida.")

if __name__ == "__main__":
    print("Rectángulo:", calcular_area("rectangulo", (5, 3)))
    print("Círculo:", calcular_area("circulo", (2,)))
    print("Triángulo:", calcular_area("triangulo", (4, 6)))
