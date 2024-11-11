
class CantidadNegativaEx(Exception):
    def __init__(self, message= "No es posible poner numeros negativos "):
        self.message = message
        super().__init__(self.message)

class PrecioNegativaEx(Exception):
    def __init__(self, message= "El precio no puede tener numeros negativos "):
        self.message = message
        super().__init__(self.message)

class ProductoInvalidoEx(Exception):
    def __init__(self, message= "El nombre del producto no puede estar vacio "):
        self.message = message
        super().__init__(self.message)

