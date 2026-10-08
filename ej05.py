# Creamos la clase Vehiculo
class Vehiculo:
    # Guardamos los datos del vehiculo
    def __init__(self, marca, modelo, año, precio):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    # Creamos una descripcion para mostrar el vehiculo a la venta
    def descripcion(self):
        return f"{self.marca} {self.modelo} {self.año} — {self.precio:,.0f} Gs."

    # Mostramos los datos del vehiculo
    def __str__(self):
        return f"{self.marca} {self.modelo} | Año: {self.año} | Precio: {self.precio:,.0f} Gs."


# Creamos dos vehiculos diferentes
vehiculo1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
vehiculo2 = Vehiculo("Kia", "Rio", 2022, 85000000)

# Mostramos los vehiculos disponibles
print("VEHICULOS EN VENTA")
print(vehiculo1.descripcion())
print(vehiculo2.descripcion())
