from fastapi import FastAPI
from routes.eventos import router as eventos
from routes.tipo_eventos import router as tipo_eventos

from database import Base, engine
import models.evento, models.tipo_evento  # Import the Evento and TipoEvento models to ensure they're registered with SQLAlchemy

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="SisEVENT",
    description="API de eventos para el sistema SisEVENT",
    version="1.0.0"
)

# Registramos ENDPOINTS
app.include_router(eventos)
app.include_router(tipo_eventos)