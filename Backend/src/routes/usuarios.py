from fastapi import APIRouter
from src.controllers.usuarios import listar_avaliadores

router = APIRouter()

@router.get('/avaliadores')
def obter_avaliadores():
    return listar_avaliadores()