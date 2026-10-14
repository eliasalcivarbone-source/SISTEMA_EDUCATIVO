import os
import json
from models import Estudiante,Docente

class ControladorJson:
    def __init__(self,carpeta="data"):
        self.carpeta=carpeta
        if not os.path.exists(self.carpeta):
            os.makedirs(self.carpeta)
            
    def guardar_datos(self,ruta_archivo,lista_objetos):
        ruta=os.path.join(self.carpeta,ruta_archivo)
        datos_json=[obj.a_diccionario() for obj in lista_objetos]
    
    
        try:
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos_json, archivo, indent=4, ensure_ascii=False)
            print(f" Datos guardados exitosamente en {ruta}")
        except Exception as e:
            print(f" Error al guardar el archivo {ruta}: {e}")

    def cargar_datos(self, nombre_archivo, clase_modelo):
        """Lee el archivo JSON y reconstruye los objetos usando desde_diccionario()."""
        ruta = os.path.join(self.carpeta, nombre_archivo)
        
        # Si el archivo no existe aún, retornamos una lista vacía
        if not os.path.exists(ruta):
            return []
        
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos_json = json.load(archivo)
                # Reconstruimos dinámicamente cada objeto usando el método de clase
                return [clase_modelo.desde_diccionario(item) for item in datos_json]
        except Exception as e:
            print(f" Error al cargar el archivo {ruta}: {e}")
            return []
        
        
        
    
    
    
if __name__ == "__main__":
    print("--- PRUEBA DE PERSISTENCIA JSON ---")
    
    # Inicializamos nuestro controlador de archivos
    controlador = ControladorJson()
    
    # 1. Creamos listas de objetos válidos (Estudiantes y Docentes)
    estudiantes_prueba = [
        Estudiante(1, "Carlos", "Pérez", "carlos.perez@email.com", "0991234567", "EST-2026-001", "Matemáticas"),
        Estudiante(2, "María", "López", "maria.lopez@email.com", "0997654321", "EST-2026-002", "Literatura")
    ]
    
    docentes_prueba = [
        Docente(1, "Ana", "Gómez", "ana.gomez@colegio.edu", "+593987654321", "Física", "Magíster")
    ]
    
    # 2. Guardamos los objetos en los archivos correspondientes dentro de 'data/'
    print("\n[Guardando registros...]")
    controlador.guardar_datos("estudiantes.json", estudiantes_prueba)
    controlador.guardar_datos("docentes.json", docentes_prueba)
    
    print("\n" + "="*50 + "\n")
    
    # 3. Probamos cargar los datos de vuelta a la memoria RAM desde el JSON
    print("[Cargando registros desde los archivos...] Ruta: data/")
    estudiantes_cargados = controlador.cargar_datos("estudiantes.json", Estudiante)
    docentes_cargados = controlador.cargar_datos("docentes.json", Docente)
    
    print("\n--- Estudiantes recuperados en memoria ---")
    for est in estudiantes_cargados:
        print(f"Objeto impreso: {est}") # Prueba el __str__ y la etiqueta polimórfica
        print(f"Diccionario: {est.a_diccionario()}\n")
        
    print("--- Docentes recuperados en memoria ---")
    for doc in docentes_cargados:
        print(f"Objeto impreso: {doc}")
        print(f"Diccionario: {doc.a_diccionario()}\n")