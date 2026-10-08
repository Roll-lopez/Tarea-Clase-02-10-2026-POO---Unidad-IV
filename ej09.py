# Creamos la clase Turno
class Turno:
    # Guardamos los datos del turno y lo dejamos pendiente
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "pendiente"
    # Cambiamos el estado del turno cuando el paciente es atendido
    def marcar_atendido(self):
        self.estado = "atendido"
    # Mostramos los datos del turno
    def __str__(self):
        return f"Paciente: {self.paciente} | Hora: {self.hora} | Estado: {self.estado}"
# Creamos la clase Agenda
class Agenda:
    # Creamos una lista vacia para guardar los turnos
    def __init__(self):
        self.turnos = []
    # Agregamos un turno a la agenda
    def agregar_turno(self, turno):
        self.turnos.append(turno)
    # Mostramos solamente los turnos que siguen pendientes
    def listar_pendientes(self):
        print("TURNOS PENDIENTES")
        # Recorremos todos los turnos
        for turno in self.turnos:
            # Verificamos cuales siguen pendientes
            if turno.estado == "pendiente":
                print(turno)
    # Mostramos la cantidad de turnos de la agenda
    def __str__(self):
        return f"Agenda con {len(self.turnos)} turnos"
# Creamos varios turnos
turno1 = Turno("Pedro Gonzalez", "08:00")
turno2 = Turno("Maria Lopez", "09:00")
turno3 = Turno("Carlos Benitez", "10:00")
turno4 = Turno("Ana Martinez", "11:00")
# Creamos la agenda
agenda = Agenda()
# Agregamos todos los turnos
agenda.agregar_turno(turno1)
agenda.agregar_turno(turno2)
agenda.agregar_turno(turno3)
agenda.agregar_turno(turno4)
# Marcamos algunos turnos como atendidos
turno1.marcar_atendido()
turno3.marcar_atendido()
# Mostramos la agenda
print(agenda)
# Mostramos los turnos que siguen pendientes
agenda.listar_pendientes()
