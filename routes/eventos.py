from datetime import datetime

from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from pydantic import BaseModel, ConfigDict
from sqlalchemy.orm import Session
from database import get_db
from models.evento import Evento

router = APIRouter(
    prefix="/eventos",
    tags=["eventos"],
)

class EventoItem(BaseModel):
    identificacion: str
    nombre: str
    apellido: str
    fecha_evento: datetime
    tipo_evento: str

    # Required for Pydantic v2 to map directly from ORM models
    model_config = ConfigDict(from_attributes=True)

class EventoCreate(BaseModel):
    identificacion: str
    nombre: str
    apellido: str
    tipo_evento_id: int
    # Required for Pydantic v2 to map directly from ORM models
    model_config = ConfigDict(from_attributes=True)




@router.get("/", response_model=list[EventoItem])
def get_eventos(db: Session = Depends(get_db)):
    return db.query(
        Evento.identificacion,
        Evento.nombre,
        Evento.apellido,
        Evento.fecha_evento,
        Evento.tipo_evento.has().nombre.label("tipo_evento")
    ).all()


@router.get("/{evento_id}")
def get_evento(evento_id: int, db: Session = Depends(get_db)):
    evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento not found")
    return evento

@router.post("/", response_model=EventoItem, status_code=201)
def create_evento(evento: EventoCreate, db: Session = Depends(get_db)):
    new_evento = Evento(
        identificacion=evento.identificacion,
        nombre=evento.nombre,
        apellido=evento.apellido,
        fecha_evento=datetime.now(),
        tipo_evento_id=evento.tipo_evento_id
    )

    db.add(new_evento)
    db.commit()
    db.refresh(new_evento)
    return new_evento