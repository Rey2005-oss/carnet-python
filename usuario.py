from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Usuario:
    username:   str = ""
    password:   str = ""
    full_name:  str = ""
    role:       str = "operador"
    active:     bool = True
    online:     bool = False
    id:         int = 0
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    last_login: Optional[datetime] = None

    def __str__(self) -> str:
        return f"{self.full_name} ({self.username}) [{self.role}]"
