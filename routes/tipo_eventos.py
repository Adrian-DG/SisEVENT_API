from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from database import get_db
from models.evento import Evento
import models.tipo_evento

from fastapi import APIRouter, Depends, HTTPException

router = APIRouter(
    prefix="/tipo-eventos",
    tags=["tipo-eventos"],
)

class TipoEventoItem(BaseModel):
    id: int
    nombre: str

    # Required for Pydantic v2 to map directly from ORM models
    model_config = ConfigDict(from_attributes=True)

class TipoEventoCreate(BaseModel):
    nombre: str

    # Required for Pydantic v2 to map directly from ORM models
    model_config = ConfigDict(from_attributes=True)

@router.get("/", response_model=list[TipoEventoItem])
def get_tipo_eventos(db: Session = Depends(get_db)):
    return db.query(models.tipo_evento.TipoEvento).all()

@router.post("/", response_model=TipoEventoItem)
def create_tipo_evento(tipo_evento: TipoEventoCreate, db: Session = Depends(get_db)):
    db_tipo_evento = models.tipo_evento.TipoEvento(nombre=tipo_evento.nombre)
    db.add(db_tipo_evento)
    db.commit()
    db.refresh(db_tipo_evento)
    return db_tipo_evento