from usuario.usuario import Usuario
from datetime import datetime
from usuario.utils.roles import Rol

class Coordinador(Usuario):
    sueldo: str
    rfc: str
    anios_antiguedad: int

    def __init__(self, numero_control: str, nombre: str, apellido: str, rfc: str, sueldo: float, anios_antiguedad: datetime, contrasenia: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.COORDINADOR.value)
        self.sueldo = sueldo
        self.rfc = rfc
        self.anios_antiguedad = anios_antiguedad
        

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"\nNumero de control: {self.numero_control} \nNombre completo: {nombre_completo} \nRFC: {self.rfc} \nSueldo: {self.sueldo} \nAños de antiguedad: {self.anios_antiguedad} \n------------------------------------------"
        return informacion