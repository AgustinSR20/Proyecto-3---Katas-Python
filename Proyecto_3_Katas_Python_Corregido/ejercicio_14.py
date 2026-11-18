"""
EJERCICIO 14: Filtrar palabras por letra inicial

ENUNCIADO:
Retorna las palabras de una lista que comiencen con una letra específica. Usa filter().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def palabras_por_inicial(palabras, letra):
    return list(filter(lambda palabra: palabra.lower().startswith(letra.lower()), palabras))

if __name__ == "__main__":
    print(palabras_por_inicial(["casa", "coche", "perro", "camino"], "c"))
