
from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    preco = Column(Float, nullable=False)
    disponivel = Column(Boolean, default=True)

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)
    unidade = Column(String, nullable=False)
    produto = Column(String, nullable=False)
    quantidade = Column(Integer, nullable=False)
    valor_total = Column(Float, nullable=False)
    status = Column(String, default="Recebido")
    pagamento = Column(String, default="Pendente")