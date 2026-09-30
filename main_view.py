"""
views/main_view.py
------------------
Ventana principal del sistema tras iniciar sesión.
Equivalente a: views/Mainviews.java
"""

import tkinter as tk
from tkinter import messagebox
from datetime import datetime

from models.usuario import Usuario
from controllers.usuario_controller import UsuarioController


class MainView(tk.Tk):

    def __init__(self, usuario: Usuario):
        super().__init__()
        self._usuario = usuario
        self._ctrl    = UsuarioController()

        self.title("Sistema de Carnetización - Panel Principal")
        self.geometry("800x500")

        # TODO Pasante:
        # 1. Configura el evento de cierre de ventana para cerrar sesión:
        #    self.protocol("WM_DELETE_WINDOW", self._cerrar)
        # 2. Llama a self._construir_ui()

    def _construir_ui(self) -> None:
        """
        TODO Pasante:
        Construye:
          - Una barra superior informativa (muestra el nombre del usuario y su rol).
          - La barra de menú principal (tk.Menu):
              * Menú 'Estudiantes' -> 'Gestionar Estudiantes'
              * Menú 'Configuración' -> 'Datos de la Institución'
              * Si self._usuario.role == 'admin':
                    Menú 'Usuarios' -> 'Gestionar Usuarios'
              * Menú 'Salir' -> 'Cerrar Sesión'
          - Un panel central con mensaje de bienvenida y accesos rápidos (botones).
        """
        pass

    def _abrir_estudiantes(self) -> None:
        """TODO: Importa EstudianteView y abre la ventana secundaria pasándole self."""
        pass

    def _abrir_usuarios(self) -> None:
        """TODO: Importa UsuarioView y abre la ventana secundaria pasándole self."""
        pass

    def _abrir_config(self) -> None:
        """TODO: Importa ConfigView y abre la ventana secundaria pasándole self."""
        pass

    def _cerrar(self) -> None:
        """
        TODO Pasante:
        Pregunta al usuario con messagebox.askyesno().
        Si confirma:
          - Llama a self._ctrl.logout(self._usuario.id)
          - Cierra la aplicación con self.destroy()
        """
        pass
