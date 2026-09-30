"""
controllers/estudiante_controller.py
------------------------------------
Capa de control para estudiantes.
Equivalente a: controllers/EstudianteController.java
"""

from typing import List, Optional
from models.estudiante import Estudiante
import services.estudiante_service as svc


class EstudianteController:

    def listar(self) -> List[Estudiante]:
        """TODO: Llama a svc.listar()"""
        pass

    def buscar(self, query: str) -> List[Estudiante]:
        """TODO: Llama a svc.buscar(query)"""
        pass

    def obtener(self, estudiante_id: int) -> Optional[Estudiante]:
        """TODO: Llama a svc.obtener_por_id(estudiante_id)"""
        pass

    def registrar(self, cedula: str, nombres: str, apellidos: str,
                  grado: str, seccion: str, foto_path: Optional[str] = None) -> bool:
        """
        TODO:
          1. Crea un objeto Estudiante con estos datos.
          2. Llama a svc.guardar(estudiante) y devuelve el resultado.
        """
        pass

    def actualizar(self, estudiante: Estudiante) -> bool:
        """TODO: Llama a svc.actualizar(estudiante)"""
        pass

    def eliminar(self, estudiante_id: int) -> bool:
        """TODO: Llama a svc.eliminar(estudiante_id)"""
        pass
