import csv
from Clase_Mat_Aprobadas import MateriasAprobadas
from Clase_Alumnos import Alumno


class ManejadorMaterias:
    def __init__(self):
        self.materias_aprobadas = []

    def cargar_archivo(self):
        """
        Carga el archivo de materias.
        """
        with open("materiasAprobadas.csv", "r") as archivo:
            csv_reader = csv.reader(archivo, delimiter=';')
            next(csv_reader)
            for datos in csv_reader:
                self.materias_aprobadas.append(
                MateriasAprobadas(datos[0], datos[1], datos[2], datos[3], datos[4])
                )

    def listar_materias_aprobadas(self):
        """
        Muestra la lista de materias aprobadas.
        """
        for materia_aprobada in self.materias_aprobadas:
            print(materia_aprobada)

    def obtener_alumnos_por_materia(self, nombre_materia):
        alumnos = []
        alumno=Alumno()
        for materia_aprobada in self.materias_aprobadas:
            if materia_aprobada.get_nombreMateria() == nombre_materia:
                dni = materia_aprobada.get_dni()
                for alumno in self.alumnos:
                    if alumno.get_dni() == dni:
                        alumnos.append(alumno)
        return alumnos
    def obtener_promocionados_por_materia(self, nombre_materia):
        promocionados = []
        for alumno in self.alumnos:
            for materia_aprobada in alumno.materias_aprobadas:
                if nombre_materia == materia_aprobada.nombre_materia:
                    if materia_aprobada in alumno.materias_aprobadas:
                        if alumno.promocionado():
                            promocionados.append(alumno)
        return promocionados