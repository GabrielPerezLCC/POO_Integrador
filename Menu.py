class Menu:
    @staticmethod
    def mostrar_menu():

        while True:
            print("Seleccione una opción:")
            print("1. Ver promedio de un alumno")
            print("2. Ver estudiantes que aprobaron una materia en forma promocional con nota mayor o igual a 7")
            print("3. Obtener un listado de alumnos ordenado por año y apellido")
            print("4. Salir")
            opcion = int(input("Ingrese una opción: "))
            if opcion in [1,2,3,4]:
                return opcion
            else:
                print("Opción incorrecta")
        
