"""
controllers/usuario_controller.py
---------------------------------
Capa intermedia entre las vistas y el servicio de usuarios.
Equivalente a: controllers/UsuarioController.java

El controlador no sabe de SQL (eso lo hace el servicio) ni sabe de botones
o ventanas (eso lo hace la vista). Simplemente coordina los datos.
"""

from typing import List, Optional
from models.usuario import Usuario
import services.usuario_service as svc


class UsuarioController:

    def listar(self) -> List[Usuario]:
        """
        Retorna la lista de todos los usuarios.
        TODO: Llama a svc.listar() y devuelve su resultado.
        """
        pass

    def buscar(self, query: str) -> List[Usuario]:
        """
        Busca usuarios según el término ingresado.
        TODO: Llama a svc.buscar(query).
        """
        pass

    def login(self, username: str, password: str) -> Optional[Usuario]:
        """
        Valida credenciales de acceso.
        TODO: Llama a svc.login(username, password).
        """
        pass

    def logout(self, usuario_id: int) -> None:
        """
        Cierra la sesión del usuario.
        TODO: Llama a svc.logout(usuario_id).
        """
        pass

    def registrar(self, username: str, password: str, full_name: str, role: str = "operador") -> bool:
        """
        Crea un objeto Usuario y solicita guardarlo.
        TODO:
          1. Crea una instancia de Usuario(username=username, password="", full_name=full_name, role=role).
          2. Llama a svc.crear(u, password) y retorna el booleano resultante.
        """
        pass

    def actualizar(self, usuario: Usuario, nueva_password: Optional[str] = None) -> bool:
        """
        Actualiza los datos de un usuario.
        TODO: Llama a svc.actualizar(usuario, nueva_password).
        """
        pass

    def eliminar(self, usuario_id: int) -> bool:
        """
        Elimina un usuario por ID.
        TODO: Llama a svc.eliminar(usuario_id).
        """
        pass
