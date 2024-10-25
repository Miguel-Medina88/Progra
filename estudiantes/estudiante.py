from usuario.usuario import Usuario
from datetime import datetime
from usuario.utils.roles import Rol

class Estudiante(Usuario):
    curp: str
    fecha_nacimiento: datetime

    def __init__(self, numero_control: str, nombre: str, apellido: str, curp: str, fecha_nacimiento: datetime, contrasenia: str):
        super().__init__(numero_control=numero_control, nombre=nombre, apellido=apellido, contrasenia=contrasenia, rol=Rol.ESTUDIANTE.value)
        self.curp = curp
        self.fecha_nacimiento = fecha_nacimiento

    def mostrar_informacion(self):
        nombre_completo = f"{self.nombre} {self.apellido}"
        informacion = f"Numero de control: {self.numero_control} \nNombre completo: {nombre_completo} \nCurp: {self.curp} \nFecha de nacimiento: {self.fecha_nacimiento} \n------------------------------------------"
        return informacion