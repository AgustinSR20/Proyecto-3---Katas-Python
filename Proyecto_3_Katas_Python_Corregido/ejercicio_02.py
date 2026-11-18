"""
EJERCICIO 2: Duplicar números con map

ENUNCIADO:
Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def duplicar_numeros(numeros):
    # map aplica la función indicada a cada elemento de la lista.
    return list(map(lambda numero: numero * 2, numeros))

if __name__ == "__main__":
    numeros = [1, 2, 3, 4, 5]
    print("Original:", numeros)
    print("Duplicados:", duplicar_numeros(numeros))
