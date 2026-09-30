"""
views/estudiante_view.py
------------------------
Ventana de gestión de estudiantes (CRUD) y generación de carnets.
Equivalente a: views/EstudianteViews.java

Herencia:
  Hereda de tk.Toplevel porque es una ventana secundaria abierta desde MainView.
"""

import os
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk

from controllers.estudiante_controller import EstudianteController
from controllers.config_controller import ConfigController
from models.estudiante import Estudiante
from utils.carnet_generator import generar_carnet, exportar_pdf


class EstudianteView(tk.Toplevel):

    def __init__(self, parent: tk.Widget):
        super().__init__(parent)
        self._ctrl     = EstudianteController()
        self._cfg_ctrl = ConfigController()
        self._seleccionado: Estudiante | None = None
        self._foto_temp: str = ""

        self.title("Gestión de Estudiantes")
        self.geometry("900x580")

        # TODO Pasante:
        # 1. Construir la UI: self._construir_ui()
        # 2. Cargar los estudiantes existentes en la tabla: self._actualizar_tabla()

    def _construir_ui(self) -> None:
        """
        TODO Pasante:
        Diseña la pantalla con dos secciones principales:
          1. Lado Izquierdo:
             - Campo de búsqueda y botón refrescar.
             - Tabla ttk.Treeview con columnas: ID, Cédula, Nombres, Apellidos, Grado, Sección.
             - Scrollbar vertical asociado a la tabla.
             - Evento de selección: self._tabla.bind("<<TreeviewSelect>>", self._seleccionar)
          2. Lado Derecho (Formulario y Acciones):
             - Label para previsualizar foto + botón 'Cargar foto' (abre filedialog.askopenfilename).
             - Campos de texto para Cédula, Nombres, Apellidos, Grado y Sección.
             - Botones CRUD: 'Registrar', 'Actualizar', 'Eliminar', 'Limpiar'.
             - Botones de Carnet: 'Ver Carnet (PNG)' y 'Exportar PDF'.
        """
        pass

    def _actualizar_tabla(self, lista=None) -> None:
        """
        TODO Pasante:
        1. Limpia las filas actuales de la tabla: self._tabla.delete(*self._tabla.get_children())
        2. Obtiene los estudiantes (si lista es None, usa self._ctrl.listar()).
        3. Inserta cada estudiante en el Treeview.
        """
        pass

    def _seleccionar(self, event=None) -> None:
        """
        TODO Pasante:
        Al hacer clic en una fila del Treeview:
        1. Obtiene el ID del estudiante seleccionado.
        2. Carga el objeto Estudiante usando self._ctrl.obtener(id).
        3. Rellena los campos del formulario y muestra su foto si existe.
        """
        pass

    def _cargar_foto(self) -> None:
        """
        TODO Pasante:
        Abre un cuadro de diálogo para seleccionar imagen (png, jpg).
        Guarda la ruta seleccionada en self._foto_temp y actualiza la vista previa.
        """
        pass

    def _registrar(self) -> None:
        """
        TODO Pasante:
        1. Lee los valores del formulario.
        2. Valida que no estén vacíos.
        3. Llama a self._ctrl.registrar(...).
        4. Si tiene éxito, muestra mensaje, limpia el formulario y actualiza la tabla.
        """
        pass

    def _actualizar(self) -> None:
        """
        TODO Pasante:
        1. Verifica que haya un estudiante seleccionado (self._seleccionado is not None).
        2. Modifica sus atributos con los datos del formulario.
        3. Llama a self._ctrl.actualizar(self._seleccionado).
        """
        pass

    def _eliminar(self) -> None:
        """
        TODO Pasante:
        1. Pide confirmación al usuario (messagebox.askyesno).
        2. Si acepta, llama a self._ctrl.eliminar(self._seleccionado.id).
        3. Actualiza la tabla.
        """
        pass

    def _generar_carnet(self) -> None:
        """
        TODO Pasante:
        1. Verifica que haya un estudiante seleccionado.
        2. Obtiene la configuración de la institución: cfg = self._cfg_ctrl.obtener().
        3. Si no hay configuración, avisa al usuario que debe configurarla primero.
        4. Llama a generar_carnet(self._seleccionado, cfg).
        5. Informa la ruta generada y ábrela con el visor predeterminado del sistema.
        """
        pass
