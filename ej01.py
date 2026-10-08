# Creamos la clase Cliente
class Cliente:
    # Creamos el constructor y guardamos los datos del cliente
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono
    # Este metodo muestra los datos del cliente de forma ordenada
    def __str__(self):
        return f"Nombre: {self.nombre} | Cedula: {self.cedula} | Telefono: {self.telefono}"
# Creamos el primer cliente
cliente1 = Cliente("Carlos Benitez", "5123456", "0981123456")
# Creamos otro cliente con datos diferentes
cliente2 = Cliente("Maria Gonzalez", "4234567", "0972123456")
# Mostramos los datos de los clientes
print("CLIENTES")
print(cliente1)
print(cliente2)
