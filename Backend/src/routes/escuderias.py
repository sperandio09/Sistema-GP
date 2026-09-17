from fastapi import APIRouter 
from src.models import EscuderiaCreate 
from src.controllers.escuderias import criar_escuderia, listar_escuderias, listar_escuderias_avaliadas

router = APIRouter()

@router.post('/escuderias')
def cadastrar_escuderia(dados: EscuderiaCreate):
    novo_id = criar_escuderia(dados.nome, dados.turma, dados.nome_mentor)
    return {'id_escuderia': novo_id, 'message': 'Escuderia cadastrada com sucesso!'}

@router.get('/escuderias')
def obter_escuderias():
    return listar_escuderias()      

@router.get("/avaliadores/{id_avaliador}/escuderias-avaliadas")          
def obter_escuderias_avaliadas(id_avaliador: int):
    return listar_escuderias_avaliadas(id_avaliador)
