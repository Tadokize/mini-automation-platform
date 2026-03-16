from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.execution import Execution

router = APIRouter(prefix="/executions", tags=["Executions"])

@router.get("/")
def list_executions(db: Session = Depends(get_db)):
    return db.query(Execution).all()