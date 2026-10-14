from controller_sistema_educativo import ControladorJson
from models import Materia

class MateriaController:
    def __init__(self):
        self.gestor = ControladorJson("data")
        self.archivo = "materias.json"

    def listar(self):
        return self.gestor.cargar_datos(self.archivo, Materia)

    def guardar(self, lista_materias):
        self.gestor.guardar_datos(self.archivo, lista_materias)

    def crear(self, codigo):
        materias = self.listar()
        
        # 1. Validación de negocio: que el código de la materia no se repita
        for mat in materias:
            if mat.codigo.upper() == codigo.upper():
                return False, f"Error de negocio: La materia con código '{codigo}' ya está registrada."

        # 2. Siguiente ID automático
        nuevo_id = 1 if not materias else max(m.id for m in materias) + 1

        try:
            # 3. Instanciamos la clase Materia (ella valida internamente contra las materias oficiales)
            nuevo = Materia(nuevo_id, codigo)
            materias.append(nuevo)
            self.guardar(materias)
            return True, f"Materia creada con éxito: {nuevo.etiqueta()}"
        except ValueError as e:
            return False, f"Error de validación del modelo: {e}"