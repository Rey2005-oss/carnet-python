"""
controllers/config_controller.py
--------------------------------
Capa de control para la configuración de la institución.
Equivalente a: controllers/ConfigController.java
"""

from typing import Optional
from models.configuracion import Configuracion
import services.config_service as svc


class ConfigController:

    def obtener(self) -> Optional[Configuracion]:
        """TODO: Llama a svc.obtener()"""
        pass

    def guardar(self, nombre: str, rif: str, direccion: str,
                telefono: str, director: str, periodo: str,
                logo_path: Optional[str] = None) -> bool:
        """
        TODO:
          1. Crea un objeto Configuracion con estos campos.
          2. Llama a svc.guardar_o_actualizar(cfg) y devuelve el resultado.
        """
        pass
