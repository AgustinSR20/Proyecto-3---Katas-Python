"""
EJERCICIO 18: Filtrar estudiantes con nota de 90 o más

ENUNCIADO:
Crea una lista de diccionarios con nombre, edad y calificación y usa filter para extraer estudiantes con calificación mayor o igual a 90.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def estudiantes_destacados(estudiantes):
    return list(filter(lambda estudiante: estudiante["calificacion"] >= 90, estudiantes))

if __name__ == "__main__":
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 21, "calificacion": 82},
        {"nombre": "Marta", "edad": 19, "calificacion": 90}
    ]
    print(estudiantes_destacados(estudiantes))
