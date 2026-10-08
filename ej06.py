# Creamos la clase para manejar la cuenta corriente
class CuentaCorriente:
    # Guardamos el nombre del cliente y el saldo inicial
    def __init__(self, cliente, saldo):
        self.cliente = cliente
        self.saldo = saldo
    # Este metodo sirve para agregar dinero a la cuenta
    def acreditar(self, monto):
        # Verificamos que el monto sea positivo
        if monto > 0:
            self.saldo += monto
            print(f"Se acreditaron {monto:,.0f} Gs.")
        # Si no es positivo mostramos un aviso
        else:
            print("El monto debe ser positivo.")
    # Este metodo sirve para registrar una compra
    def consumir(self, monto):
        # Verificamos que el consumo sea valido
        if monto <= 0:
            print("El consumo debe ser positivo.")
        # Si hay suficiente saldo realizamos la compra
        elif monto <= self.saldo:
            self.saldo -= monto
            print(f"Compra realizada por {monto:,.0f} Gs.")
        # Si no hay suficiente saldo rechazamos la compra
        else:
            print("Compra rechazada: saldo insuficiente.")
    # Mostramos el cliente y su saldo actual
    def __str__(self):
        return f"Cliente: {self.cliente} | Saldo: {self.saldo:,.0f} Gs."
# Creamos una cuenta con un saldo inicial
cuenta = CuentaCorriente("Carlos Benitez", 100000)
# Mostramos el saldo inicial
print(cuenta)
# Agregamos dinero a la cuenta
cuenta.acreditar(50000)
print(cuenta)
# Hacemos una compra que si se puede realizar
cuenta.consumir(80000)
print(cuenta)
# Intentamos hacer una compra sin saldo suficiente
cuenta.consumir(100000)
print(cuenta)
# Probamos agregar un monto negativo
cuenta.acreditar(-5000)
print(cuenta)
