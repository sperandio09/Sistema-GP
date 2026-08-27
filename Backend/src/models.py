from pydantic import BaseModel
from datetime import datetime

class EscuderiaCreate(BaseModel):
    nome: str
    turma: str
    id_mentor: int

class AvaliacaoCreate(BaseModel):
    id_escuderia: int 
    id_avaliador: int 
    id_criterio: int
    nota: float
    comentario: str | None = None

class DivulgacaoUpdate(BaseModel):
    mostrar_resultado: bool
    data_divulgacao: datetime  