from typing import List
from estudiantes.estudiante import Estudiante
from grupos.grupo import Grupo
from maestros.maestro import Maestro
from materias.materia import Materia
from carrera.carrera import Carrera
from semestre.semestre import Semestre
from datetime import datetime
from random import randint

class Escuela:
    lista_estudiantes: List[Estudiante] = []
    lista_maestros: List[Maestro] = []
    lista_grupos: List[Grupo] = []
    lista_materias: List[Materia] = []
    lista_carreras: List[Carrera] = []
    lista_semestres: List[Semestre] = []

    ###ESTUDIANTE###
    def registrar_estudiante(self, estudiante: Estudiante):
        self.lista_estudiantes.append(estudiante)
        print("\nSe registro con exito al estudiante con numero de control: ", estudiante.numero_control)

    def generar_numero_control(self):
        ano = datetime.now().year
        mes = datetime.now().month
        longitud_mas_uno = len(self.lista_estudiantes)+1
        aleatorio = randint(0,10000)
        numero_control = f"l{ano}{mes}{longitud_mas_uno}{aleatorio}"
        return numero_control
    
    def listar_estudiantes(self):
        print("*************Estudiantes*************")
        for estudiante in self.lista_estudiantes:
            print(estudiante.mostrar_informacion())

    def eliminar_estudiante(self, numero_control: str):
        for estudiante in self.lista_estudiantes:
            if estudiante.numero_control == numero_control.strip():
                self.lista_estudiantes.remove(estudiante)
                print(f"El Estudiante {estudiante.nombre} {estudiante.apellido}, ha sido eliminado exitosamente.\n")
                return 
        print(f"No se encontro al estudiante con numero de control: {numero_control} \n")

    ###MAESTRO###
    def registrar_maestro(self, maestro: Maestro):
        self.lista_maestros.append(maestro)

    def generar_numero_control_maestros(self, maestro: Maestro):
        ano = maestro.fecha_nacimiento.year
        dia = datetime.now().day
        aleatorio = randint(500,5000)
        primeras_2_letras_nombre = maestro.nombre[:2].upper()
        ultimas_2_letras_rfc = maestro.rfc[-2:].upper()
        longitud_mas_uno = len(self.lista_maestros)+1
        numero_control_maestro = f"M{ano}{dia}{aleatorio}{primeras_2_letras_nombre}{ultimas_2_letras_rfc}{longitud_mas_uno}"
        return numero_control_maestro
    
    def listar_maestros(self):
        print("*************Maestros*************")
        for maestro in self.lista_maestros:
            print(maestro.mostrar_informacion())

    def eliminar_maestro(self, numero_control: str):
        for maestro in self.lista_maestros:
            if maestro.numero_control_maestro == numero_control.strip():
                self.lista_maestros.remove(maestro)
                print(f"El Maestro {maestro.nombre} {maestro.apellido}, ha sido eliminado exitosamente.\n")
                return 
        print(f"No se encontro el maestro con numero de control: {numero_control} \n")

    ###MATERIA###
    def registrar_materia(self, materia: Materia):
        self.lista_materias.append(materia)
    
    def listar_materias(self):
        print("*************Materias*************")
        for materia in self.lista_materias:
            print(materia.mostrar_informacion())

    def eliminar_materia(self, id_de_la_materia: str):
        for materia in self.lista_materias:
            if materia.id == id_de_la_materia.strip():
                self.lista_materias.remove(materia)
                print(f"La Materia {materia.nombre}, ha sido eliminada exitosamente.\n")
                return 
        print(f"No se encontro la materia con ID: {id_de_la_materia} \n")

    ###Carrera###
    def registrar_carrera(self, carrera: Carrera):
        self.lista_carreras.append(carrera)
    
    def listar_carreras(self):
        print("*************Carreras*************")
        for carrera in self.lista_carreras:
            print(carrera.mostrar_informacion())

    ###Semestre###
    def registrar_semestre(self, semestre: Semestre):
        id_carrera = semestre.id_carrera
        for carrera in self.lista_carreras:
            if carrera.matricula == id_carrera:
                carrera.registrar_semestre(semestre=semestre)
                break
        self.lista_semestres.append(semestre)

    def listar_semestres(self):
        print("*************Semestres*************")
        for semestre in self.lista_semestres:
            print(semestre.mostrar_informacion())
    
    ###Grupo###
    def registrar_grupo(self, grupo: Grupo):
        id_semestre = grupo.id_semestre
        for semestre in self.lista_semestres:
            if id_semestre == semestre.id:
                semestre.registrar_grupo_en_semestre(grupo=grupo)
                break
        self.lista_grupos.append(grupo)

    def listar_grupos(self):
        print("*************Grupos*************")
        for grupo in self.lista_grupos:
            print(grupo.mostrar_informacion())