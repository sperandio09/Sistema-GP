from fastapi import APIRouter, HTTPException
from src.models import AvaliacaoCreate
from src.controllers.avaliacoes import criar_avaliacao

router = APIRouter()

@router.post('/avaliacoes')
def cadastrar_avaliacao(dados: AvaliacaoCreate):
    try:
        novo_id  = criar_avaliacao(dados.id_escuderia, dados.id_avaliador, dados.id_criterio, dados.nota, dados.comentario)
    except ValueError as erro:
        raise HTTPException(status_code=400, detail=str(erro))