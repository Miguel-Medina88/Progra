from excepciones.excepciones import PrecioNegativaEx, ProductoInvalidoEx, CantidadNegativaEx

class Producto:
    def __init__(self, nombre: str, precio: float, cantidad: int):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

        if not nombre:
            raise ProductoInvalidoEx()
        if precio <= 0:
            raise PrecioNegativaEx()
        if cantidad <= 0:
            raise CantidadNegativaEx()

    def calcular_precio_total(self):
        return self.precio * self.cantidad

    def mostrar_detalles_compra(self):
        precio_total = self.calcular_precio_total()
        # Ahora calculamos correctamente el precio total al invocar el método
        return (f"Nombre Artículo: {self.nombre},\n"
                f"Productos en existencia: {self.cantidad}\n"
                f"Precio: ${self.precio}\n"
                f"Precio total: ${precio_total}\n")

