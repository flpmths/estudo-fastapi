from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa rota e padrao de autenticacao do sistema.
    """
    
    return {"mensagem": "Voce acessou a rota padrao de autenticacao", "autenticado": False}