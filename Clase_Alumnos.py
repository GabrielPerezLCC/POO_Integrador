
class Alumno:
    __dni: int
    __apellido: str
    __nombre: str
    __carrera: str
    __anioCursado: int
    
    def __init__(self, dni=0,apellido=None,nombre=None,carrera=None,anioCursado=1900):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anioCursado = anioCursado

    def get_dni(self):
        return self.__dni
    def set_dni(self,dni):
        self.__dni = dni
    def get_apellido(self):
        return self.__apellido
    def set_apellido(self,apellido):
        self.__apellido = apellido
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self,nombre):
        self.__nombre = nombre
    def get_carrera(self):
        return self.__carrera
    def set_carrera(self,carrera):
        self.__carrera = carrera
    def get_anioCursado(self):
        return self.__anioCursado
    def set_anioCursado(self,anioCursado):
        self.__anioCursado = anioCursado
    #def __str__(self):
        #return f"{self.get_dni()} {self.get_apellido()} {self.get_nombre()} {self.get_carrera()} {self.get_anioCursado()}"
    def __str__(self):
        return f"{self.__dni} {self.__apellido} {self.__nombre} {self.__carrera} {self.__anioCursado}"
    def __lt__(self, otro):
        primero=str(self.__anioCursado)+str(self.__apellido)+str(self.__nombre)
        segundo=str(otro.__anioCursado)+str(otro.__apellido)+str(otro.__nombre)
        return primero<segundo