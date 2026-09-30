from dataclasses import dataclass
from typing import Optional

@dataclass
class Configuracion:
    nombre_institucion: str = ""
    rif:                str = ""
    direccion:          str = ""
    telefono:           str = ""
    director:           str = ""
    periodo_escolar:    str = ""
    logo_path:          Optional[str] = None
    id:                 int = 0
