"""
EJERCICIO 34: Clase Arbol

ENUNCIADO:
Define un árbol con tronco y ramas. Implementa crecer_tronco, nueva_rama, crecer_ramas, quitar_rama e info_arbol. Caso de uso: crear árbol, crecer tronco, añadir rama, crecer ramas, añadir dos ramas, quitar la rama de posición 2 y mostrar información.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        # Recorremos los índices para aumentar cada rama existente.
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        # Las posiciones de Python empiezan en 0.
        if not 0 <= posicion < len(self.ramas):
            raise IndexError("No existe una rama en esa posición.")
        self.ramas.pop(posicion)

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas.copy()
        }

if __name__ == "__main__":
    arbol = Arbol()             # a. Crear árbol.
    arbol.crecer_tronco()       # b. El tronco pasa de 1 a 2.
    arbol.nueva_rama()          # c. Añadir una rama.
    arbol.crecer_ramas()        # d. La rama pasa de 1 a 2.
    arbol.nueva_rama()          # e. Añadir dos ramas nuevas.
    arbol.nueva_rama()
    arbol.quitar_rama(2)        # f. Quitar posición 2 (tercera rama).
    print(arbol.info_arbol())   # g. Mostrar información.
