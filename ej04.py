# Creamos la clase Libro
class Libro:
    # Guardamos los datos del libro
    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible
    # Mostramos la informacion del libro y su estado
    def __str__(self):
        # Si disponible es True mostramos que esta disponible
        if self.disponible:
            estado = "Disponible"
        # Si es False mostramos que esta prestado
        else:
            estado = "Prestado"
        return f"Titulo: {self.titulo} | Autor: {self.autor} | Estado: {estado}"
# Creamos un libro que esta disponible
libro1 = Libro("El principito", "Antoine de Saint-Exupery", True)
# Creamos otro libro que esta prestado
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", False)
# Mostramos los dos libros
print(libro1)
print(libro2)
