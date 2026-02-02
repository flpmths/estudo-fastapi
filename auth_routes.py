from fastapi import APIRouter, Depends
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context

#modulo que cria uma fabrica para criar sessoes/Session para transacao/conversar com o banco usando engine 

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def autenticar():
    """
    Essa rota e padrao de autenticacao do sistema.
    """
    
    return {"mensagem": "Voce acessou a rota padrao de autenticacao", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==email).first() #all ou first
    if usuario:
        # Ja existe um usuario com esse email
        return {"mensagem": "Ja existe usuario com esse email"}
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome, email, senha)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": "Usuario cadastrado com sucesso"}
    
