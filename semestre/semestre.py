from typing import List
from materias.materia import Materia
from grupos.grupo import Grupo
from random import randint

class Semestre:
    id: str
    numero: int
    id_carrera: str
    materias: List[Materia] = []
    grupos: List[Grupo] = []

    def __init__(self, numero: int, id_carrera: str):
        self.id = self.generar_id(numero)
        self.id_carrera = id_carrera
        self.numero = numero

    def generar_id(self, numero_semestre: int) -> str:
        return f"{numero_semestre}-{randint(0,1000000)}-{randint(0,1000000)}"
    
    def registrar_grupo_en_semestre(self, grupo: Grupo):
        self.grupos.append(grupo)

    def mostrar_informacion(self):
        informacion = f"ID: {self.id} \nNumero: {self.numero} \nID de Carrera: {self.id_carrera} \n------------------------------------------"
        return informacion
