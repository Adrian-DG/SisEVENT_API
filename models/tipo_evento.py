from database import Base
from sqlalchemy import Column, Integer, String  
from sqlalchemy.orm import relationship

class TipoEvento(Base):
    __tablename__ = 'tipo_eventos'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
