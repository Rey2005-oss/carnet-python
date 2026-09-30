"""
views/usuario_view.py
---------------------
Ventana de gestión de usuarios (CRUD).
Solo accesible por usuarios administradores.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from controllers.usuario_controller import UsuarioController
from models.usuario import Usuario


class UsuarioView(tk.Toplevel):

    def __init__(self, parent: tk.Widget):
        super().__init__(parent)
        self._ctrl = UsuarioController()
        self._seleccionado: Usuario | None = None

        self.title("Gestión de Usuarios")
        self.geometry("780x520")
        self.grab_set()

        # TODO Pasante:
        # 1. self._construir_ui()
        # 2. self._actualizar_tabla()

    def _construir_ui(self) -> None:
        """
        TODO Pasante:
        - Barra superior con buscador.
        - Tabla con columnas: ID, Usuario, Nombre Completo, Rol, Activo.
        - Panel lateral para crear/editar usuarios (Campos: username, password, full_name, rol, activo).
        - Botones CRUD: Crear, Actualizar, Eliminar, Limpiar.
        """
        pass

    def _actualizar_tabla(self, usuarios=None) -> None:
        """TODO Pasante: Llena la tabla con los usuarios de la base de datos."""
        pass

    def _seleccionar(self, event=None) -> None:
        """TODO Pasante: Carga el usuario seleccionado en el formulario lateral."""
        pass

    def _crear(self) -> None:
        """TODO Pasante: Registra un nuevo usuario llamando al controlador."""
        pass

    def _actualizar(self) -> None:
        """TODO Pasante: Actualiza los datos del usuario seleccionado."""
        pass

    def _eliminar(self) -> None:
        """TODO Pasante: Elimina al usuario tras confirmación."""
        pass
