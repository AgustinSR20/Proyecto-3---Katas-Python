"""
EJERCICIO 32: Buscar puesto de empleado

ENUNCIADO:
Toma un nombre completo y una lista de empleados, busca el nombre y devuelve el puesto si existe; si no, indica que la persona no trabaja aquí.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def buscar_puesto(nombre_completo, empleados):
    for empleado in empleados:
        if empleado["nombre"].casefold() == nombre_completo.casefold():
            return empleado["puesto"]
    return "Esta persona no trabaja aquí."

if __name__ == "__main__":
    empleados = [
        {"nombre": "Ana García", "puesto": "Desarrolladora"},
        {"nombre": "Luis Pérez", "puesto": "Administrador"}
    ]
    print(buscar_puesto("Ana García", empleados))
    print(buscar_puesto("Pedro López", empleados))
