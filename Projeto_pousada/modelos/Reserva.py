from sqlalchemy import Column, Integer, String, Date, ForeignKey, ForeignKeyConstraint
from sqlalchemy.orm import relationship
from modelos.base import Base



class Reserva(Base.Base, Base):
    __tablename__ = "Reserva"
    nro = Column(Integer, primary_key=True)
    nome_status = Column(String(50), ForeignKey('Status.nome'))
    data_inicio_data = Column(Date, nullable=False)
    numero_quarto_data_inicio = Column(Integer, nullable=False)
    data_fim_data = Column(Date, nullable=False)
    nro_quarto_data_fim = Column(Integer, nullable=False)
    data = Column(Date, nullable=False)
    id_cliente = Column(Integer, ForeignKey('Cliente.id'))

    cliente = relationship('Cliente', backref= 'reservas')
    status = relationship('Status', backref= 'reservas')
    
    data_inicio = relationship('Data', foreign_keys=[data_inicio_data, numero_quarto_data_inicio], backref='reservas_inicio')
    data_fim = relationship('Data', foreign_keys=[data_fim_data, nro_quarto_data_fim], backref='reservas_fim')

    __table_args__ = (
        ForeignKeyConstraint(['data_inicio_data', 'numero_quarto_data_inicio'], ['Data.data', 'Data.nro_quarto']), 
        ForeignKeyConstraint(['data_fim_data', 'nro_quarto_data_fim'], ['Data.data', 'Data.nro_quarto'])
    )
    
