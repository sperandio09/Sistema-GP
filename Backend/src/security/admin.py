import os
import json
import hmac
import base64
import hashlib
import time

from fastapi import Header, HTTPException


ADMIN_TOKEN_EXPIRACAO = 60 * 60 * 2

def _codificar_base64(dados: bytes) -> str:

    return base64.urlsafe_b64encode(
        dados
    ).decode().rstrip("=")


def _decodificar_base64(valor: str) -> bytes:

    padding = "=" * (
        4 - len(valor) % 4
    )

    return base64.urlsafe_b64decode(
        valor + padding
    )


def verificar_codigo_admin(codigo: str) -> bool:

    codigo_correto = os.getenv(
        "ADMIN_CODIGO"
    )

    if not codigo_correto:

        raise RuntimeError(
            "ADMIN_CODIGO não configurado."
        )

    return hmac.compare_digest(
        codigo,
        codigo_correto
    )


def gerar_token_admin() -> str:

    segredo = os.getenv(
        "ADMIN_TOKEN_SECRET"
    )

    if not segredo:

        raise RuntimeError(
            "ADMIN_TOKEN_SECRET não configurado."
        )

    payload = {
        "tipo": "admin",
        "exp": int(time.time()) +
               ADMIN_TOKEN_EXPIRACAO
    }

    payload_json = json.dumps(
        payload,
        separators=(",", ":")
    ).encode()

    payload_base64 = _codificar_base64(
        payload_json
    )

    assinatura = hmac.new(
        segredo.encode(),
        payload_base64.encode(),
        hashlib.sha256
    ).digest()

    assinatura_base64 = _codificar_base64(
        assinatura
    )

    return (
        f"{payload_base64}."
        f"{assinatura_base64}"
    )


def validar_token_admin(
    authorization: str | None =
        Header(default=None)
):

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Acesso administrativo não autorizado."
        )

    if not authorization.startswith(
        "Bearer "
    ):

        raise HTTPException(
            status_code=401,
            detail="Token administrativo inválido."
        )

    token = authorization[7:]

    try:

        payload_base64, assinatura_recebida = (
            token.split(".", 1)
        )

        segredo = os.getenv(
            "ADMIN_TOKEN_SECRET"
        )

        if not segredo:

            raise HTTPException(
                status_code=500,
                detail=(
                    "Configuração administrativa "
                    "indisponível."
                )
            )

        assinatura_esperada = _codificar_base64(
            hmac.new(
                segredo.encode(),
                payload_base64.encode(),
                hashlib.sha256
            ).digest()
        )

        if not hmac.compare_digest(
            assinatura_recebida,
            assinatura_esperada
        ):

            raise HTTPException(
                status_code=401,
                detail=(
                    "Sessão administrativa inválida."
                )
            )

        payload = json.loads(
            _decodificar_base64(
                payload_base64
            ).decode()
        )

        if payload.get("tipo") != "admin":

            raise HTTPException(
                status_code=401,
                detail="Token inválido."
            )

        if payload.get("exp", 0) < time.time():

            raise HTTPException(
                status_code=401,
                detail=(
                    "Sessão administrativa expirada."
                )
            )

        return True

    except HTTPException:

        raise

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Token administrativo inválido."
        )