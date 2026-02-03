#.venv\Scripts\Activate ##Para ativar o venv ou Ctrl + Shift + P e pesquise por "Python: Select Interpreter" e ative o recomendado
#Para rodar o codigo, executar no terminal:  uvicorn main:app --reload

#alembic revision --autogenerate -m "Initial Migration"              ##Para iniciar uma migracao do banco de dados

# Quando houver alteracao estrutural nas tabela usar o exemplo a seguir
#alembic revision --autogenerate -m "mensagem_descrevendo_a_mudanca" ##Gera nova migration
#alembic upgrade head                                                ##Aplica no banco
#Recomendado usar versao python 3.12.x | pode acontecer erro de compatibilidade entre python muito novo (3.14), passlib e bcrypt

from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)



#endpoint:
# /ordens

#REST APIs

# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> edicao
# Delete -> deletar