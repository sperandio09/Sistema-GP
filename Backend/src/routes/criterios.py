from fastapi import APIRouter
from src.controllers.criterios import listar_criterios

router = APIRouter()

@router.get('/criterios')
def obter_criterios():
    return listar_criterios()


