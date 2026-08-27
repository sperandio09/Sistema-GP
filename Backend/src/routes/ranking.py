from fastapi import APIRouter, HTTPException
from src.controllers.ranking import obter_status_divulgacao, obter_ranking_salvo
from src.models import DivulgacaoUpdate
from src.controllers.ranking import atualizar_divulgacao
from src.controllers.ranking import obter_desempenho_escuderia 

router = APIRouter()

@router.get('/divulgacao')
def status_divulgacao():
    status = obter_status_divulgacao()
    if status is None:
        return {'mostrar_resultado': False, 'data_divulgacao': None}
    return status 

@router.get("/ranking")
def obter_ranking():
    status = obter_status_divulgacao()
    if not status or not status["mostrar_resultado"]:
        raise HTTPException(status_code=403, detail="O ranking ainda não foi divulgado.")
    return obter_ranking_salvo()

@router.post('/divulgacao')
def definir_divulgacao(dados: DivulgacaoUpdate):
    atualizar_divulgacao(dados.mostrar_resultado, dados.data_divulgacao)
    return{'mensagem': 'Divulgação atualizada com sucesso.'}

@router.get('/escuderias/{id_escuderia}/desempenho')
def desempenho_escuderia(id_escuderia: int):
    status = obter_status_divulgacao()
    if not status or not status['mostrar_resultado']:
        raise HTTPException(status_code=403, detail='O resultado ainda não foi divulgado.')

    resultado = obter_desempenho_escuderia(id_escuderia)
    if resultado is None:
        raise HTTPException(status_code=404, detail='Escuderia não encontrada ou sem avaliações.')

    return resultado
