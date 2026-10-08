# Creamos la clase Habitacion
class Habitacion:
    # Guardamos los datos de la habitacion y comenzamos como libre
    def __init__(self, numero, tipo, tarifa):
        self.numero = numero
        self.tipo = tipo
        self.tarifa = tarifa
        self.ocupada = False
    # Este metodo sirve para ocupar la habitacion
    def ocupar(self):
        # Verificamos que la habitacion este libre
        if not self.ocupada:
            self.ocupada = True
            print(f"La habitacion {self.numero} fue ocupada.")
        # Si ya esta ocupada mostramos un aviso
        else:
            print("La habitacion ya esta ocupada.")
    # Este metodo sirve para liberar la habitacion
    def liberar(self):
        # Verificamos que la habitacion este ocupada
        if self.ocupada:
            self.ocupada = False
            print(f"La habitacion {self.numero} fue liberada.")
        # Si ya esta libre mostramos un aviso
        else:
            print("La habitacion ya esta libre.")
    # Calculamos el precio total de la estadia
    def calcular_estadia(self, noches):
        return self.tarifa * noches
    # Mostramos los datos y el estado de la habitacion
    def __str__(self):
        # Determinamos si esta ocupada o libre
        if self.ocupada:
            estado = "Ocupada"
        else:
            estado = "Libre"
        return f"Habitacion: {self.numero} | Tipo: {self.tipo} | Tarifa: {self.tarifa:,.0f} Gs. | Estado: {estado}"
# Creamos una habitacion
habitacion = Habitacion(205, "Doble", 350000)
# Mostramos la habitacion antes de ocuparla
print(habitacion)
# Ocupamos la habitacion
habitacion.ocupar()
print(habitacion)
# Indicamos la cantidad de noches
noches = 3
# Calculamos el costo de la estadia
costo = habitacion.calcular_estadia(noches)
# Mostramos el costo total
print(f"Costo de la estadia por {noches} noches: {costo:,.0f} Gs.")
# Probamos ocuparla otra vez para comprobar la validacion
habitacion.ocupar()
# Liberamos la habitacion
habitacion.liberar()
# Mostramos el estado final
print(habitacion)