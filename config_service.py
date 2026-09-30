"""
services/config_service.py
---------------------------
Operaciones de base de datos para la tabla 'configuracion'.
Equivalente a: servirces/ConfigService.java

PARTICULARIDAD:
    Esta tabla siempre tiene exactamente UN registro.
    Si no existe → hay que hacer INSERT.
    Si ya existe → hay que hacer UPDATE.
    A esto se le llama "upsert" (update + insert).

Referencia Java (la versión correcta estaba en la clase interna ConfigServices):
    public Configuracion obtenerConfiguracion() { ... }
    public boolean guardarOActualizar(Configuracion config) { ... }
"""

# TODO: Importa get_connection
# TODO: Importa Configuracion
# TODO: Importa Optional desde typing


def _fila_a_config(fila: dict):
    """
    Convierte una fila de la BD en un objeto Configuracion.

    La fila tiene estas claves:
        "id", "nombre_institucion", "rif", "direccion",
        "telefono", "director", "periodo_escolar", "logo_path"

    TODO: Implementa
    """
    pass


def obtener():
    """
    Retorna la configuración de la institución, o None si no existe.

    SQL:
        SELECT * FROM configuracion LIMIT 1

    Returns:
        Un objeto Configuracion, o None si la tabla está vacía.

    TODO: Implementa usando fetchone()
    """
    pass


def guardar_o_actualizar(config) -> bool:
    """
    Guarda o actualiza la configuración.

    Lógica:
        1. Llama a obtener() para ver si ya existe un registro
        2. Si NO existe → hace INSERT
        3. Si ya existe → hace UPDATE con el id del registro existente

    SQL para INSERT:
        INSERT INTO configuracion
        (nombre_institucion, rif, direccion, telefono, director, periodo_escolar, logo_path)
        VALUES (%s, %s, %s, %s, %s, %s, %s)

    SQL para UPDATE:
        UPDATE configuracion
        SET nombre_institucion=%s, rif=%s, direccion=%s,
            telefono=%s, director=%s, periodo_escolar=%s, logo_path=%s
        WHERE id=%s

    Returns:
        True si se guardó/actualizó, False si hubo error.

    TODO: Implementa
    """
    pass
