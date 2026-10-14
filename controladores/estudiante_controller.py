from controller_sistema_educativo import ControladorJson
from models import Estudiante  # <--- Importamos la clase que YA existe en models.py, NO la reescribimos

class EstudianteController:
    def __init__(self):
        # Usamos tu gestor JSON existente
        self.gestor = ControladorJson("data")
        self.archivo = "estudiantes.json"

    def listar(self):
        # Carga los estudiantes del JSON usando tu modelo Estudiante existente
        return self.gestor.cargar_datos(self.archivo, Estudiante)

    def guardar(self, lista_estudiantes):
        # Guarda la lista usando tu gestor
        self.gestor.guardar_datos(self.archivo, lista_estudiantes)

    def crear(self, nombre, apellido, correo, telefono, carnet, materia):
        estudiantes = self.listar()
        
        # 1. Validación de negocio: que el carnet no se repita
        for est in estudiantes:
            if est.carnet.upper() == carnet.upper():
                return False, f"Error de negocio: El carnet '{carnet}' ya está registrado."

        # 2. Calcular el siguiente ID automáticamente
        nuevo_id = 1 if not estudiantes else max(e.id for e in estudiantes) + 1

        try:
            # 3. Instanciamos la clase Estudiante que YA vive en models.py
            nuevo = Estudiante(nuevo_id, nombre, apellido, correo, telefono, carnet, materia)
            estudiantes.append(nuevo)
            self.guardar(estudiantes)
            return True, f"Estudiante creado con éxito: {nuevo.etiqueta()}"
        except ValueError as e:
            return False, f"Error de validación del modelo: {e}"