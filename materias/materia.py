from typing import List
from random import randint
from datetime import datetime

class Materia:
    nombre: str
    descripcion:str
    id_semestre: int
    creditos: int

    def __init__(self, nombre: str, descripcion:str, id_semestre: int, creditos: int):
        self.nombre = nombre
        self.descripcion = descripcion
        self.id_semestre = id_semestre
        self.creditos = creditos
        self.numero_control = self.generar_numero_control()

    def generar_numero_control(self):
        Ultimas_2_letras_nombre = self.nombre[-2:].upper()
        aleatorio = randint(1,1000)
        return f"MT{Ultimas_2_letras_nombre}{self.id_semestre}{self.creditos}{aleatorio}"

    def mostrar_informacion(self):
        informacion = f"Id de la Materia: {self.numero_control} \nNombre de la materia: {self.nombre} \nDescripcion: {self.descripcion} \nSemetre: {self.id_semestre} \nCreditos: {self.creditos} \n------------------------------------------"
        return informacion
