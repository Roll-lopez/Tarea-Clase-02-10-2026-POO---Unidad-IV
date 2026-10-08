# Creamos la clase para representar una linea telefonica
class LineaTelefonica:
    # Guardamos el numero, los gigabytes del plan y empezamos con cero consumido
    def __init__(self, numero, gigabytes):
        self.numero = numero
        self.gigabytes = gigabytes
        self.consumidos = 0
    # Este metodo sirve para registrar el consumo de internet
    def registrar_consumo(self, cantidad):
        # Verificamos que la cantidad sea positiva
        if cantidad > 0:
            # Verificamos que no supere los gigabytes del plan
            if self.consumidos + cantidad <= self.gigabytes:
                self.consumidos += cantidad
                print(f"Consumo registrado: {cantidad} GB.")
            # Si supera el plan mostramos un aviso
            else:
                print("AVISO: el consumo supera los gigabytes disponibles.")
        # Si la cantidad no es positiva mostramos un aviso
        else:
            print("La cantidad debe ser positiva.")
    # Calculamos cuantos gigabytes quedan disponibles
    def gigabytes_disponibles(self):
        return self.gigabytes - self.consumidos

    # Mostramos los datos de la linea y el consumo actual
    def __str__(self):
        return f"Numero: {self.numero} | Plan: {self.gigabytes} GB | Consumidos: {self.consumidos} GB | Disponibles: {self.gigabytes_disponibles()} GB"
# Creamos una linea con un plan de 10 GB
linea = LineaTelefonica("0981123456", 10)
# Mostramos el estado inicial
print(linea)
# Registramos un consumo
linea.registrar_consumo(3)
print(linea)
# Registramos otro consumo
linea.registrar_consumo(4)
print(linea)
# Intentamos consumir mas de lo que queda disponible
linea.registrar_consumo(5)
print(linea)