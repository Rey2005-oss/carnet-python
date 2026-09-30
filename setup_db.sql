-- ============================================
-- Script de creación de la BD: carnetescolar
-- Version: 1.0 de Jean Carlos 
-- ============================================

CREATE DATABASE IF NOT EXISTS carnetescolar
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE carnetescolar;

-- --------------------------
-- Tabla: usuarios
-- --------------------------
CREATE TABLE IF NOT EXISTS usuarios (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    username    VARCHAR(50)  NOT NULL UNIQUE,
    password    VARCHAR(255) NOT NULL,           -- hash bcrypt
    full_name   VARCHAR(100) NOT NULL,
    role        ENUM('admin','operador') NOT NULL DEFAULT 'operador',
    active      TINYINT(1)   NOT NULL DEFAULT 1,
    online      TINYINT(1)   NOT NULL DEFAULT 0,
    created_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP,
    updated_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    last_login  TIMESTAMP    NULL
) ENGINE=InnoDB;

-- Usuario administrador por defecto  (password: admin123)
INSERT IGNORE INTO usuarios (username, password, full_name, role)
VALUES (
    'admin',
    '$2b$12$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uDutYHnaK', -- bcrypt de 'admin123'
    'Administrador',
    'admin'
);

-- --------------------------
-- Tabla: estudiantes
-- --------------------------
CREATE TABLE IF NOT EXISTS estudiantes (
    id          INT AUTO_INCREMENT PRIMARY KEY,
    cedula      VARCHAR(20)  NOT NULL UNIQUE,
    nombres     VARCHAR(100) NOT NULL,
    apellidos   VARCHAR(100) NOT NULL,
    grado       VARCHAR(20)  NOT NULL,
    seccion     VARCHAR(10)  NOT NULL,
    foto_path   VARCHAR(255) DEFAULT NULL,
    created_at  TIMESTAMP    DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB;

-- --------------------------
-- Tabla: configuracion
-- --------------------------
CREATE TABLE IF NOT EXISTS configuracion (
    id                  INT AUTO_INCREMENT PRIMARY KEY,
    nombre_institucion  VARCHAR(150) NOT NULL,
    rif                 VARCHAR(30)  DEFAULT NULL,
    direccion           TEXT         DEFAULT NULL,
    telefono            VARCHAR(30)  DEFAULT NULL,
    director            VARCHAR(100) DEFAULT NULL,
    periodo_escolar     VARCHAR(20)  DEFAULT NULL,
    logo_path           VARCHAR(255) DEFAULT NULL
) ENGINE=InnoDB;

-- Configuración inicial de ejemplo
INSERT IGNORE INTO configuracion (id, nombre_institucion, rif, direccion, telefono, director, periodo_escolar)
VALUES (1, 'U.E. Mi Institución', 'J-00000000-0', 'Calle Principal, Ciudad', '0212-0000000', 'Prof. Director(a)', '2025-2026');
