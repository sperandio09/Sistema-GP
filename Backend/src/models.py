from pydantic import BaseModel

class EscuderiaCreate(BaseModel):
    nome: str
    turma: str
    id_mentor: int