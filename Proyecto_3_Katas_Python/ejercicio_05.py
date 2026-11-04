"""
EJERCICIO 5: Media y estado de aprobado

ENUNCIADO:
Escribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado (por defecto 5). La función debe calcular la media y determinar si es mayor o igual que nota_aprobado. Debe devolver una tupla con la media y el estado.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def evaluar_notas(notas, nota_aprobado=5):
    if not notas:
        raise ValueError("La lista de notas no puede estar vacía.")
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado

if __name__ == "__main__":
    print(evaluar_notas([6, 7, 4, 8]))
    print(evaluar_notas([3, 4, 2], 5))
