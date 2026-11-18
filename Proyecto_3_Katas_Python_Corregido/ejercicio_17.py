"""
EJERCICIO 17: Convertir dígitos en número con reduce

ENUNCIADO:
Toma una lista de dígitos y devuelve el número correspondiente. Por ejemplo, [5,7,2] corresponde al número 572. Usa reduce().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
from functools import reduce

def digitos_a_numero(digitos):
    if not digitos:
        raise ValueError("La lista no puede estar vacía.")
    if any(not isinstance(d, int) or not 0 <= d <= 9 for d in digitos):
        raise ValueError("Todos los elementos deben ser dígitos enteros entre 0 y 9.")
    return reduce(lambda acumulado, digito: acumulado * 10 + digito, digitos)

if __name__ == "__main__":
    print(digitos_a_numero([5, 7, 2]))
