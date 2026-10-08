# Creamos la clase Empleado
class Empleado:
    # Guardamos los datos del empleado al crear el objeto
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
    # Calculamos el salario anual incluyendo un mes de aguinaldo
    def salario_anual(self):
        return self.salario * 13
    # Mostramos los datos del empleado
    def __str__(self):
        return f"Empleado: {self.nombre} | Cargo: {self.cargo} | Salario mensual: {self.salario:,.0f} Gs."
# Creamos dos empleados diferentes
empleado1 = Empleado("Juan Perez", "Soporte Tecnico", 4500000)
empleado2 = Empleado("Ana Lopez", "Administradora", 5000000)
# Mostramos los datos del primer empleado
print(empleado1)
# Mostramos cuanto gana en un año
print(f"Salario anual con aguinaldo: {empleado1.salario_anual():,.0f} Gs.\n")
# Mostramos los datos del segundo empleado
print(empleado2)
# Mostramos el salario anual del segundo empleado
print(f"Salario anual con aguinaldo: {empleado2.salario_anual():,.0f} Gs.")
