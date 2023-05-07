from datetime import date
    
class MateriasAprobadas:
    __dni: int
    __nombreMateria:str
    __fecha:date
    __nota:float
    __aprobacion:str

    def __init__(self,dni=0,nombremateria=None,fecha='1900/01/01',nota=0,aprobacion=None):
        self.__dni=dni
        self.__nombreMateria=nombremateria
        self.__fecha=fecha
        self.__nota=nota
        self.__aprobacion=aprobacion

    def get_dni(self):
        return self.__dni
    def set_dni(self,dni):
        self.__dni=dni
    def get_nombreMateria(self):
        return self.__nombreMateria
    def set_nombreMateria(self,nombremateria):
        self.__nombreMateria=nombremateria
    def get_fecha(self):
        return self.__fecha

    def set_fecha(self,fecha):
        self.__fecha=fecha

    def get_nota(self):
        return self.__nota

    def set_nota(self, nota):
        self.__nota = nota

    def get_aprobacion(self):
        return self.__aprobacion

    def set_aprobacion(self, aprobacion):
        self.__aprobacion = aprobacion

    def __str__(self):
        return f"DNI: {self.__dni} \n Nombre Materia: {self.__nombreMateria} \n Fecha: {self.__fecha} \n Nota: {self.__nota} \n Aprobacion: {self.__aprobacion}"
