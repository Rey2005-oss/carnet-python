"""
views/config_view.py
--------------------
Ventana de configuración de los datos de la institución educativa.
Equivalente a: views/Configviews.java
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from controllers.config_controller import ConfigController


class ConfigView(tk.Toplevel):

    def __init__(self, parent: tk.Widget):
        super().__init__(parent)
        self._ctrl = ConfigController()
        self._logo_path: str = ""

        self.title("Configuración de la Institución")
        self.geometry("540x460")
        self.resizable(False, False)
        self.grab_set()  # Hace la ventana modal (bloquea la ventana padre)

        # TODO Pasante:
        # 1. self._construir_ui()
        # 2. self._cargar_datos()

    def _construir_ui(self) -> None:
        """
        TODO Pasante:
        Crea los campos:
          - Nombre Institución
          - RIF / Código
          - Dirección
          - Teléfono
          - Director(a)
          - Período Escolar
          - Selector de archivo para el Logo (opcional)
          - Botón para 'Guardar Configuración'
        """
        pass

    def _cargar_datos(self) -> None:
        """
        TODO Pasante:
        Consulta la configuración existente: cfg = self._ctrl.obtener()
        Si existe, puebla los campos de texto con los valores correspondientes.
        """
        pass

    def _guardar(self) -> None:
        """
        TODO Pasante:
        Lee los datos del formulario y llama a:
        self._ctrl.guardar(nombre, rif, direccion, telefono, director, periodo, logo_path)
        Informa del resultado con messagebox.
        """
        pass
