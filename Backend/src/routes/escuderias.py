from fastapi import APIRouter 
from src.models import EscuderiaCreate 
from src.controllers.escuderias import criar_escuderia

router = APIRouter()

@router.post('/escuderias')
def cadastrar_escuderia(dados: EscuderiaCreate):
    novo_id = criar_escuderia(dados.nome, dados.turma, dados.id_mentor)
    return {'id_escuderia': novo_id, 'message': 'Escuderia cadastrada com sucesso!'}