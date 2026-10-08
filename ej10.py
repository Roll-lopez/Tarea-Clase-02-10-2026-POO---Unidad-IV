# Creamos la clase Producto
class Producto:
    # Guardamos el nombre y el precio del producto
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    # Mostramos los datos del producto
    def __str__(self):
        return f"{self.nombre} - {self.precio:,.0f} Gs."
# Creamos la clase Item para saber que producto y cantidad se agregan
class Item:
    # Guardamos el producto y la cantidad
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
    # Calculamos el subtotal del item
    def subtotal(self):
        return self.producto.precio * self.cantidad
    # Mostramos el producto, cantidad y subtotal
    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = {self.subtotal():,.0f} Gs."
# Creamos la clase Carrito
class Carrito:
    # Creamos una lista vacia para guardar los items
    def __init__(self):
        self.items = []
    # Agregamos un item al carrito
    def agregar_item(self, item):
        self.items.append(item)
    # Calculamos el total de todos los productos
    def total(self):
        total = 0
        # Recorremos todos los items
        for item in self.items:
            total += item.subtotal()
        return total
    # Mostramos el detalle completo de la compra
    def mostrar_detalle(self):
        print("DETALLE DE LA COMPRA")
        # Mostramos cada item
        for item in self.items:
            print(item)
        # Mostramos el total general
        print(f"Total general: {self.total():,.0f} Gs.")
    # Mostramos la cantidad de items del carrito
    def __str__(self):
        return f"Carrito con {len(self.items)} items"
# Creamos los productos
producto1 = Producto("Teclado", 120000)
producto2 = Producto("Mouse", 80000)
producto3 = Producto("Auriculares", 150000)
# Creamos los items con sus respectivas cantidades
item1 = Item(producto1, 1)
item2 = Item(producto2, 2)
item3 = Item(producto3, 1)
# Creamos el carrito
carrito = Carrito()
# Agregamos los items al carrito
carrito.agregar_item(item1)
carrito.agregar_item(item2)
carrito.agregar_item(item3)
# Mostramos el carrito
print(carrito)
# Mostramos el detalle de la compra
carrito.mostrar_detalle()