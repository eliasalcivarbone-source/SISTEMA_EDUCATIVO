from controller_sistema_educativo import ControladorJson
from models import Docente  # Importamos la clase Docente de models.py

class DocenteController:
    def __init__(self):
        # Usamos tu gestor JSON existente apuntando a docentes.json
        self.gestor = ControladorJson("data")
        self.archivo = "docentes.json"

    def listar(self):
        # Carga los docentes del JSON
        return self.gestor.cargar_datos(self.archivo, Docente)

    def guardar(self, lista_docentes):
        # Guarda la lista usando tu gestor
        self.gestor.guardar_datos(self.archivo, lista_docentes)

    def crear(self, nombre, apellido, correo, telefono, especialidad, titulo):
        docentes = self.listar()
        
        # 1. Validación de negocio: que el correo del docente no se repita
        for doc in docentes:
            if doc.correo.lower() == correo.lower():
                return False, f"Error de negocio: El correo '{correo}' ya está registrado por otro docente."

        # 2. Calcular el siguiente ID automáticamente
        nuevo_id = 1 if not docentes else max(d.id for d in docentes) + 1

        try:
            # 3. Instanciamos la clase Docente con sus parámetros reales
            nuevo = Docente(nuevo_id, nombre, apellido, correo, telefono, especialidad, titulo)
            docentes.append(nuevo)
            self.guardar(docentes)
            return True, f"Docente creado con éxito: {nuevo.etiqueta()}"
        except ValueError as e:
            return False, f"Error de validación del modelo: {e}"