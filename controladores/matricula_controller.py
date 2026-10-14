from controller_sistema_educativo import ControladorJson
from models import Matricula
from controladores.estudiante_controller import EstudianteController

class MatriculaController:
    def __init__(self):
        self.gestor = ControladorJson("data")
        self.archivo = "matriculas.json"
        self.estudiante_ctrl = EstudianteController()

    def listar(self):
        return self.gestor.cargar_datos(self.archivo, Matricula)

    def guardar(self, lista_matriculas):
        self.gestor.guardar_datos(self.archivo, lista_matriculas)

    def crear(self, estudiante_id, codigos_materias, periodo):
        # 1. Validación de negocio: Verificar que el estudiante exista realmente
        estudiante_obj = self.estudiante_ctrl.obtener_por_id(estudiante_id)
        if not estudiante_obj:
            return False, f"Error de negocio: No existe un estudiante registrado con el ID {estudiante_id}."

        matriculas = self.listar()
        nuevo_id = 1 if not matriculas else max(mat.id for mat in matriculas) + 1

        try:
            # 2. Instanciamos Matrícula (el modelo valida internamente las materias y el periodo)
            nueva = Matricula(nuevo_id, estudiante_id, codigos_materias, periodo)
            matriculas.append(nueva)
            self.guardar(matriculas)
            return True, f"Matrícula registrada con éxito: {nueva.etiqueta()}"
        except ValueError as e:
            return False, f"Error de validación del modelo: {e}"

    def agregar_nota_a_matricula(self, matricula_id, nota):
        matriculas = self.listar()
        encontrada = False

        for mat in matriculas:
            if mat.id == matricula_id:
                try:
                    mat.agregar_calificacion(nota)
                    encontrada = True
                    break
                except ValueError as e:
                    return False, f"Error al agregar la nota: {e}"

        if not encontrada:
            return False, f"No se encontró ninguna matrícula con el ID {matricula_id}."

        self.guardar(matriculas)
        return True, "Nota agregada correctamente y promedio recalculado."