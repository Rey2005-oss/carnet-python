import mysql.connector
from mysql.connector import Error

_CONFIG = {
    "host":       "localhost",
    "port":       3306,
    "database":   "carnetescolar",
    "user":       "root",
    "password":   "",
    "charset":    "utf8mb4",
    "autocommit": True,
}

def get_connection():
    try:
        return mysql.connector.connect(**_CONFIG)
    except Error as e:
        raise ConnectionError(f"No se pudo conectar a la BD: {e}")
