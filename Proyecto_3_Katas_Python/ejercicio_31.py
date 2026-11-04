"""
EJERCICIO 31: Buscar nombre introducido por el usuario

ENUNCIADO:
Solicita al usuario una lista de nombres y luego un nombre para buscar. Si está, muestra un mensaje; si no, lanza una excepción.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
class NombreNoEncontradoError(Exception):
    pass

def buscar_nombre():
    nombres = input("Introduce nombres separados por comas: ").split(",")
    nombres = [nombre.strip() for nombre in nombres if nombre.strip()]
    objetivo = input("¿Qué nombre quieres buscar? ").strip()
    if objetivo.casefold() not in [nombre.casefold() for nombre in nombres]:
        raise NombreNoEncontradoError(f"{objetivo} no está en la lista.")
    print(f"¡{objetivo} ha sido encontrado!")

if __name__ == "__main__":
    try:
        buscar_nombre()
    except NombreNoEncontradoError as error:
        print("Error:", error)
