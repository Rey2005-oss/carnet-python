"""
services/estudiante_service.py
-------------------------------
Operaciones de base de datos para la tabla 'estudiantes'.
Equivalente a: servirces/EstudianteServirces.java

NOTA: En el código Java original, la clase se llama EstudianteServirces
(con error de tipeo). Aquí lo corregimos.

Referencia Java:
    public boolean guardarEstudiante(Estudiante e) { ... }
    public List<Estudiante> obtenerTodos() { ... }
    public boolean eliminarEstudiante(int id) { ... }

Tu versión tendrá más funciones que el Java original. (por eso me gusta python)
"""

# TODO: Importa get_connection
# TODO: Importa Estudiante
# TODO: Importa List y Optional desde typing


def _fila_a_estudiante(fila: dict):
    """
    Convierte una fila de la BD (diccionario) en un objeto Estudiante.

    La fila tendrá estas claves:
        "id", "cedula", "nombres", "apellidos", "grado", "seccion", "foto_path"

    TODO: Crea y retorna un objeto Estudiante con los datos de la fila
    """
    pass


def listar():
    """
    Retorna todos los estudiantes, ordenados por apellidos y luego nombres.

    SQL:
        SELECT * FROM estudiantes ORDER BY apellidos, nombres

    TODO: Implementa
    """
    pass


def buscar(query: str):
    """
    Busca estudiantes por cédula, nombres o apellidos.

    SQL:
        SELECT * FROM estudiantes
        WHERE cedula LIKE %s OR nombres LIKE %s OR apellidos LIKE %s
        ORDER BY apellidos, nombres

    TODO: Implementa (recuerda el patrón "%query%")
    """
    pass


def obtener_por_id(estudiante_id: int):
    """
    Retorna un estudiante específico por su ID, o None si no existe.

    SQL:
        SELECT * FROM estudiantes WHERE id=%s

    TODO: Implementa usando fetchone() en vez de fetchall()
    """
    pass


def guardar(estudiante) -> bool:
    """
    Inserta un nuevo estudiante en la base de datos.

    SQL:
        INSERT INTO estudiantes (cedula, nombres, apellidos, grado, seccion, foto_path)
        VALUES (%s, %s, %s, %s, %s, %s)

    Returns:
        True si se guardó, False si hubo error (por ej. cédula duplicada).

    TODO: Implementa
    """
    pass


def actualizar(estudiante) -> bool:
    """
    Actualiza los datos de un estudiante existente.

    SQL:
        UPDATE estudiantes
        SET cedula=%s, nombres=%s, apellidos=%s, grado=%s, seccion=%s, foto_path=%s
        WHERE id=%s

    Returns:
        True si se actualizó, False si hubo error.

    TODO: Implementa
    """
    pass


def eliminar(estudiante_id: int) -> bool:
    """
    Elimina un estudiante por su ID.

    SQL:
        DELETE FROM estudiantes WHERE id=%s

    Returns:
        True si se eliminó, False si hubo error.

    TODO: Implementa
    """
    pass
