from controller_sistema_educativo import ControladorJson
from models import Curso

class CursoController:
    def __init__(self):
        self.gestor = ControladorJson("data")
        self.archivo = "cursos.json"

    def listar(self):
        return self.gestor.cargar_datos(self.archivo, Curso)

    def guardar(self, lista_cursos):
        self.gestor.guardar_datos(self.archivo, lista_cursos)

    def crear(self, paralelo, cantidad_estudiantes, docente_asignado):
        cursos = self.listar()
        
        # 1. Validación de negocio opcional: por ejemplo, que no se repita el mismo paralelo
        for cur in cursos:
            if cur.paralelo.upper() == paralelo.upper():
                return False, f"Error de negocio: El paralelo '{paralelo}' ya está registrado."

        # 2. Siguiente ID automático
        nuevo_id = 1 if not cursos else max(c.id for c in cursos) + 1

        try:
            # 3. Instanciamos la clase Curso
            nuevo = Curso(nuevo_id, paralelo, cantidad_estudiantes, docente_asignado)
            cursos.append(nuevo)
            self.guardar(cursos)
            return True, f"Curso creado con éxito: {nuevo.etiqueta()}"
        except ValueError as e:
            return False, f"Error de validación del modelo: {e}"