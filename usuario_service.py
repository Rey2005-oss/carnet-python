"""
services/usuario_service.py
----------------------------
Operaciones de base de datos para la tabla 'usuarios'.
Equivalente a: servirces/UsuarioService.java

IMPORTANTE: A diferencia del código Java original, aquí NO guardamos
las contraseñas en texto plano. Usamos bcrypt para hacerlas seguras.

¿Por qué bcrypt?
    Si alguien roba la base de datos, no podrá ver las contraseñas reales
    porque están cifradas. Es una práctica de seguridad básica.

¿Cómo funciona bcrypt?
    import bcrypt

    # Para GUARDAR una contraseña nueva:
    texto_plano = "mi_contraseña"
    hash_seguro = bcrypt.hashpw(texto_plano.encode(), bcrypt.gensalt())
    # hash_seguro es lo que guardas en la BD (se ve como: $2b$12$abc...)

    # Para VERIFICAR al hacer login:
    es_correcta = bcrypt.checkpw(texto_plano.encode(), hash_guardado_en_bd)

Patrón de cada función:
    def mi_funcion(parametros):
        sql = "CONSULTA SQL AQUÍ"
        conn = get_connection()      # 1. Abrir conexión
        try:
            with conn.cursor(dictionary=True) as cur:
                cur.execute(sql, (parametros,))
                resultado = cur.fetchall()  # o fetchone()
            return resultado
        except Exception as e:
            print(f"Error: {e}")
            return None  # o False
        finally:
            conn.close()             # 2. SIEMPRE cerrar la conexión
"""

# TODO: Importa bcrypt
# TODO: Importa get_connection desde config.conexion
# TODO: Importa Usuario desde models.usuario
# TODO: Importa List y Optional desde typing


# ── Funciones auxiliares de contraseña ───────────────────────────────────────

def _hash_password(password_texto_plano: str) -> str:
    """
    Convierte una contraseña en texto plano a un hash seguro con bcrypt.

    TODO: Implementa usando bcrypt.hashpw()
    Pista: bcrypt.hashpw() recibe bytes, no string. Usa .encode()
    """
    # TODO: Implementa
    pass


def _verificar_password(password_texto_plano: str, hash_guardado: str) -> bool:
    """
    Verifica si una contraseña en texto plano coincide con el hash guardado.
    Retorna True si coincide, False si no.

    TODO: Implementa usando bcrypt.checkpw()
    """
    # TODO: Implementa
    pass


# ── Función auxiliar para convertir una fila de BD en un objeto Usuario ──────

def _fila_a_usuario(fila: dict):
    """
    Recibe un diccionario con los datos de una fila de la tabla 'usuarios'
    y retorna un objeto Usuario.

    Ejemplo de 'fila':
        {
            "id": 1,
            "username": "admin",
            "password": "$2b$12$...",
            "full_name": "Administrador",
            "role": "admin",
            "active": 1,
            "online": 0,
            ...
        }

    TODO: Crea y retorna un objeto Usuario con los datos de la fila
    Pista: active y online vienen como 0/1 de MySQL, conviértelos a bool
    """
    # TODO: Implementa
    pass


# ── Operaciones CRUD ─────────────────────────────────────────────────────────

def listar():
    """
    Retorna todos los usuarios de la base de datos, ordenados por nombre.

    SQL a usar:
        SELECT * FROM usuarios ORDER BY full_name

    Returns:
        Lista de objetos Usuario. Lista vacía si no hay ninguno.

    Equivalente Java:
        public List<Usuario> listar() { ... }

    TODO: Implementa esta función
    """
    pass


def buscar(query: str):
    """
    Busca usuarios cuyo username O nombre completo contengan el texto buscado.

    SQL a usar:
        SELECT * FROM usuarios WHERE username LIKE %s OR full_name LIKE %s

    Pista: Para buscar "cualquier cosa que contenga juan" usa: "%juan%"
           En Python: patron = f"%{query}%"

    TODO: Implementa
    """
    pass


def login(username: str, password: str):
    """
    Verifica las credenciales de un usuario.

    Proceso:
        1. Busca el usuario en BD por su username
        2. Si existe y está activo, verifica la contraseña con bcrypt
        3. Si la contraseña es correcta, actualiza last_login y online=1
        4. Retorna el objeto Usuario si todo está bien, None si no

    SQL para buscar:
        SELECT * FROM usuarios WHERE username = %s AND active = 1

    SQL para actualizar last_login:
        UPDATE usuarios SET last_login=NOW(), online=1 WHERE id=%s

    TODO: Implementa
    """
    pass


def crear(usuario, password_texto_plano: str) -> bool:
    """
    Inserta un nuevo usuario en la base de datos.
    La contraseña se guarda como hash bcrypt (¡nunca en texto plano!).

    SQL a usar:
        INSERT INTO usuarios (username, password, full_name, role, active)
        VALUES (%s, %s, %s, %s, %s)

    Returns:
        True si se creó correctamente, False si hubo error.

    TODO: Implementa
    """
    pass


def actualizar(usuario, nueva_password: str = None) -> bool:
    """
    Actualiza los datos de un usuario existente.
    Si nueva_password no es None, también actualiza la contraseña (con hash).

    SQL sin cambio de contraseña:
        UPDATE usuarios SET username=%s, full_name=%s, role=%s, active=%s
        WHERE id=%s

    SQL con cambio de contraseña:
        UPDATE usuarios SET username=%s, password=%s, full_name=%s, role=%s, active=%s
        WHERE id=%s

    Returns:
        True si se actualizó, False si hubo error.

    TODO: Implementa
    """
    pass


def eliminar(usuario_id: int) -> bool:
    """
    Elimina un usuario de la base de datos por su ID.

    SQL:
        DELETE FROM usuarios WHERE id=%s

    Returns:
        True si se eliminó, False si hubo error.

    TODO: Implementa
    """
    pass


def logout(usuario_id: int) -> None:
    """
    Marca al usuario como 'no online' cuando cierra sesión.

    SQL:
        UPDATE usuarios SET online=0 WHERE id=%s

    TODO: Implementa
    """
    pass
