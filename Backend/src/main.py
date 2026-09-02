from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from src.routes.escuderias import router as escuderias_router
from src.routes.avaliacoes import router as avaliacoes_router 
from src.routes.criterios import router as criterios_router 
from src.routes.usuarios import router as usuarios_router 
from src.routes.ranking import router as ranking_router 

app = FastAPI(title = 'Sistema GP de Avaliação', version = '1.0.0')

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_methods = ['*'],
    allow_credentials = True,
    allow_headers = ['*']
)

app.include_router(escuderias_router)
app.include_router(avaliacoes_router)
app.include_router(criterios_router)
app.include_router(usuarios_router)
app.include_router(ranking_router)

@app.get('/')
def root():
    return {'status': 'Sistema GP rodando'}