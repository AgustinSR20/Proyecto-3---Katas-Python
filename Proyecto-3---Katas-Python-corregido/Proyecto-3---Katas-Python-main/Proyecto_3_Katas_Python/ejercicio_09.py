"""
EJERCICIO 9: Filtrar mascotas prohibidas

ENUNCIADO:
Toma una lista de nombres de mascotas y devuelve otra excluyendo ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa filter().

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
MASCOTAS_PROHIBIDAS = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def filtrar_mascotas(mascotas):
    prohibidas = {nombre.casefold() for nombre in MASCOTAS_PROHIBIDAS}
    return list(filter(lambda mascota: mascota.casefold() not in prohibidas, mascotas))

if __name__ == "__main__":
    lista = ["Perro", "Tigre", "Gato", "Oso", "Canario"]
    print(filtrar_mascotas(lista))
