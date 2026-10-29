from sqlalchemy import Column, Integer, String, DateTime,  ForeignKey
from database import Base
from sqlalchemy.orm import relationship

class Evento(Base):
    __tablename__ = 'eventos'

    id = Column(Integer, primary_key=True, index=True)
    identificacion = Column(String, unique=True, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)     
    fecha_evento = Column(DateTime, nullable=False)
    tipo_evento_id = Column(Integer, ForeignKey('tipo_eventos.id'), nullable=False)
    tipo_evento = relationship("TipoEvento") 

