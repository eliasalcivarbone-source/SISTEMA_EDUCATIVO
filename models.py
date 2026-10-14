from abc import ABC, abstractmethod

class ModeloBase(ABC):
    "molde con el cual vamos a crear nuestras clases "
    CAMPOS=()
    OBLIGATORIO=()
    def __init__(self,id_registro):
        self.id=id_registro
    @property
    def id(self):
        return self.__id_registro
    
    @id.setter
    def id(self,valor):
        try:
            valor_entero=int(valor)
        except (TypeError,ValueError):
            raise ValueError(f"el id deve ser un numero valido se recibio :{valor}")
    
  
        if valor_entero<=0:
            raise ValueError("el id deve ser mayor a 0")
        
        else: self.__id_registro=valor_entero
        
    
        
    @staticmethod
    def limpiar_texto(texto):
        return str(texto).strip()
    
    @abstractmethod
    def a_diccionario(self):
        pass
    
    @abstractmethod
    def etiqueta(self):
        pass
   

    @classmethod
    def desde_diccionario(cls, datos):
        """Reconstruye dinámicamente cualquier clase usando sus CAMPOS oficiales."""
        valores = {campo: datos.get(campo, "") for campo in cls.CAMPOS}
        return cls(datos["id"], **valores)

    def __str__(self):
        return f"[{self.id}] {self.etiqueta()}"
    
    
    
class Persona(ModeloBase):
    CAMPOS=("nombre","apellido","correo","telefono")
    OBLIGATORIOS=("nombre","apellido")
    def __init__(self,id_registro,nombre,apellido,correo,telefono):
        super().__init__(id_registro)
        self.nombre=nombre
        self.apellido=apellido
        self.correo=correo
        self.telefono=telefono
        
    def a_diccionario(self):
        return{
            "id": self.id,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "correo":self.correo,
            "telefono":self.telefono,
       
        }
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        limpio = self.limpiar_texto(valor)
        if not limpio:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = limpio

    # --- PROPIEDAD Y VALIDACIÓN DE APELLIDO ---
    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        limpio = self.limpiar_texto(valor)
        if not limpio:
            raise ValueError("El apellido no puede estar vacío.")
        self._apellido = limpio

    # --- PROPIEDAD Y VALIDACIÓN DE CORREO ---
    @property
    def correo(self):
        return self._correo

    @correo.setter
    def correo(self, valor):
        # Validación defensiva del correo (ejemplo: que tenga '@' y '.')
        if not valor or "@" not in valor or "." not in valor:
            raise ValueError(f"Correo electrónico inválido: '{valor}'. Debe contener '@' y un dominio.")
        self._correo = valor.strip().lower()

    # --- PROPIEDAD Y VALIDACIÓN DE TELÉFONO ---
    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        # Puedes validar que contenga números o una longitud mínima
        str_val = str(valor).strip()
        if not str_val.isdigit() and not (str_val.startswith("+") and str_val[1:].isdigit()):
            raise ValueError(f"Teléfono inválido: '{valor}'. Solo debe contener dígitos.")
        self._telefono = str_val

    
class Estudiante(Persona):
    CAMPOS=("nombre","apellido","correo","telefono","carnet","materia")
    OBLIGATORIOS=("nombre","apellido","carnet","materia")
    def __init__(self,id_registro,nombre,apellido,correo,telefono,carnet,materia,):
         super().__init__(id_registro,nombre,apellido,correo,telefono)
         self.carnet=carnet
         self.materia=materia
         
    def a_diccionario(self):
        return{
            "id": self.id,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "correo":self.correo,
            "telefono":self.telefono,
            "carnet":self.carnet,
            "materia":self.materia
            
        }
        
    def etiqueta (self):
        return f"{self.nombre} {self.apellido} {self.carnet}"
    
    
        

class Docente(Persona):
    CAMPOS=("nombre","apellido","correo","telefono","especialidad","titulo")
    OBLIGATORIOS=("nombre","apellido","especialidad","titulo")
    def __init__(self,id_registro,nombre,apellido,correo,telefono,especialidad,titulo,):
         super().__init__(id_registro,nombre,apellido,correo,telefono)
         self.especialidad=especialidad
         self.titulo=titulo
         
    def a_diccionario(self):
        return{
            "id": self.id,
            "nombre":self.nombre,
            "apellido":self.apellido,
            "correo":self.correo,
            "telefono":self.telefono,
            "especialidad":self.especialidad,
            "titulo": self.titulo
            
        }
        
    def etiqueta (self):
        return f"{self.nombre} {self.apellido} {self.especialidad} {self.titulo}"
    
    


if __name__ == "__main__":
    print("--- PRUEBAS DE SISTEMA ESCOLAR ---")
    
    try:
        # 1. Instanciamos un Estudiante válido
        estudiante1 = Estudiante(
            id_registro=1,
            nombre="  Carlos  ",       # Debería limpiarse con strip() gracias a limpiar_texto
            apellido="Pérez",
            correo="carlos.perez@email.com",
            telefono="0991234567",
            carnet="EST-2026-001",
            materia="Matemáticas"
        )
        
        # Gracias al __str__ heredado de ModeloBase y la etiqueta polimórfica:
        print(estudiante1) 
        print("Diccionario:", estudiante1.a_diccionario())
        
        print("\n" + "="*40 + "\n")
        
        # 2. Instanciamos un Docente válido
        docente1 = Docente(
            id_registro=2,
            nombre="Ana",
            apellido="Gómez",
            correo="ana.gomez@colegio.edu",
            telefono="+593987654321",
            especialidad="Física",
            titulo="Magíster"
        )
        
        print(docente1)
        print("Diccionario:", docente1.a_diccionario())
        
        print("\n" + "="*40 + "\n")
        print("Probando validaciones defensivas (esto debería fallar):")
        
        # 3. Intentamos crear un estudiante con correo inválido para probar el fail-fast
        estudiante_malo = Estudiante(
            id_registro=3,
            nombre="Luis",
            apellido="Vera",
            correo="correo_sin_arroba_ni_punto", # <-- Esto debe disparar el ValueError del setter
            telefono="12345",
            carnet="EST-002",
            materia="Historia"
        )

    except ValueError as e:
        print(f" ¡Bloqueo defensivo exitoso! El sistema atrapó el error: {e}")
        
        


class Materia(ModeloBase):
    # Catálogo institucional predefinido (Atributo de clase)
    MATERIAS_OFICIALES = {
        "MAT-101": {"nombre": "Matemáticas I", "creditos": 4},
        "LIT-102": {"nombre": "Literatura Universal", "creditos": 3},
        "FIS-103": {"nombre": "Física General", "creditos": 4},
        "HIS-104": {"nombre": "Historia Contemporánea", "creditos": 3},
        "QUI-105": {"nombre": "Química Básica", "creditos": 4}
    }

    CAMPOS = ("codigo", "nombre", "creditos")
    OBLIGATORIOS = ("codigo", "nombre")

    def __init__(self, id_registro, codigo):
        super().__init__(id_registro)
        self.codigo = codigo # Utilizará un setter con validación defensiva
      

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El código de la materia no puede estar vacío.")
        
        # Validación defensiva contra el catálogo del sistema
        if valor not in Materia.MATERIAS_OFICIALES:
            raise ValueError(f"Error defensivo: La materia con código '{valor}' no existe en el catálogo oficial del sistema.")
        
        self._codigo = valor
        # Extraemos automáticamente los datos oficiales del catálogo
        self._nombre = Materia.MATERIAS_OFICIALES[valor]["nombre"]
        self._creditos = Materia.MATERIAS_OFICIALES[valor]["creditos"]

    @property
    def nombre(self):
        return self._nombre

    @property
    def creditos(self):
        return self._creditos

    @creditos.setter
    def creditos(self, valor):
        # Validación defensiva de créditos: debe ser un número entero positivo
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError(f"Error defensivo: Los créditos deben ser un número entero mayor a 0. Se recibió: {valor}")
        self._creditos = valor

    def a_diccionario(self):
        return {
            "id": self.id,
            "codigo": self.codigo,
            "nombre": self.nombre,
            "creditos": self.creditos
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            id_registro=datos["id"],
            codigo=datos["codigo"]
        )
    def etiqueta(self):
        return f"[Materia Oficial] {self.codigo} - {self.nombre} ({self.creditos} Créditos)"
   
   




class Nota(ModeloBase):
    CAMPOS = ("estudiante_id", "codigo_materia", "calificaciones")
    OBLIGATORIOS = ("estudiante_id", "codigo_materia")

    def __init__(self, id_registro, estudiante_id, codigo_materia, calificaciones=None):
        super().__init__(id_registro)
        self.estudiante_id = estudiante_id
        self.codigo_materia = codigo_materia
        # Si no se pasan calificaciones, inicializamos una lista vacía
        self.calificaciones = calificaciones if calificaciones is not None else []

    @property
    def estudiante_id(self):
        return self._estudiante_id

    @estudiante_id.setter
    def estudiante_id(self, valor):
        if not valor:
            raise ValueError("El ID del estudiante no puede estar vacío.")
        self._estudiante_id = valor

    @property
    def codigo_materia(self):
        return self._codigo_materia

    @codigo_materia.setter
    def codigo_materia(self, valor):
        if not valor or not isinstance(valor, str):
            raise ValueError("El código de la materia debe ser un texto válido.")
        self._codigo_materia = valor

    @property
    def calificaciones(self):
        return self._calificaciones

    @calificaciones.setter
    def calificaciones(self, lista_valores):
        if not isinstance(lista_valores, list):
            raise ValueError("Las calificaciones deben ser una lista de números.")
        
        # Validación defensiva: cada nota debe estar en un rango válido (ej. 0 a 10)
        for nota in lista_valores:
            if not isinstance(nota, (int, float)) or not (0 <= nota <= 10):
                raise ValueError(f"Calificación inválida: '{nota}'. Debe ser un número entre 0 y 10.")
        
        self._calificaciones = lista_valores

    def agregar_calificacion(self, nota):
        """Método útil para añadir una nueva nota validada a la lista."""
        if not isinstance(nota, (int, float)) or not (0 <= nota <= 10):
            raise ValueError(f"La calificación '{nota}' no es válida (debe ser de 0 a 10).")
        self._calificaciones.append(nota)

    @property
    def promedio(self):
        """Calcula el promedio de forma dinámica si hay calificaciones."""
        if not self._calificaciones:
            return 0.0
        return round(sum(self._calificaciones) / len(self._calificaciones), 2)

    def a_diccionario(self):
        return {
            "id": self.id,
            "estudiante_id": self.estudiante_id,
            "codigo_materia": self.codigo_materia,
            "calificaciones": self.calificaciones
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            id_registro=datos["id"],
            estudiante_id=datos["estudiante_id"],
            codigo_materia=datos["codigo_materia"],
            calificaciones=datos.get("calificaciones", [])
        )

    def etiqueta(self):
        return f"[Registro de Notas] Estudiante ID: {self.estudiante_id} | Materia: {self.codigo_materia} | Notas: {self.calificaciones} | Promedio: {self.promedio}"
    
    
    
    
    
class Matricula(ModeloBase):
        CAMPOS = ("estudiante_id", "codigos_materias", "periodo")
        OBLIGATORIOS = ("estudiante_id", "codigos_materias", "periodo")

        def __init__(self, id_registro, estudiante_id, codigos_materias, periodo):
             super().__init__(id_registro)
             self.estudiante_id = estudiante_id
             self.codigos_materias = codigos_materias
             self.periodo = periodo
 
        @property
        def estudiante_id(self):
           return self._estudiante_id

        @estudiante_id.setter
        def estudiante_id(self, valor):
          if not valor:
            raise ValueError("El ID del estudiante no puede estar vacío.")
          self._estudiante_id = valor

        @property
        def codigos_materias(self):
           return self._codigos_materias
   
        @codigos_materias.setter
        def codigos_materias(self, lista):
           if not isinstance(lista, list) or not lista:
              raise ValueError("Las materias matriculadas deben ser una lista no vacía.")
           for codigo in lista:
               if codigo not in Materia.MATERIAS_OFICIALES:
                  raise ValueError(f"Error defensivo: No se puede matricular en '{codigo}' porque no existe en el catálogo oficial.")
           self._codigos_materias = lista

        @property
        def periodo(self):
           return self._periodo

        @periodo.setter
        def periodo(self, valor):
           limpio = self.limpiar_texto(valor)
           if not limpio:
              raise ValueError("El periodo académico no puede estar vacío.")
           self._periodo = limpio

        def a_diccionario(self):
          return {
            "id": self.id,
            "estudiante_id": self.estudiante_id,
            "codigos_materias": self.codigos_materias,
            "periodo": self.periodo
        }

        @classmethod
        def desde_diccionario(cls, datos):
           return cls(
            id_registro=datos["id"],
            estudiante_id=datos["estudiante_id"],
            codigos_materias=datos.get("codigos_materias", []),
            periodo=datos.get("periodo", "")
        )

        def etiqueta(self):
           return f"[Matrícula - {self.periodo}] Estudiante ID: {self.estudiante_id} | Materias: {', '.join(self.codigos_materias)}"
       
       

class Curso(ModeloBase):
    CAMPOS=("paralelo","cantidad_estudiantes","docente_asignado")
    OBLIGATRIOS=("docente_asignado","paralelo")
    def __init__(self, id_registro, paralelo ,cantidad_estudiantes,docente_asignado):
        super().__init__(id_registro)
        self.paralelo=paralelo
        self.cantidad_estudiantes=cantidad_estudiantes
        self.docente_asignado=docente_asignado
        
        def a_diccionario(self):
            return {
                "paralelo": self.paralelo,
                "cantidad_estudiantes": self.cantidad_estudiantes,
                "docente_asignado": self.docente_asignado
            }       
        
        def etiqueta(self):
            return f"paralelo asignado {self.paralelo} cantidad de estudiantes {self.cantidad_estudiantes} docente asignado {self.docente_asignado}"
    
    
 