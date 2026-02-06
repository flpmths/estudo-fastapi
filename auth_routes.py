from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependencies import pegar_sessao
from main import bcrypt_context
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session

#modulo que cria uma fabrica para criar sessoes/Session para transacao/conversar com o banco usando engine 

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(id_usuario):
    token = f"uyhetuinasui{id_usuario}"
    return token
    

@auth_router.get("/")
async def home():
    """
    Essa rota e padrao de autenticacao do sistema.
    """
    
    return {"mensagem": "Voce acessou a rota padrao de autenticacao", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first() #all ou first
    if usuario:
        # Ja existe um usuario com esse email
        raise HTTPException(status_code=400, detail="E-mail do usuario ja cadastrado") #utilizar raise ao inves de return
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuario cadastrado com sucesso {usuario_schema.email}"}
    
    
# login -> email e senha -> token JWT (Json Web Token)

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==login_schema.email).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario nao encontrado")
    else:
        access_token = criar_token(usuario.id)
        return{
            "access_token": access_token,
            "token_type": "Bearer"
            }