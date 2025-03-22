from sqlalchemy import Column, Integer, String, Date, ForeignKey, PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from modelos.base import Base
from modelos.Quarto import Quarto
from modelos.Reserva import Reserva


class Data(Base.Base, Base):
    __tablename__ = "Data"
    data = Column(Date, nullable=False)
    nro_quarto = Column(Integer, ForeignKey('Quarto.nro'), nullable=False)
    status = Column(String(50), nullable=False)

    quarto = relationship('Quarto', back_populates='datas')

    __table_args__ = (
        PrimaryKeyConstraint('data', 'nro_quarto'),
    )
