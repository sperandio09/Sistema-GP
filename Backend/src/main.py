from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.escuderias import router as escuderias_router
from src.routes.avaliacoes import router as avaliacoes_router
from src.routes.criterios import router as criterios_router
from src.routes.usuarios import router as usuarios_router
from src.routes.ranking import router as ranking_router
from src.routes.admin import router as admin_router

app = FastAPI(
    title="Sistema GP de Avaliação",
    version="1.0.0"
)

origins = [
    # FRONTEND LOCAL
    "http://127.0.0.1:5500",
    "http://localhost:5500",

    # BACKEND LOCAL / SWAGGER
    "http://127.0.0.1:8000",
    "http://localhost:8000",

    # FRONTEND PUBLICADO NO RAILWAY
    "https://frontend-sistema-gp-production.up.railway.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"]
)

app.include_router(escuderias_router)

app.include_router(avaliacoes_router)

app.include_router(criterios_router)

app.include_router(usuarios_router)

app.include_router(ranking_router)

app.include_router(admin_router)

@app.get("/")
def root():

    return {
        "status": "Sistema GP rodando"
    }