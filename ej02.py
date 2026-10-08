# Creamos la clase Producto
class Producto:
    # Creamos el constructor para guardar los datos del producto
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    # Calculamos cuanto vale todo el stock del producto
    def valor_stock(self):
        return self.precio * self.stock
    # Mostramos los datos principales del producto
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio:,.0f} Gs. | Stock: {self.stock}"
# Creamos algunos productos para probar la clase
producto1 = Producto("Arroz", 8000, 10)
producto2 = Producto("Aceite", 12000, 8)
producto3 = Producto("Azucar", 7000, 15)
# Mostramos el primer producto y su valor en stock
print(producto1)
print(f"Valor en stock: {producto1.valor_stock():,.0f} Gs.\n")
# Mostramos el segundo producto y su valor en stock
print(producto2)
print(f"Valor en stock: {producto2.valor_stock():,.0f} Gs.\n")
# Mostramos el tercer producto y su valor en stock
print(producto3)
print(f"Valor en stock: {producto3.valor_stock():,.0f} Gs.")