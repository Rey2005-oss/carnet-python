from dataclasses import dataclass
from typing import Optional

@dataclass
class Estudiante:
    cedula:    str = ""
    nombres:   str = ""
    apellidos: str = ""
    grado:     str = ""
    seccion:   str = ""
    foto_path: Optional[str] = None
    id:        int = 0

    @property
    def nombre_completo(self) -> str:
        return f"{self.nombres} {self.apellidos}"

    def __str__(self) -> str:
        return f"{self.nombre_completo} | {self.cedula} | {self.grado}-{self.seccion}"
