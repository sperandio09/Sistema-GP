from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware 

from src.routes.escuderias import router as escuderias_router
from src.routes.avaliacoes import router as avaliacoes_router 

app = FastAPI(title = 'Sistema GP de Avaliação', version = '1.0.0')
app.include_router(escuderias_router)
app.include_router(avaliacoes_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_methods = ['*'],
    allow_headers = ['*']
)

@app.get('/')
def root():
    return {'status': 'Sistema GP rodando'}