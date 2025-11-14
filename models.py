from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

# cria a conexão com o banco
db = create_engine ("sqlite:///banco.db")

# cria a base do banco de dados
Base = declarative_base()

class Logradouro(Base):
    __tablename__ = "logradouros"
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    cep = Column("cep",String (8), nullable = False)
    logradouro = Column("logradouro",String (255), nullable = False)
    complemento = Column("complemento",String (255))
    unidade = Column ("unidade",String (255))
    bairro = Column ("bairro",String (255,))
    localicade = Column ("localidade",String (255))
    uf = Column ("uf",String (255))
    estado = Column ("estado",String (255))
    regiao = Column ("regiao",String (255))
    ibge = Column ("ibge",Integer)
    gia = Column ("gia", Integer)
    ddd = Column ("ddd", Integer)
    siafi = Column ("siafi", Integer)

    def __init__(self, cep, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.unidade = unidade
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.estado = estado
        self.regiao = regiao
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd


    

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String (255), nullable = False)
    email = Column("email", String (255), nullable = False)
    senha = Column("senha", String (255), nullable = False)
    ativo = Column("ativo", Boolean, default = True)
    cep = Column("cep", String, ForeignKey("logradouros.id"))

    def __init__(self, nome, email, senha, ativo, cep):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.cep = cep










   