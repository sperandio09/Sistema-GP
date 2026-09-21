from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from src.models import AdminLogin

from src.security.admin import (
    verificar_codigo_admin,
    gerar_token_admin,
    validar_token_admin
)


router = APIRouter()


@router.post("/admin/validar")
def validar_acesso_admin(
    dados: AdminLogin
):

    if not verificar_codigo_admin(
        dados.codigo
    ):

        raise HTTPException(
            status_code=401,
            detail=(
                "Código administrativo incorreto."
            )
        )

    token = gerar_token_admin()

    return {
        "token": token,
        "mensagem": (
            "Acesso administrativo autorizado."
        )
    }


@router.get("/admin/verificar")
def verificar_sessao_admin(
    _admin=Depends(
        validar_token_admin
    )
):

    return {
        "autorizado": True
    }