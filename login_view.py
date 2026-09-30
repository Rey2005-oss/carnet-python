"""
views/login_view.py
-------------------
Ventana de autenticación (Login).
Equivalente a: views/LoginViews.java

En Java se usaba JFrame y JPanel con NetBeans (.form).
En Python usamos 'tkinter' (o ttk) directamente por código.

Flujo del Login:
  1. El usuario introduce usuario y contraseña.
  2. Al pulsar 'Ingresar' (o dar Enter), se llama al método _validar_login().
  3. Se invoca UsuarioController().login(username, password).
  4. Si es correcto: se cierra esta ventana y se llama al callback on_login_success(usuario).
  5. Si falla: se muestra messagebox.showerror().
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Callable

from controllers.usuario_controller import UsuarioController
from models.usuario import Usuario


class LoginView(tk.Tk):

    def __init__(self, on_login_success: Callable[[Usuario], None]):
        super().__init__()
        self._controller = UsuarioController()
        self._on_success = on_login_success

        self.title("Sistema de Carnetización - Login")
        self.resizable(False, False)

        # TODO Pasante:
        # 1. Configura el tamaño y posición de la ventana (ej: 400x300 centrada).
        # 2. Llama a un método propio self._construir_ui() para crear los controles.

    def _construir_ui(self) -> None:
        """
        TODO Pasante:
        Crea los elementos gráficos:
          - Label de título ("INICIO DE SESIÓN").
          - Label y Entry para 'Usuario' (self._txt_usuario).
          - Label y Entry con show='●' para 'Contraseña' (self._txt_password).
          - Button para 'Ingresar' que llame a self._validar_login.
          - Vincula la tecla Enter (<Return>) para disparar el login automáticamente.
        """
        pass

    def _validar_login(self) -> None:
        """
        TODO Pasante:
        1. Lee los valores con .get().strip().
        2. Si están vacíos, avisa con messagebox.showwarning().
        3. Llama a self._controller.login(user, pass).
        4. Si retorna un usuario:
             self.destroy()
             self._on_success(usuario)
           Si retorna None:
             messagebox.showerror("Error", "Credenciales incorrectas")
        """
        pass
