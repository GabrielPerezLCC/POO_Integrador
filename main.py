from Clase_Alumnos import Alumno
from Clase_Mat_Aprobadas import MateriasAprobadas
from manejador_alumnos import ManejadorAlumnos
from Menu import Menu
from manejador_materias import ManejadorMaterias



if __name__=='__main__':
    
    manejador = ManejadorAlumnos()
    manejador.cargarAlumno()
    materias=ManejadorMaterias()
    materias.cargar_archivo()

    #print("VOLVI AL MAIN",manejador)
    opcion=int(Menu.mostrar_menu())
    if opcion==1:
        
        dni=int(input("Ingrese DNI del Alumno  "))
        alumno = manejador.buscar_alumno(int(dni))
        #print("buscado en MAIN",alumno)
        if alumno:
            print(f"Promedio sin aplazos del alumno {alumno.get_nombre()} {alumno.get_apellido()}: {manejador.promedio_sin_aplazos(dni)}")
            print(f"Promedio con aplazos del alumno {alumno.get_nombre()} {alumno.get_apellido()}: {manejador.promedio_con_aplazos(dni)}")
        
        else:
            print("Alumno no encontrado")
                   

    elif opcion==2:
        nombre_materia = input("Ingrese el nombre de la materia: ")
        promocionados = manejador.obtener_promocionados_por_materia(nombre_materia)
        print(f"Los promocionados en {nombre_materia} son: {promocionados}")
    elif opcion==3:
        alumnos_ordenados = sorted(manejador.alumnos)
        for alumno in alumnos_ordenados:
            print(alumno)
'''
opcion = input("Ingrese la opción deseada: ")
    if opcion == "1":
        dni = input("Ingrese el DNI del alumno: ")
        alumno = alumnos[alumnos[:,0] == dni][0]
        print(f"Promedio sin aplazos del alumno {alumno.nombre} {alumno.apellido}: {alumno.promedio_sin_aplazos()}")
        print(f"Promedio con aplazos del alumno {alumno.nombre} {alumno.apellido}: {alumno.promedio_con_aplazos()}")
    
    elif opcion == "2":
        materia = input("Ingrese el nombre de la materia: ")
        estudiantes = [m.aprobacion for m in materias if m.nombre_materia == materia and m.aprobacion == "P" and float(m.nota) >= 7]
        print(f"Estudiantes que aprobaron {materia} en forma promocional con nota mayor o igual a 7:")
        for e in estudiantes:
            print(e)

    elif opcion == "3":
        alumnos_ordenados = sorted(alumnos, key=lambda a: (a.anio, a.apellido, a.nombre))
        print("Listado de alumnos ordenado por año y apellido:")
        for a in alumnos_ordenados:
            print(f"{a.dni} - {a.apellido} {a.nombre} - {a.carrera} - Año {a.anio}")

    elif opcion == "4":
        break

    else:
        print("Opción inválida. Intente nuevamente.")
    
    
    '''
