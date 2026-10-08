# Creamos la clase Estudiante
class Estudiante:
    # Guardamos el nombre y creamos un diccionario para las notas
    def __init__(self, nombre):
        self.nombre = nombre
        self.notas = {}
    # Agregamos una nota indicando la materia
    def registrar_nota(self, materia, nota):
        self.notas[materia] = nota
    # Calculamos el promedio de todas las materias
    def calcular_promedio(self):
        # Si no hay notas devolvemos cero
        if len(self.notas) == 0:
            return 0
        total = 0
        # Sumamos todas las notas
        for nota in self.notas.values():
            total += nota
        # Calculamos el promedio
        return total / len(self.notas)
    # Verificamos si el promedio es suficiente para aprobar
    def aprobado(self):
        return self.calcular_promedio() >= 60
    # Mostramos el nombre, promedio y condicion del estudiante
    def __str__(self):
        # Verificamos la condicion final
        if self.aprobado():
            condicion = "Aprobado"
        else:
            condicion = "No aprobado"
        return f"Estudiante: {self.nombre} | Promedio: {self.calcular_promedio():.2f} | Condicion: {condicion}"
# Creamos el estudiante
estudiante = Estudiante("Carlos Benitez")
# Registramos las notas de las materias
estudiante.registrar_nota("Programacion", 80)
estudiante.registrar_nota("Matematica", 65)
estudiante.registrar_nota("Sistemas Distribuidos", 75)
estudiante.registrar_nota("Base de Datos", 70)
# Mostramos el boletin
print("BOLETIN")
# Recorremos las materias para mostrar sus notas
for materia, nota in estudiante.notas.items():
    print(f"{materia}: {nota}")
# Mostramos el promedio y la condicion final
print(estudiante)