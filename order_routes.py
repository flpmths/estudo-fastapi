from fastapi import APIRouter

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    """
    Essa e a rota padrao de pedidos do sistema. Todas as rotas precisam de autenticacao.
    """
    
    return {"mensagem": "Voce acessou a rota de pedidos"}