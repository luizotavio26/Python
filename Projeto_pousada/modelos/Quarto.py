from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from modelos.base import Base


class Quarto(Base.Base, Base):
    __tablename__ = "Quarto"
    nro = Column(Integer, primary_key=True)
    preco = Column(Float, nullable=False)
    descricao = Column(String(50), nullable=False)

    datas = relationship('Data', back_populates='quarto')
