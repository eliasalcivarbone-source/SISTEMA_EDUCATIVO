from controladores.estudiante_controller import EstudianteController
from controladores.docente_controller import  DocenteController
from controladores.materia_controller import MateriaController
from controladores.matricula_controller import MatriculaController
from controladores.controller_curso import CursoController
def mostrar_menu():
    print("\n" + "="*40)
    print("   SISTEMA DE GESTIÓN EDUCATIVA")
    print("="*40)
    print("1. Gestionar Estudiantes")
    print("2. Gestionar Docentes")
    print("3. Gestionar Materias")
    print("4. Gestionar Matrículas y Notas")
    print("5. Salir")
    print("="*40)

def menu_estudiantes():
    ctrl = EstudianteController()
    while True:
        print("\n--- MENÚ ESTUDIANTES ---")
        print("1. Listar estudiantes")
        print("2. Registrar nuevo estudiante")
        print("3. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            estudiantes = ctrl.listar()
            if not estudiantes:
                print("\nNo hay estudiantes registrados.")
            else:
                print("\n--- LISTA DE ESTUDIANTES ---")
                for e in estudiantes:
                    print(f"ID: {e.id} | {e.etiqueta()} | Carnet: {e.carnet} | Correo: {e.correo}")
        
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            carnet = input("Carnet (ej. EST-2026-001): ")
            materia = input("Materia principal: ")
            
            exito, mensaje = ctrl.crear(nombre, apellido, correo, telefono, carnet, materia)
            print(f"\n{mensaje}")
            
        elif opcion == "3":
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")

def menu_docentes():
    ctrl = DocenteController()
    while True:
        print("\n--- MENÚ DOCENTES ---")
        print("1. Listar docentes")
        print("2. Registrar nuevo docente")
        print("3. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            docentes = ctrl.listar()
            if not docentes:
                print("\nNo hay docentes registrados.")
            else:
                print("\n--- LISTA DE DOCENTES ---")
                for d in docentes:
                    print(f"ID: {d.id} | {d.etiqueta()} | Correo: {d.correo} | Especialidad: {d.especialidad}")
        
        elif opcion == "2":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            telefono = input("Teléfono: ")
            especialidad = input("Especialidad: ")
            titulo = input("Título: ")
            
            exito, mensaje = ctrl.crear(nombre, apellido, correo, telefono, especialidad, titulo)
            print(f"\n{mensaje}")
            
        elif opcion == "3":
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")

def menu_materias():
    ctrl = MateriaController()
    while True:
        print("\n--- MENÚ MATERIAS ---")
        print("1. Listar materias registradas")
        print("2. Agregar materia oficial")
        print("3. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            materias = ctrl.listar()
            if not materias:
                print("\nNo hay materias guardadas.")
            else:
                print("\n--- MATERIAS REGISTRADAS ---")
                for m in materias:
                    print(f"ID: {m.id} | Código: {m.codigo}")
        
        elif opcion == "2":
            codigo = input("Código de la materia (ej. MAT-101): ")
            exito, mensaje = ctrl.crear(codigo)
            print(f"\n{mensaje}")
            
        elif opcion == "3":
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")

def menu_matriculas():
    ctrl = MatriculaController()
    while True:
        print("\n--- MENÚ MATRÍCULAS Y NOTAS ---")
        print("1. Listar matrículas")
        print("2. Registrar nueva matrícula")
        print("3. Agregar calificación a matrícula")
        print("4. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            matriculas = ctrl.listar()
            if not matriculas:
                print("\nNo hay matrículas registradas.")
            else:
                print("\n--- LISTA DE MATRÍCULAS ---")
                for mat in matriculas:
                    print(f"ID Matrícula: {mat.id} | Estudiante ID: {mat.estudiante_id} | Periodo: {mat.periodo} | Materias: {mat.codigos_materias} | Calificaciones: {mat.calificaciones} | Promedio: {mat.promedio}")
        
        elif opcion == "2":
            try:
                estudiante_id = int(input("ID del estudiante a matricular: "))
            except ValueError:
                print("\nEl ID debe ser un número entero.")
                continue
                
            codigos_input = input("Códigos de materias separados por coma (ej. MAT-101,FIS-102): ")
            codigos_materias = [c.strip() for c in codigos_input.split(",")]
            periodo = input("Periodo académico (ej. 2026-1): ")
            
            exito, mensaje = ctrl.crear(estudiante_id, codigos_materias, periodo)
            print(f"\n{mensaje}")
            
        elif opcion == "3":
            try:
                matricula_id = int(input("ID de la matrícula: "))
                nota = float(input("Calificación a agregar: "))
            except ValueError:
                print("\nPor favor ingresa valores numéricos válidos.")
                continue
                
            exito, mensaje = ctrl.agregar_nota_a_matricula(matricula_id, nota)
            print(f"\n{mensaje}")
            
        elif opcion == "4":
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")
            
  

def menu_cursos():
    ctrl = CursoController()
    while True:
        print("\n--- MENÚ CURSOS ---")
        print("1. Listar cursos")
        print("2. Registrar nuevo curso")
        print("3. Volver al menú principal")
        
        opcion = input("Elige una opción: ")
        
        if opcion == "1":
            cursos = ctrl.listar()
            if not cursos:
                print("\nNo hay cursos registrados.")
            else:
                print("\n--- LISTA DE CURSOS ---")
                for c in cursos:
                    print(f"ID: {c.id} | Paralelo: {c.paralelo} | Estudiantes: {c.cantidad_estudiantes} | Docente: {c.docente_asignado}")
        
        elif opcion == "2":
            paralelo = input("Paralelo (ej. 5 "A", 3 "B"): ")
            try:
                cantidad_estudiantes = int(input("Cantidad de estudiantes: "))
            except ValueError:
                print("\nLa cantidad debe ser un número entero.")
                continue
            docente_asignado = input("Nombre o cédula del docente asignado: ")
            
            exito, mensaje = ctrl.crear(paralelo, cantidad_estudiantes, docente_asignado)
            print(f"\n{mensaje}")
            
        elif opcion == "3":
            break
        else:
            print("\nOpción inválida. Intenta de nuevo.")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")
        
        if opcion == "1":
            menu_estudiantes()
        elif opcion == "2":
            menu_docentes()
        elif opcion == "3":
            menu_materias()
        elif opcion == "4":
            menu_matriculas()
        elif opcion == "5":
             menu_cursos()
        elif opcion==6:
            break
        else:
             print("\nOpción no válida. Por favor elige entre 1 y 5.")
            

if __name__ == "__main__":
    main()