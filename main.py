"""
main.py
-------
Punto de entrada de la aplicación en Python.

Responsabilidades:
  1. Validar que la conexión a la base de datos MySQL esté disponible.
     Si falla, mostrar un error entendible antes de lanzar ventanas.
  2. Iniciar la ventana de Login (LoginView).
  3. Al recibir confirmación de éxito en el login, destruir el login y
     lanzar la ventana principal (MainView).
"""

import tkinter as tk
from tkinter import messagebox
from models.usuario import Usuario


def iniciar_aplicacion_principal(usuario: Usuario) -> None:
    """
    Función que se ejecuta cuando el login es correcto.
    TODO Pasante:
      1. Importa MainView desde views.main_view.
      2. Instancia la ventana pasándole el objeto 'usuario': app = MainView(usuario).
      3. Ejecuta el bucle principal: app.mainloop().
    """
    pass


def main() -> None:
    """
    TODO Pasante:
      1. Prueba la conexión a la base de datos importando get_connection() de config.conexion.
         try:
             conn = get_connection()
             conn.close()
         except Exception as e:
             # Muestra un popup avisando que MySQL no está activo o la BD no existe.
             return

      2. Importa LoginView desde views.login_view.
      3. Crea la instancia pasándole como callback la función iniciar_aplicacion_principal:
         login = LoginView(on_login_success=iniciar_aplicacion_principal)
      4. Ejecuta login.mainloop().
    """
    pass


if __name__ == "__main__":
    main()
