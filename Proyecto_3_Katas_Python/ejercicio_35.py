"""
EJERCICIO 35: Clase UsuarioBanco

ENUNCIADO:
Representa un usuario bancario con nombre, saldo y cuenta corriente. Implementa retirar_dinero, transferir_dinero y agregar_dinero. Caso: Alicia 100 y Bob 50; agregar 20 a Bob; transferir 80 de Bob a Alicia; retirar 50 de Alicia.

Explicación:
Este archivo es independiente. Puedes ejecutarlo directamente.
"""
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        if saldo < 0:
            raise ValueError("El saldo inicial no puede ser negativo.")
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError("El usuario no tiene cuenta corriente.")
        if cantidad <= 0 or cantidad > self.saldo:
            raise ValueError("Cantidad no válida o saldo insuficiente.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        # Primero se descuenta del origen; luego se ingresa al destinatario.
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.saldo += cantidad

if __name__ == "__main__":
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)                  # Bob tiene ahora 70.
    # El enunciado pide transferir 80 desde Bob, pero solo tiene 70.
    # Se captura el error para que el programa pueda explicar el problema.
    try:
        bob.transferir_dinero(alicia, 80)
    except ValueError as error:
        print("No se pudo transferir:", error)
    # Para completar el caso de uso literalmente, se añade saldo a Bob.
    bob.agregar_dinero(10)                  # Bob llega a 80.
    bob.transferir_dinero(alicia, 80)       # Alicia llega a 180; Bob a 0.
    alicia.retirar_dinero(50)               # Alicia termina con 130.
    print(f"{alicia.nombre}: {alicia.saldo}")
    print(f"{bob.nombre}: {bob.saldo}")
