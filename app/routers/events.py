from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.event import Event
from app.services.automation_engine import AutomationEngine
from pydantic import BaseModel
from typing import Any

router = APIRouter(prefix="/events", tags=["Events"])

class EventCreate(BaseModel):
    event_type: str
    payload: dict[str, Any] = {}

class EventResponse(BaseModel):
    id: int
    event_type: str
    payload: dict

    class Config:
        from_attributes = True

@router.post("/", response_model=EventResponse)
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    db_event = Event(
        event_type=event.event_type,
        payload=event.payload
    )
    db.add(db_event)
    db.commit()
    db.refresh(db_event)

    engine = AutomationEngine(db)
    engine.process_event(db_event)

    return db_event

@router.get("/")
def list_events(db: Session = Depends(get_db)):
    return db.query(Event).all()