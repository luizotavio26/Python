from sqlalchemy import Column, Integer, String
from modelos.base import Base

class Cliente(Base.Base, Base):
    __tablename__ = "Cliente"
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False)
    telefone = Column(String(50), nullable=False)
    cpf = Column(String(50), unique=True)