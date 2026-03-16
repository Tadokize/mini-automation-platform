from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.rule import Rule
from pydantic import BaseModel

router = APIRouter(prefix="/rules", tags=["Rules"])

class RuleCreate(BaseModel):
    event_type: str
    action_type: str
    action_config: str

@router.post("/")
def create_rule(rule: RuleCreate, db: Session = Depends(get_db)):
    db_rule = Rule(
        event_type=rule.event_type,
        action_type=rule.action_type,
        action_config=rule.action_config
    )
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return db_rule

@router.get("/")
def list_rules(db: Session = Depends(get_db)):
    return db.query(Rule).all()

@router.delete("/{rule_id}")
def delete_rule(rule_id: int, db: Session = Depends(get_db)):
    rule = db.query(Rule).filter(Rule.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Regra não encontrada")
    db.delete(rule)
    db.commit()
    return {"message": "Regra removida com sucesso"}