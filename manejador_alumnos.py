import numpy as np
from Clase_Alumnos import Alumno
import csv
from typing import List


class ManejadorAlumnos:
    def __init__(self):
        self.alumnos = np.empty((0,), dtype=Alumno)

    def cargarAlumno(self):
        with open("alumnos.csv", "r") as f:
            next(f)
            for linea in f:
                datos = linea.strip().split(";")
                dni = int(datos[0])
                # print(dni)
                apellido = datos[1]
                # print(apellido)
                nombre = datos[2]
                # print(nombre)
                carrera = datos[3]
                # print(carrera)
                anio_carrera = datos[4]
                # print(anioCarrera)
                alumno = Alumno(dni, apellido, nombre, carrera, anio_carrera)
                # print(alumno)
                self.alumnos = np.append(self.alumnos, alumno)
            # print(self.alumnos)

    def buscar_alumno(self, dni: int):
        buscado = None
        # print("longitud",len(self.alumnos))
        # print("entrando al for de buscar alumno")
        for alumno in self.alumnos:
            # print("ENTRE al for de buscar alumno")

            if alumno.get_dni() == dni:
                buscado = alumno

        return buscado

    def promedio_con_aplazos(self, dni):
        alumno = self.buscar_alumno(dni)
        if not alumno:
            raise ValueError("Alumno no Encontrado")

        else:
            notas = []
            with open("materiasAprobadas.csv", "r") as ma:
                next(ma)
                for linea in ma:
                    datos = linea.strip().split(";")
                    if int(datos[0]) == dni:
                        nota = float(datos[3])
                        # print("nota encontrada",nota)
                        notas.append(nota)
            promedio = sum(notas) / len(notas)
        return promedio

    def promedio_sin_aplazos(self, dni):
        alumno = self.buscar_alumno(dni)
        if not alumno:
            raise ValueError("Alumno no Encontrado")

        else:
            notas = []
            with open("materiasAprobadas.csv", "r") as ma:
                next(ma)
                for linea in ma:
                    datos = linea.strip().split(";")
                    # print("DNI Notas  ",datos[0], datos[3])
                    if int(datos[0]) == dni and float(datos[3]) >= 4:
                        nota = float(datos[3])
                        notas.append(nota)
            if sum(notas) == 0:
                promedio = "EL ALUMNO NO TIENE APLAZOS"
            else:
                promedio = sum(notas) / len(notas)
        return promedio

    def __str__(self):
        resultado = "Lista de alumnos:\n"
        for alumno in self.alumnos:
            resultado += f"{alumno}\n"
        return resultado

    def get_materias_aprobadas(self, dni):
        materias_aprobadas = []
        for alumno in self.alumnos:
            if alumno.get_dni() == dni:
                for materia in alumno.get_materias_aprobadas():
                    materias_aprobadas.append(materia)
        return materias_aprobadas
    
    def obtener_promocionados_por_materia(self, nombre_materia):
        promocionados = []
        for alumno in self.alumnos:
            for materia_aprobada in alumno.get_materias_aprobadas():
                if (
                    materia_aprobada.get_nombreMateria() == nombre_materia
                    and materia_aprobada.get_aprobacion() == "P"
                    and materia_aprobada.get_nota() >= 7
                ):
                    promocionados.append(alumno.get_dni())
        return promocionados