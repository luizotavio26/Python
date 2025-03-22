from sqlalchemy import Column, String
from modelos.base import Base


class Status(Base.Base, Base):
    __tablename__ = "Status"
    nome = Column(String(50), primary_key=True)
