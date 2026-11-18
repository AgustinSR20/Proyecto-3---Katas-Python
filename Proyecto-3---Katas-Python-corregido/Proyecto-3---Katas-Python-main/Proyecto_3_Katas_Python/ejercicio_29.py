"""
EJERCICIO 29: Enmascarar caracteres excepto los últimos cuatro

ENUNCIADO:
Convierte una variable en una cadena y enmascara todos los caracteres con # excepto los últimos cuatro.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def enmascarar(valor):
    texto = str(valor)
    if len(texto) <= 4:
        return texto
    return "#" * (len(texto) - 4) + texto[-4:]

if __name__ == "__main__":
    print(enmascarar("123456789"))
    print(enmascarar(987654321))
