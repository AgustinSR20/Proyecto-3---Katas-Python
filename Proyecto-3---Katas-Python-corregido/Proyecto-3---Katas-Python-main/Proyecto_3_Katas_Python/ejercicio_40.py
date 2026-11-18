"""
EJERCICIO 40: Precio final con cupón de descuento

ENUNCIADO:
Solicita precio original, pregunta si hay cupón sí/no, solicita el porcentaje si lo hay, valida que sea mayor que cero y calcula el precio final usando if, elif y else.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
def calcular_precio_final(precio, tiene_cupon, descuento=0):
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if tiene_cupon == "si":
        if not 0 < descuento <= 100:
            raise ValueError("El descuento debe ser mayor que 0 y como máximo 100.")
        precio_final = precio - (precio * descuento / 100)
    elif tiene_cupon == "no":
        precio_final = precio
    else:
        raise ValueError("Responde sí o no.")
    return precio_final

if __name__ == "__main__":
    try:
        precio = float(input("Precio original: "))
        respuesta = input("¿Tienes cupón? (sí/no): ").strip().lower()
        respuesta = "si" if respuesta in ("si", "sí") else respuesta
        descuento = 0
        if respuesta == "si":
            descuento = float(input("Porcentaje de descuento: "))
        total = calcular_precio_final(precio, respuesta, descuento)
        print(f"Precio final: {total:.2f} €")
    except ValueError as error:
        print("No se pudo calcular el precio:", error)
