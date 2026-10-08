# Creamos la clase Cancion
class Cancion:
    # Guardamos los datos de cada cancion
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion
    # Mostramos la informacion de la cancion
    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion} minutos)"
# Creamos la clase para manejar la lista de reproduccion
class ListaReproduccion:
    # Creamos una lista vacia donde vamos a guardar las canciones
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []
    # Agregamos una cancion a la lista
    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
    # Calculamos la duracion total de todas las canciones
    def duracion_total(self):
        total = 0
        # Recorremos todas las canciones de la lista
        for cancion in self.canciones:
            total += cancion.duracion
        return total
    # Mostramos el nombre de la lista y la cantidad de canciones
    def __str__(self):
        return f"Lista: {self.nombre} | Canciones: {len(self.canciones)}"
# Creamos algunas canciones
cancion1 = Cancion("La Curiosidad", "Jay Wheeler", 3.5)
cancion2 = Cancion("512", "Mora", 3.2)
cancion3 = Cancion("Si Antes Te Hubiera Conocido", "Karol G", 3.1)
# Creamos la lista de reproduccion
lista = ListaReproduccion("Mis canciones")
# Agregamos las canciones a la lista
lista.agregar_cancion(cancion1)
lista.agregar_cancion(cancion2)
lista.agregar_cancion(cancion3)
# Mostramos los datos de la lista
print(lista)
# Mostramos todas las canciones
for cancion in lista.canciones:
    print(cancion)
# Mostramos la duracion total
print(f"Duracion total: {lista.duracion_total():.1f} minutos")
