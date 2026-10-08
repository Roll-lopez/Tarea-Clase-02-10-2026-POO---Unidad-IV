# Creamos la clase Producto
class Producto:
    # Guardamos los datos del producto y su stock minimo
    def __init__(self, nombre, precio, stock, stock_minimo):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.stock_minimo = stock_minimo
    # Este metodo sirve para agregar mercaderia
    def ingresar_mercaderia(self, cantidad):
        # Verificamos que la cantidad sea positiva
        if cantidad > 0:
            self.stock += cantidad
            print(f"Se agregaron {cantidad} unidades.")
        # Si no es positiva mostramos un aviso
        else:
            print("La cantidad debe ser positiva.")
    # Este metodo sirve para registrar una venta
    def vender(self, cantidad):
        # Verificamos que la cantidad sea correcta
        if cantidad <= 0:
            print("La cantidad debe ser positiva.")
        # Comprobamos que haya suficientes unidades
        elif cantidad <= self.stock:
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades.")
            # Avisamos si el stock queda por debajo del minimo
            if self.stock < self.stock_minimo:
                print("ALERTA: stock por debajo del minimo.")
        # Si no hay suficiente stock no hacemos la venta
        else:
            print("Venta rechazada: no hay suficientes unidades.")
    # Mostramos los datos del producto
    def __str__(self):
        return f"Producto: {self.nombre} | Precio: {self.precio:,.0f} Gs. | Stock: {self.stock}"
# Creamos un producto con su stock minimo
producto = Producto("Yerba", 12000, 10, 5)
# Mostramos el stock inicial
print(producto)
# Realizamos una venta
producto.vender(4)
print(producto)
# Hacemos otra venta para probar la alerta
producto.vender(3)
print(producto)
# Agregamos mercaderia nuevamente
producto.ingresar_mercaderia(10)
print(producto)
