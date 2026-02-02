from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType # pip install sqlalchemy_utils

# instalar biblioteca alembic --> pip install alembic para migrar informacoes do banco de dados no sqlalchemy de forma segura /// no terminal digitar alembic init alembic

# Cria a conexao do banco de dados
db = create_engine("sqlite:///banco.db") # 3 barras '/' padrao sqlite

# Cria a base do banco de dados
Base = declarative_base()

### Cria a classes/tabela do banco

# Usuarios
class Usuario(Base):  
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)
    admin = Column("admin", Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False): #nao usa id como parametro porque ele foi criado automaticamente
        self.nome = nome #apos self. sao chamados de atributos
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin


# Pedido
class Pedido(Base):
    __tablename__ = "pedidos"
    
    
    # STATUS_PEDIDOS = (              #tupla como "dicionario" com chave e valor para ser usado em ChoiceType 
    #     ("PENDENTE", "PENDENTE"),
    #     ("CANCELADO", "CANCELADO"),
    #     ("FINALIZADO", "FINALIZADO")
    # )
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    status = Column("status", String) #Pendente, Cancelado e Finalizado
    usuario = Column("usuario", ForeignKey("usuarios.id")) #ForeignKey/Chave estrangeira é chamado a partir de outra tabela  - Passado o nome da tabela __tablename__ - é passado tambem um identificador unico, por exemplo: ID
    preco = Column("preco", Float)
    
    # itens = Column("itens") #a ser criado
    
    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.preco = preco
        self.status = status

        
# ItensPedido
class ItemPedido(Base):
    __tablename__ = "itens_pedidos"
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    quantidade = Column("quantidade", Integer)
    sabor = Column("sabor", String)
    tamanho = Column("tamanho", String)
    preco_unitario = Column("preco_unitario", Float)
    pedido = Column("pedido", ForeignKey("pedidos.id")) #ForeignKey/Chave estrangeira é chamado a partir de outra tabela  - Passado o nome da tabela __tablename__ - é passado tambem um identificador unico, por exemplo: ID

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido

        



#Executa a criacao do metadados do banco (cria efetivamente o banco de dados)