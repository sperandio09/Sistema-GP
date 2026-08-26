from fastapi import APIRouter, HTTPException
from src.controllers.ranking import obter_status_divulgacao, calcular_ranking

router = APIRouter()

@router.get('/divulgacao')
def status_divulgacao():
    status = obter_status_divulgacao()
    if status is None:
        return {'mostrar_resultado': False, 'data_divulgacao': None}
    return status 

@router.get('/ranking')
def obter_ranking():
    status = obter_status_divulgacao()
    if not status or not status['mostrar_resultado']:
        raise HTTPException(status_code=403, detail='O ranking ainda não foi divulgado.')
    return calcular_ranking()